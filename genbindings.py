#!/usr/bin/env python3
import sys, re

if len(sys.argv) != 6:
    print("USAGE: /path/to/lightning.h /path/to/bindings/output.java /path/to/bindings/ /path/to/bindings/output.c debug")
    print("debug should be true or false and indicates whether to track allocations and ensure we don't leak")
    sys.exit(1)

hu_struct_file_prefix = """package org.ldk.structs;

import org.ldk.impl.bindings;
import org.ldk.enums.*;
import org.ldk.util.*;
import java.util.Arrays;

@SuppressWarnings("unchecked") // We correctly assign various generic arrays
"""

class TypeInfo:
    def __init__(self, is_native_primitive, rust_obj, java_ty, java_fn_ty_arg, java_hu_ty, c_ty, passed_as_ptr, is_ptr, var_name, arr_len, arr_access, subty=None):
        self.is_native_primitive = is_native_primitive
        self.rust_obj = rust_obj
        self.java_ty = java_ty
        self.java_hu_ty = java_hu_ty
        self.java_fn_ty_arg = java_fn_ty_arg
        self.c_ty = c_ty
        self.passed_as_ptr = passed_as_ptr
        self.is_ptr = is_ptr
        self.var_name = var_name
        self.arr_len = arr_len
        self.arr_access = arr_access
        self.subty = subty
        self.pass_by_ref = is_ptr

class ConvInfo:
    def __init__(self, ty_info, arg_name, arg_conv, arg_conv_name, arg_conv_cleanup, ret_conv, ret_conv_name, to_hu_conv, to_hu_conv_name, from_hu_conv):
        assert(ty_info.c_ty is not None)
        assert(ty_info.java_ty is not None)
        assert(arg_name is not None)
        self.passed_as_ptr = ty_info.passed_as_ptr
        self.rust_obj = ty_info.rust_obj
        self.c_ty = ty_info.c_ty
        self.java_ty = ty_info.java_ty
        self.java_hu_ty = ty_info.java_hu_ty
        self.java_fn_ty_arg = ty_info.java_fn_ty_arg
        self.arg_name = arg_name
        self.arg_conv = arg_conv
        self.arg_conv_name = arg_conv_name
        self.arg_conv_cleanup = arg_conv_cleanup
        self.ret_conv = ret_conv
        self.ret_conv_name = ret_conv_name
        self.to_hu_conv = to_hu_conv
        self.to_hu_conv_name = to_hu_conv_name
        self.from_hu_conv = from_hu_conv

    def print_ty(self):
        out_c.write(self.c_ty)
        out_java.write(self.java_ty)

    def print_name(self):
        if self.arg_name != "":
            out_java.write(" " + self.arg_name)
            out_c.write(" " + self.arg_name)
        else:
            out_java.write(" arg")
            out_c.write(" arg")

def camel_to_snake(s):
    # Convert camel case to snake case, in a way that appears to match cbindgen
    con = "_"
    ret = ""
    lastchar = ""
    lastund = False
    for char in s:
        if lastchar.isupper():
            if not char.isupper() and not lastund:
                ret = ret + "_"
                lastund = True
            else:
                lastund = False
            ret = ret + lastchar.lower()
        else:
            ret = ret + lastchar
            if char.isupper() and not lastund:
                ret = ret + "_"
                lastund = True
            else:
                lastund = False
        lastchar = char
        if char.isnumeric():
            lastund = True
    return (ret + lastchar.lower()).strip("_")

unitary_enums = set()
complex_enums = set()
opaque_structs = set()
trait_structs = set()
tuple_types = {}

var_is_arr_regex = re.compile("\(\*([A-za-z0-9_]*)\)\[([a-z0-9]*)\]")
var_ty_regex = re.compile("([A-za-z_0-9]*)(.*)")
java_c_types_none_allowed = True # Unset when we do the real pass that populates the above sets
def java_c_types(fn_arg, ret_arr_len):
    fn_arg = fn_arg.strip()
    if fn_arg.startswith("MUST_USE_RES "):
        fn_arg = fn_arg[13:]
    is_const = False
    if fn_arg.startswith("const "):
        fn_arg = fn_arg[6:]
        is_const = True

    is_ptr = False
    take_by_ptr = False
    rust_obj = None
    arr_access = None
    java_hu_ty = None
    if fn_arg.startswith("LDKThirtyTwoBytes"):
        fn_arg = "uint8_t (*" + fn_arg[18:] + ")[32]"
        assert var_is_arr_regex.match(fn_arg[8:])
        rust_obj = "LDKThirtyTwoBytes"
        arr_access = "data"
    elif fn_arg.startswith("LDKPublicKey"):
        fn_arg = "uint8_t (*" + fn_arg[13:] + ")[33]"
        assert var_is_arr_regex.match(fn_arg[8:])
        rust_obj = "LDKPublicKey"
        arr_access = "compressed_form"
    elif fn_arg.startswith("LDKSecretKey"):
        fn_arg = "uint8_t (*" + fn_arg[13:] + ")[32]"
        assert var_is_arr_regex.match(fn_arg[8:])
        rust_obj = "LDKSecretKey"
        arr_access = "bytes"
    elif fn_arg.startswith("LDKSignature"):
        fn_arg = "uint8_t (*" + fn_arg[13:] + ")[64]"
        assert var_is_arr_regex.match(fn_arg[8:])
        rust_obj = "LDKSignature"
        arr_access = "compact_form"
    elif fn_arg.startswith("LDKThreeBytes"):
        fn_arg = "uint8_t (*" + fn_arg[14:] + ")[3]"
        assert var_is_arr_regex.match(fn_arg[8:])
        rust_obj = "LDKThreeBytes"
        arr_access = "data"
    elif fn_arg.startswith("LDKFourBytes"):
        fn_arg = "uint8_t (*" + fn_arg[13:] + ")[4]"
        assert var_is_arr_regex.match(fn_arg[8:])
        rust_obj = "LDKFourBytes"
        arr_access = "data"
    elif fn_arg.startswith("LDKSixteenBytes"):
        fn_arg = "uint8_t (*" + fn_arg[16:] + ")[16]"
        assert var_is_arr_regex.match(fn_arg[8:])
        rust_obj = "LDKSixteenBytes"
        arr_access = "data"
    elif fn_arg.startswith("LDKTenBytes"):
        fn_arg = "uint8_t (*" + fn_arg[12:] + ")[10]"
        assert var_is_arr_regex.match(fn_arg[8:])
        rust_obj = "LDKTenBytes"
        arr_access = "data"
    elif fn_arg.startswith("LDKu8slice"):
        fn_arg = "uint8_t (*" + fn_arg[11:] + ")[datalen]"
        assert var_is_arr_regex.match(fn_arg[8:])
        rust_obj = "LDKu8slice"
        arr_access = "data"
    elif fn_arg.startswith("LDKCVecTempl_u8") or fn_arg.startswith("LDKCVec_u8Z"):
        if fn_arg.startswith("LDKCVecTempl_u8"):
            fn_arg = "uint8_t (*" + fn_arg[16:] + ")[datalen]"
            rust_obj = "LDKCVecTempl_u8"
            assert var_is_arr_regex.match(fn_arg[8:])
        else:
            fn_arg = "uint8_t (*" + fn_arg[12:] + ")[datalen]"
            rust_obj = "LDKCVec_u8Z"
            assert var_is_arr_regex.match(fn_arg[8:])
        arr_access = "data"
    elif fn_arg.startswith("LDKCVecTempl_") or fn_arg.startswith("LDKCVec_"):
        is_ptr = False
        if "*" in fn_arg:
            fn_arg = fn_arg.replace("*", "")
            is_ptr = True

        if fn_arg.startswith("LDKCVec_"):
            tyn = fn_arg[8:].split(" ")
            assert tyn[0].endswith("Z")
            if tyn[0] == "u64Z":
                new_arg = "uint64_t"
            else:
                new_arg = "LDK" + tyn[0][:-1]
            for a in tyn[1:]:
                new_arg = new_arg + " " + a
            res = java_c_types(new_arg, ret_arr_len)
        else:
            res = java_c_types("LDK" + fn_arg[13:], ret_arr_len)
        if res is None:
            assert java_c_types_none_allowed
            return None
        if is_ptr:
            res.pass_by_ref = True
        if res.is_native_primitive or res.passed_as_ptr:
            return TypeInfo(rust_obj=fn_arg.split(" ")[0], java_ty=res.java_ty + "[]", java_hu_ty=res.java_hu_ty + "[]",
                java_fn_ty_arg="[" + res.java_fn_ty_arg, c_ty=res.c_ty + "Array", passed_as_ptr=False, is_ptr=is_ptr,
                var_name=res.var_name, arr_len="datalen", arr_access="data", subty=res, is_native_primitive=False)
        else:
            return TypeInfo(rust_obj=fn_arg.split(" ")[0], java_ty=res.java_ty + "[]", java_hu_ty=res.java_hu_ty + "[]",
                java_fn_ty_arg="[" + res.java_fn_ty_arg, c_ty="jobjectArray", passed_as_ptr=False, is_ptr=is_ptr,
                var_name=res.var_name, arr_len="datalen", arr_access="data", subty=res, is_native_primitive=False)

    is_primitive = False
    arr_len = None
    if fn_arg.startswith("void"):
        java_ty = "void"
        c_ty = "void"
        fn_ty_arg = "V"
        fn_arg = fn_arg[4:].strip()
        is_primitive = True
    elif fn_arg.startswith("bool"):
        java_ty = "boolean"
        c_ty = "jboolean"
        fn_ty_arg = "Z"
        fn_arg = fn_arg[4:].strip()
        is_primitive = True
    elif fn_arg.startswith("uint8_t"):
        java_ty = "byte"
        c_ty = "jbyte"
        fn_ty_arg = "B"
        fn_arg = fn_arg[7:].strip()
        is_primitive = True
    elif fn_arg.startswith("uint16_t"):
        java_ty = "short"
        c_ty = "jshort"
        fn_ty_arg = "S"
        fn_arg = fn_arg[8:].strip()
        is_primitive = True
    elif fn_arg.startswith("uint32_t"):
        java_ty = "int"
        c_ty = "jint"
        fn_ty_arg = "I"
        fn_arg = fn_arg[8:].strip()
        is_primitive = True
    elif fn_arg.startswith("uint64_t") or fn_arg.startswith("uintptr_t"):
        java_ty = "long"
        c_ty = "jlong"
        fn_ty_arg = "J"
        if fn_arg.startswith("uint64_t"):
            fn_arg = fn_arg[8:].strip()
        else:
            fn_arg = fn_arg[9:].strip()
        is_primitive = True
    elif is_const and fn_arg.startswith("char *"):
        java_ty = "String"
        c_ty = "const char*"
        fn_ty_arg = "Ljava/lang/String;"
        fn_arg = fn_arg[6:].strip()
    elif fn_arg.startswith("LDKStr"):
        java_ty = "String"
        c_ty = "jstring"
        fn_ty_arg = "Ljava/lang/String;"
        fn_arg = fn_arg[6:].strip()
        arr_access = "chars"
        arr_len = "len"
    else:
        ma = var_ty_regex.match(fn_arg)
        if ma.group(1).strip() in unitary_enums:
            java_ty = ma.group(1).strip()
            c_ty = "jclass"
            fn_ty_arg = "Lorg/ldk/enums/" + ma.group(1).strip() + ";"
            fn_arg = ma.group(2).strip()
            rust_obj = ma.group(1).strip()
            take_by_ptr = True
        elif ma.group(1).strip().startswith("LDKC2Tuple"):
            java_ty = "long"
            java_hu_ty = "TwoTuple<"
            if not ma.group(1).strip() in tuple_types:
                assert java_c_types_none_allowed
                return None
            for idx, ty_info in enumerate(tuple_types[ma.group(1).strip()][0]):
                if idx != 0:
                    java_hu_ty = java_hu_ty + ", "
                if ty_info.is_native_primitive:
                    java_hu_ty = java_hu_ty + ty_info.java_hu_ty.title() # If we're a primitive, capitalize the first letter
                else:
                    java_hu_ty = java_hu_ty + ty_info.java_hu_ty
            java_hu_ty = java_hu_ty + ">"
            c_ty = "jlong"
            fn_ty_arg = "J"
            fn_arg = ma.group(2).strip()
            rust_obj = ma.group(1).strip()
            take_by_ptr = True
        elif ma.group(1).strip().startswith("LDKC3Tuple"):
            java_ty = "long"
            java_hu_ty = "ThreeTuple<"
            if not ma.group(1).strip() in tuple_types:
                assert java_c_types_none_allowed
                return None
            for idx, ty_info in enumerate(tuple_types[ma.group(1).strip()][0]):
                if idx != 0:
                    java_hu_ty = java_hu_ty + ", "
                if ty_info.is_native_primitive:
                    java_hu_ty = java_hu_ty + ty_info.java_hu_ty.title() # If we're a primitive, capitalize the first letter
                else:
                    java_hu_ty = java_hu_ty + ty_info.java_hu_ty
            java_hu_ty = java_hu_ty + ">"
            c_ty = "jlong"
            fn_ty_arg = "J"
            fn_arg = ma.group(2).strip()
            rust_obj = ma.group(1).strip()
            take_by_ptr = True
        else:
            java_ty = "long"
            java_hu_ty = ma.group(1).strip().replace("LDK", "")
            c_ty = "jlong"
            fn_ty_arg = "J"
            fn_arg = ma.group(2).strip()
            rust_obj = ma.group(1).strip()
            take_by_ptr = True

    if fn_arg.startswith(" *") or fn_arg.startswith("*"):
        fn_arg = fn_arg.replace("*", "").strip()
        is_ptr = True
        c_ty = "jlong"
        java_ty = "long"
        fn_ty_arg = "J"
        is_primitive = False

    var_is_arr = var_is_arr_regex.match(fn_arg)
    if var_is_arr is not None or ret_arr_len is not None:
        assert(not take_by_ptr)
        assert(not is_ptr)
        java_ty = java_ty + "[]"
        c_ty = c_ty + "Array"
        if var_is_arr is not None:
            if var_is_arr.group(1) == "":
                return TypeInfo(rust_obj=rust_obj, java_ty=java_ty, java_hu_ty=java_ty, java_fn_ty_arg="[" + fn_ty_arg, c_ty=c_ty,
                    passed_as_ptr=False, is_ptr=False, var_name="arg", arr_len=var_is_arr.group(2), arr_access=arr_access, is_native_primitive=False)
            return TypeInfo(rust_obj=rust_obj, java_ty=java_ty, java_hu_ty=java_ty, java_fn_ty_arg="[" + fn_ty_arg, c_ty=c_ty,
                passed_as_ptr=False, is_ptr=False, var_name=var_is_arr.group(1), arr_len=var_is_arr.group(2), arr_access=arr_access, is_native_primitive=False)

    if java_hu_ty is None:
        java_hu_ty = java_ty
    return TypeInfo(rust_obj=rust_obj, java_ty=java_ty, java_hu_ty=java_hu_ty, java_fn_ty_arg=fn_ty_arg, c_ty=c_ty, passed_as_ptr=is_ptr or take_by_ptr,
        is_ptr=is_ptr, var_name=fn_arg, arr_len=arr_len, arr_access=arr_access, is_native_primitive=is_primitive)

fn_ptr_regex = re.compile("^extern const ([A-Za-z_0-9\* ]*) \(\*(.*)\)\((.*)\);$")
fn_ret_arr_regex = re.compile("(.*) \(\*(.*)\((.*)\)\)\[([0-9]*)\];$")
reg_fn_regex = re.compile("([A-Za-z_0-9\* ]* \*?)([a-zA-Z_0-9]*)\((.*)\);$")
clone_fns = set()
constructor_fns = {}
with open(sys.argv[1]) as in_h:
    for line in in_h:
        reg_fn = reg_fn_regex.match(line)
        if reg_fn is not None:
            if reg_fn.group(2).endswith("_clone"):
                clone_fns.add(reg_fn.group(2))
            else:
                rty = java_c_types(reg_fn.group(1), None)
                if rty is not None and rty.rust_obj is not None and reg_fn.group(2) == rty.java_hu_ty + "_new":
                    constructor_fns[rty.rust_obj] = reg_fn.group(3)
            continue
        arr_fn = fn_ret_arr_regex.match(line)
        if arr_fn is not None:
            if arr_fn.group(2).endswith("_clone"):
                clone_fns.add(arr_fn.group(2))
            # No object constructors return arrays, as then they wouldn't be an object constructor
            continue
java_c_types_none_allowed = False # C structs created by cbindgen are declared in dependency order

with open(sys.argv[1]) as in_h, open(sys.argv[2], "w") as out_java, open(sys.argv[4], "w") as out_c:
    def map_type(fn_arg, print_void, ret_arr_len, is_free, holds_ref):
        ty_info = java_c_types(fn_arg, ret_arr_len)
        return map_type_with_info(ty_info, print_void, ret_arr_len, is_free, holds_ref)

    def map_type_with_info(ty_info, print_void, ret_arr_len, is_free, holds_ref):
        if ty_info.c_ty == "void":
            if not print_void:
                return ConvInfo(ty_info = ty_info, arg_name = ty_info.var_name,
                    arg_conv = None, arg_conv_name = None, arg_conv_cleanup = None,
                    ret_conv = None, ret_conv_name = None, to_hu_conv = None, to_hu_conv_name = None, from_hu_conv = None)
        if ty_info.c_ty.endswith("Array"):
            arr_len = ty_info.arr_len
            if arr_len is not None:
                arr_name = ty_info.var_name
            else:
                arr_name = "ret"
                arr_len = ret_arr_len
            if ty_info.c_ty == "jbyteArray":
                ret_conv = ("jbyteArray " + arr_name + "_arr = (*_env)->NewByteArray(_env, " + arr_len + ");\n" + "(*_env)->SetByteArrayRegion(_env, " + arr_name + "_arr, 0, " + arr_len + ", ", "")
                arg_conv_cleanup = None
                if not arr_len.isdigit():
                    arg_conv = ty_info.rust_obj + " " + arr_name + "_ref;\n"
                    arg_conv = arg_conv + arr_name + "_ref." + ty_info.arr_access + " = (*_env)->GetByteArrayElements (_env, " + arr_name + ", NULL);\n"
                    arg_conv = arg_conv + arr_name + "_ref." + arr_len + " = (*_env)->GetArrayLength (_env, " + arr_name + ");"
                    arg_conv_cleanup = "(*_env)->ReleaseByteArrayElements(_env, " + arr_name + ", (int8_t*)" + arr_name + "_ref." + ty_info.arr_access + ", 0);"
                    ret_conv = (ty_info.rust_obj + " " + arr_name + "_var = ", "")
                    ret_conv = (ret_conv[0], ";\njbyteArray " + arr_name + "_arr = (*_env)->NewByteArray(_env, " + arr_name + "_var." + arr_len + ");\n")
                    ret_conv = (ret_conv[0], ret_conv[1] + "(*_env)->SetByteArrayRegion(_env, " + arr_name + "_arr, 0, " + arr_name + "_var." + arr_len + ", " + arr_name + "_var." + ty_info.arr_access + ");")
                    if not holds_ref and ty_info.rust_obj == "LDKCVec_u8Z":
                        ret_conv = (ret_conv[0], ret_conv[1] + "\nCVec_u8Z_free(" + arr_name + "_var);")
                elif ty_info.rust_obj is not None:
                    arg_conv = ty_info.rust_obj + " " + arr_name + "_ref;\n"
                    arg_conv = arg_conv + "CHECK((*_env)->GetArrayLength (_env, " + arr_name + ") == " + arr_len + ");\n"
                    arg_conv = arg_conv + "(*_env)->GetByteArrayRegion (_env, " + arr_name + ", 0, " + arr_len + ", " + arr_name + "_ref." + ty_info.arr_access + ");"
                    ret_conv = (ret_conv[0], "." + ty_info.arr_access + ");")
                else:
                    arg_conv = "unsigned char " + arr_name + "_arr[" + arr_len + "];\n"
                    arg_conv = arg_conv + "CHECK((*_env)->GetArrayLength (_env, " + arr_name + ") == " + arr_len + ");\n"
                    arg_conv = arg_conv + "(*_env)->GetByteArrayRegion (_env, " + arr_name + ", 0, " + arr_len + ", " + arr_name + "_arr);\n" + "unsigned char (*" + arr_name + "_ref)[" + arr_len + "] = &" + arr_name + "_arr;"
                    ret_conv = (ret_conv[0] + "*", ");")
                return ConvInfo(ty_info = ty_info, arg_name = ty_info.var_name,
                    arg_conv = arg_conv, arg_conv_name = arr_name + "_ref", arg_conv_cleanup = arg_conv_cleanup,
                    ret_conv = ret_conv, ret_conv_name = arr_name + "_arr", to_hu_conv = None, to_hu_conv_name = None, from_hu_conv = None)
            else:
                assert not arr_len.isdigit() # fixed length arrays not implemented
                assert ty_info.java_ty[len(ty_info.java_ty) - 2:] == "[]"
                conv_name = "arr_conv_" + str(len(ty_info.java_hu_ty))
                idxc = chr(ord('a') + (len(ty_info.java_hu_ty) % 26))
                ty_info.subty.var_name = conv_name
                subty = map_type_with_info(ty_info.subty, False, None, is_free, holds_ref)
                if arr_name == "":
                    arr_name = "arg"
                arg_conv = ty_info.rust_obj + " " + arr_name + "_constr;\n"
                arg_conv = arg_conv + arr_name + "_constr." + arr_len + " = (*_env)->GetArrayLength (_env, " + arr_name + ");\n"
                arg_conv = arg_conv + "if (" + arr_name + "_constr." + arr_len + " > 0)\n"
                if subty.rust_obj is None:
                    szof = subty.c_ty
                else:
                    szof = subty.rust_obj
                arg_conv = arg_conv + "\t" + arr_name + "_constr." + ty_info.arr_access + " = MALLOC(" + arr_name + "_constr." + arr_len + " * sizeof(" + szof + "), \"" + ty_info.rust_obj + " Elements\");\n"
                arg_conv = arg_conv + "else\n"
                arg_conv = arg_conv + "\t" + arr_name + "_constr." + ty_info.arr_access + " = NULL;\n"
                if not ty_info.java_ty[:len(ty_info.java_ty) - 2].endswith("[]"):
                    arg_conv = arg_conv + ty_info.java_ty.strip("[]") + "* " + arr_name + "_vals = (*_env)->Get" + ty_info.subty.java_ty.title() + "ArrayElements (_env, " + arr_name + ", NULL);\n"
                arg_conv = arg_conv + "for (size_t " + idxc + " = 0; " + idxc + " < " + arr_name + "_constr." + arr_len + "; " + idxc + "++) {\n"
                if not ty_info.java_ty[:len(ty_info.java_ty) - 2].endswith("[]"):
                    arg_conv = arg_conv + "\t" + ty_info.java_ty.strip("[]") + " " + conv_name + " = " + arr_name + "_vals[" + idxc + "];"
                    if subty.arg_conv is not None:
                        arg_conv = arg_conv + "\n\t" + subty.arg_conv.replace("\n", "\n\t")
                else:
                    arg_conv = arg_conv + "\tjobject " + conv_name + " = (*_env)->GetObjectArrayElement(_env, " + arr_name + ", " + idxc + ");\n"
                    arg_conv = arg_conv + "\t" + subty.arg_conv.replace("\n", "\n\t")
                arg_conv = arg_conv + "\n\t" + arr_name + "_constr." + ty_info.arr_access + "[" + idxc + "] = " + subty.arg_conv_name + ";\n}"
                if not ty_info.java_ty[:len(ty_info.java_ty) - 2].endswith("[]"):
                    arg_conv = arg_conv + "\n(*_env)->Release" + ty_info.java_ty.strip("[]").title() + "ArrayElements (_env, " + arr_name + ", " + arr_name + "_vals, 0);"
                if ty_info.is_ptr:
                    arg_conv_name = "&" + arr_name + "_constr"
                else:
                    arg_conv_name = arr_name + "_constr"
                arg_conv_cleanup = None
                if ty_info.is_ptr:
                    arg_conv_cleanup = "FREE(" + arr_name + "_constr." + ty_info.arr_access + ");"

                if arr_name == "arg":
                    arr_name = "ret"
                ret_conv = (ty_info.rust_obj + " " + arr_name + "_var = ", "")
                if subty.ret_conv is None:
                    ret_conv = ("DUMMY", "DUMMY")
                elif not ty_info.java_ty[:len(ty_info.java_ty) - 2].endswith("[]"):
                    ret_conv = (ret_conv[0], ";\n" + ty_info.c_ty + " " + arr_name + "_arr = (*_env)->New" + ty_info.java_ty.strip("[]").title() + "Array(_env, " + arr_name + "_var." + arr_len + ");\n")
                    ret_conv = (ret_conv[0], ret_conv[1] + subty.c_ty + " *" + arr_name + "_arr_ptr = (*_env)->GetPrimitiveArrayCritical(_env, " + arr_name + "_arr, NULL);\n")
                    ret_conv = (ret_conv[0], ret_conv[1] + "for (size_t " + idxc + " = 0; " + idxc + " < " + arr_name + "_var." + arr_len + "; " + idxc + "++) {\n")
                    ret_conv = (ret_conv[0], ret_conv[1] + "\t" + subty.ret_conv[0].replace("\n", "\n\t"))
                    ret_conv = (ret_conv[0], ret_conv[1] + arr_name + "_var." + ty_info.arr_access + "[" + idxc + "]" + subty.ret_conv[1].replace("\n", "\n\t"))
                    ret_conv = (ret_conv[0], ret_conv[1] + "\n\t" + arr_name + "_arr_ptr[" + idxc + "] = " + subty.ret_conv_name + ";\n")
                    ret_conv = (ret_conv[0], ret_conv[1] + "}\n(*_env)->ReleasePrimitiveArrayCritical(_env, " + arr_name + "_arr, " + arr_name + "_arr_ptr, 0);")
                else:
                    ret_conv = (ret_conv[0], ";\n" + ty_info.c_ty + " " + arr_name + "_arr = (*_env)->NewObjectArray(_env, " + arr_name + "_var." + arr_len + ", NULL, NULL);\n") # XXX: second arg needs to be a clazz!
                    ret_conv = (ret_conv[0], ret_conv[1] + "for (size_t " + idxc + " = 0; " + idxc + " < " + arr_name + "_var." + arr_len + "; " + idxc + "++) {\n")
                    ret_conv = (ret_conv[0], ret_conv[1] + "\t" + subty.ret_conv[0].replace("\n", "\n\t"))
                    ret_conv = (ret_conv[0], ret_conv[1] + arr_name + "_var." + ty_info.arr_access + "[" + idxc + "]" + subty.ret_conv[1].replace("\n", "\n\t"))
                    ret_conv = (ret_conv[0], ret_conv[1] + "\n\t(*_env)->SetObjectArrayElement(_env, " + arr_name + "_arr, " + idxc + ", " + subty.ret_conv_name + ");\n")
                    ret_conv = (ret_conv[0], ret_conv[1] + "}")
                if not holds_ref:
                    if subty.rust_obj is not None and subty.rust_obj in opaque_structs:
                        ret_conv = (ret_conv[0], ret_conv[1] + "\nFREE(" + arr_name + "_var." + ty_info.arr_access + ");")
                    else:
                        ret_conv = (ret_conv[0], ret_conv[1] + "\n" + ty_info.rust_obj.replace("LDK", "") + "_free(" + arr_name + "_var);")

                to_hu_conv = None
                to_hu_conv_name = None
                if subty.to_hu_conv is not None:
                    to_hu_conv = ty_info.java_hu_ty + " " + conv_name + "_arr = new " + ty_info.subty.java_hu_ty.split("<")[0] + "[" + arr_name + ".length];\n"
                    to_hu_conv = to_hu_conv + "for (int " + idxc + " = 0; " + idxc + " < " + arr_name + ".length; " + idxc + "++) {\n"
                    to_hu_conv = to_hu_conv + "\t" + subty.java_ty + " " + conv_name + " = " + arr_name + "[" + idxc + "];\n"
                    to_hu_conv = to_hu_conv + "\t" + subty.to_hu_conv.replace("\n", "\n\t") + "\n"
                    to_hu_conv = to_hu_conv + "\t" + conv_name + "_arr[" + idxc + "] = " + subty.to_hu_conv_name + ";\n}"
                    to_hu_conv_name = conv_name + "_arr"
                from_hu_conv = None
                if subty.from_hu_conv is not None:
                    if subty.java_ty == "long" and subty.java_hu_ty != "long":
                        from_hu_conv = ("Arrays.stream(" + arr_name + ").mapToLong(" + conv_name + " -> " + subty.from_hu_conv[0] + ").toArray()", "/* TODO 2 " + subty.java_hu_ty + "  */")
                    elif subty.java_ty == "long":
                        from_hu_conv = ("Arrays.stream(" + arr_name + ").map(" + conv_name + " -> " + subty.from_hu_conv[0] + ").toArray()", "/* TODO 2 " + subty.java_hu_ty + "  */")
                    else:
                        from_hu_conv = ("(" + ty_info.java_ty + ")Arrays.stream(" + arr_name + ").map(" + conv_name + " -> " + subty.from_hu_conv[0] + ").toArray()", "/* TODO 2 " + subty.java_hu_ty + "  */")

                return ConvInfo(ty_info = ty_info, arg_name = ty_info.var_name,
                    arg_conv = arg_conv, arg_conv_name = arg_conv_name, arg_conv_cleanup = arg_conv_cleanup,
                    ret_conv = ret_conv, ret_conv_name = arr_name + "_arr", to_hu_conv = to_hu_conv, to_hu_conv_name = to_hu_conv_name, from_hu_conv = from_hu_conv)
        elif ty_info.java_ty == "String":
            if ty_info.arr_access is None:
                return ConvInfo(ty_info = ty_info, arg_name = ty_info.var_name,
                    arg_conv = None, arg_conv_name = None, arg_conv_cleanup = None,
                    ret_conv = ("jstring " + ty_info.var_name + "_conv = (*_env)->NewStringUTF(_env, ", ");"), ret_conv_name = ty_info.var_name + "_conv",
                    to_hu_conv = None, to_hu_conv_name = None, from_hu_conv = None)
            else:
                return ConvInfo(ty_info = ty_info, arg_name = ty_info.var_name,
                    arg_conv = None, arg_conv_name = None, arg_conv_cleanup = None,
                    ret_conv = ("LDKStr " + ty_info.var_name + "_str = ",
                        ";\nchar* " + ty_info.var_name + "_buf = MALLOC(" + ty_info.var_name + "_str." + ty_info.arr_len + " + 1, \"str conv buf\");\n" +
                        "memcpy(" + ty_info.var_name + "_buf, " + ty_info.var_name + "_str." + ty_info.arr_access + ", " + ty_info.var_name + "_str." + ty_info.arr_len + ");\n" +
                        ty_info.var_name + "_buf[" + ty_info.var_name + "_str." + ty_info.arr_len + "] = 0;\n" +
                        "jstring " + ty_info.var_name + "_conv = (*_env)->NewStringUTF(_env, " + ty_info.var_name + "_str." + ty_info.arr_access + ");\n" +
                        "FREE(" + ty_info.var_name + "_buf);"),
                    ret_conv_name = ty_info.var_name + "_conv", to_hu_conv = None, to_hu_conv_name = None, from_hu_conv = None)
        elif ty_info.var_name != "":
            # If we have a parameter name, print it (noting that it may indicate its a pointer)
            if ty_info.rust_obj is not None:
                assert(ty_info.passed_as_ptr)
                opaque_arg_conv = ty_info.rust_obj + " " + ty_info.var_name + "_conv;\n"
                opaque_arg_conv = opaque_arg_conv + ty_info.var_name + "_conv.inner = (void*)(" + ty_info.var_name + " & (~1));\n"
                opaque_arg_conv = opaque_arg_conv + ty_info.var_name + "_conv.is_owned = (" + ty_info.var_name + " & 1) || (" + ty_info.var_name + " == 0);"
                if not ty_info.is_ptr and not is_free and not ty_info.pass_by_ref:
                    if (ty_info.java_hu_ty + "_clone") in clone_fns:
                        # TODO: This is a bit too naive, even with the checks above, we really need to know if rust wants a ref or not, not just if its pass as a ptr.
                        opaque_arg_conv = opaque_arg_conv + "\nif (" + ty_info.var_name + "_conv.inner != NULL)\n"
                        opaque_arg_conv = opaque_arg_conv + "\t" + ty_info.var_name + "_conv = " + ty_info.java_hu_ty + "_clone(&" + ty_info.var_name + "_conv);"
                    elif ty_info.passed_as_ptr:
                        opaque_arg_conv = opaque_arg_conv + "\n// Warning: we may need a move here but can't clone!"
                if not ty_info.is_ptr:
                    if ty_info.rust_obj in unitary_enums:
                        return ConvInfo(ty_info = ty_info, arg_name = ty_info.var_name,
                            arg_conv = ty_info.rust_obj + " " + ty_info.var_name + "_conv = " + ty_info.rust_obj + "_from_java(_env, " + ty_info.var_name + ");",
                            arg_conv_name = ty_info.var_name + "_conv",
                            arg_conv_cleanup = None,
                            ret_conv = ("jclass " + ty_info.var_name + "_conv = " + ty_info.rust_obj + "_to_java(_env, ", ");"),
                            ret_conv_name = ty_info.var_name + "_conv", to_hu_conv = None, to_hu_conv_name = None, from_hu_conv = None)
                    if ty_info.rust_obj in opaque_structs:
                        ret_conv_suf = ";\nCHECK((((long)" + ty_info.var_name + "_var.inner) & 1) == 0); // We rely on a free low bit, malloc guarantees this.\n"
                        ret_conv_suf = ret_conv_suf + "CHECK((((long)&" + ty_info.var_name + "_var) & 1) == 0); // We rely on a free low bit, pointer alignment guarantees this.\n"
                        if holds_ref:
                            ret_conv_suf = ret_conv_suf + "long " + ty_info.var_name + "_ref = (long)" + ty_info.var_name + "_var.inner & ~1;"
                        else:
                            ret_conv_suf = ret_conv_suf + "long " + ty_info.var_name + "_ref;\n"
                            ret_conv_suf = ret_conv_suf + "if (" + ty_info.var_name + "_var.is_owned) {\n"
                            ret_conv_suf = ret_conv_suf + "\t" + ty_info.var_name + "_ref = (long)" + ty_info.var_name + "_var.inner | 1;\n"
                            ret_conv_suf = ret_conv_suf + "} else {\n"
                            ret_conv_suf = ret_conv_suf + "\t" + ty_info.var_name + "_ref = (long)" + ty_info.var_name + "_var.inner & ~1;\n"
                            ret_conv_suf = ret_conv_suf + "}"
                        return ConvInfo(ty_info = ty_info, arg_name = ty_info.var_name,
                            arg_conv = opaque_arg_conv, arg_conv_name = ty_info.var_name + "_conv", arg_conv_cleanup = None,
                            ret_conv = (ty_info.rust_obj + " " + ty_info.var_name + "_var = ", ret_conv_suf),
                            ret_conv_name = ty_info.var_name + "_ref",
                            to_hu_conv = ty_info.java_hu_ty + " " + ty_info.var_name + "_hu_conv = new " + ty_info.java_hu_ty + "(null, " + ty_info.var_name + ");",
                            to_hu_conv_name = ty_info.var_name + "_hu_conv",
                            from_hu_conv = (ty_info.var_name + " == null ? 0 : " + ty_info.var_name + ".ptr & ~1", "this.ptrs_to.add(" + ty_info.var_name + ")"))
                    base_conv = ty_info.rust_obj + " " + ty_info.var_name + "_conv = *(" + ty_info.rust_obj + "*)" + ty_info.var_name + ";";
                    if ty_info.rust_obj in trait_structs:
                        if not is_free:
                            base_conv = base_conv + "\nif (" + ty_info.var_name + "_conv.free == " + ty_info.rust_obj + "_JCalls_free) {\n"
                            base_conv = base_conv + "\t// If this_arg is a JCalls struct, then we need to increment the refcnt in it.\n"
                            base_conv = base_conv + "\t" + ty_info.rust_obj + "_JCalls_clone(" + ty_info.var_name + "_conv.this_arg);\n}"
                        else:
                            base_conv = base_conv + "\n" + "FREE((void*)" + ty_info.var_name + ");"
                        return ConvInfo(ty_info = ty_info, arg_name = ty_info.var_name,
                            arg_conv = base_conv, arg_conv_name = ty_info.var_name + "_conv", arg_conv_cleanup = None,
                            ret_conv = ("CANT PASS TRAIT TO Java?", ""), ret_conv_name = "NO CONV POSSIBLE",
                            to_hu_conv = "DUMMY", to_hu_conv_name = None,
                            from_hu_conv = (ty_info.var_name + " == null ? 0 : " + ty_info.var_name + ".ptr", "this.ptrs_to.add(" + ty_info.var_name + ")"))
                    if ty_info.rust_obj != "LDKu8slice":
                        # Don't bother free'ing slices passed in - Rust doesn't auto-free the
                        # underlying unlike Vecs, and it gives Java more freedom.
                        base_conv = base_conv + "\nFREE((void*)" + ty_info.var_name + ");";
                    if ty_info.rust_obj in complex_enums:
                        ret_conv = ("long " + ty_info.var_name + "_ref = (long)&", ";")
                        if not ty_info.is_ptr and not holds_ref and (ty_info.java_hu_ty + "_clone") in clone_fns:
                            ret_conv = (ty_info.rust_obj + " *" + ty_info.var_name + "_copy = MALLOC(sizeof(" + ty_info.rust_obj + "), \"" + ty_info.rust_obj + "\");\n", "")
                            ret_conv = (ret_conv[0] + "*" + ty_info.var_name + "_copy = " + ty_info.java_hu_ty + "_clone(&", ");\n")
                            ret_conv = (ret_conv[0], ret_conv[1] + "long " + ty_info.var_name + "_ref = (long)" + ty_info.var_name + "_copy;")
                        return ConvInfo(ty_info = ty_info, arg_name = ty_info.var_name,
                            arg_conv = base_conv, arg_conv_name = ty_info.var_name + "_conv", arg_conv_cleanup = None,
                            ret_conv = ret_conv, ret_conv_name = ty_info.var_name + "_ref",
                            to_hu_conv = ty_info.java_hu_ty + " " + ty_info.var_name + "_hu_conv = " + ty_info.java_hu_ty + ".constr_from_ptr(" + ty_info.var_name + ");",
                            to_hu_conv_name = ty_info.var_name + "_hu_conv", from_hu_conv = (ty_info.var_name + ".conv_to_c()", ""))
                    if ty_info.rust_obj in tuple_types:
                        to_hu_conv_pfx = ""
                        to_hu_conv_sfx = ty_info.java_hu_ty + " " + ty_info.var_name + "_conv = new " + ty_info.java_hu_ty + "("
                        for idx, conv in enumerate(tuple_types[ty_info.rust_obj][0]):
                            if idx != 0:
                                to_hu_conv_sfx = to_hu_conv_sfx + ", "
                            conv.var_name = ty_info.var_name + "_" + chr(idx + ord("a"))
                            conv_map = map_type_with_info(conv, False, None, is_free, holds_ref)
                            to_hu_conv_pfx = to_hu_conv_pfx + conv.java_ty + " " + ty_info.var_name + "_" + chr(idx + ord("a")) + " = " + "bindings." + tuple_types[ty_info.rust_obj][1] + "_get_" + chr(idx + ord("a")) + "(" + ty_info.var_name + ");\n"
                            if conv_map.to_hu_conv is not None:
                                to_hu_conv_pfx = to_hu_conv_pfx + conv_map.to_hu_conv + ";\n"
                                to_hu_conv_sfx = to_hu_conv_sfx + conv_map.to_hu_conv_name;
                            else:
                                to_hu_conv_sfx = to_hu_conv_sfx + ty_info.var_name + "_" + chr(idx + ord("a"));
                        return ConvInfo(ty_info = ty_info, arg_name = ty_info.var_name,
                            arg_conv = base_conv, arg_conv_name = ty_info.var_name + "_conv", arg_conv_cleanup = None,
                            ret_conv = ("long " + ty_info.var_name + "_ref = (long)&", ";"), ret_conv_name = ty_info.var_name + "_ref",
                            to_hu_conv = to_hu_conv_pfx + to_hu_conv_sfx + ");", to_hu_conv_name = ty_info.var_name + "_conv", from_hu_conv = ("/*TODO b*/0", ""))

                    # The manually-defined types - TxOut and Transaction
                    return ConvInfo(ty_info = ty_info, arg_name = ty_info.var_name,
                        arg_conv = base_conv, arg_conv_name = ty_info.var_name + "_conv", arg_conv_cleanup = None,
                        ret_conv = ("long " + ty_info.var_name + "_ref = (long)&", ";"), ret_conv_name = ty_info.var_name + "_ref",
                        to_hu_conv = ty_info.java_hu_ty + " " + ty_info.var_name + "_conv = new " +ty_info.java_hu_ty + "(null, " + ty_info.var_name + ");",
                        to_hu_conv_name = ty_info.var_name + "_conv", from_hu_conv = ("/*TODO 1*/0", ""))
                else:
                    assert(not is_free)
                    if ty_info.rust_obj in opaque_structs:
                        return ConvInfo(ty_info = ty_info, arg_name = ty_info.var_name,
                            arg_conv = opaque_arg_conv, arg_conv_name = "&" + ty_info.var_name + "_conv", arg_conv_cleanup = None,
                            ret_conv = None, ret_conv_name = None, to_hu_conv = "TODO 2", to_hu_conv_name = None,
                            from_hu_conv = (ty_info.var_name + " == null ? 0 : " + ty_info.var_name + ".ptr & ~1", "this.ptrs_to.add(" + ty_info.var_name + ")")) # its a pointer, no conv needed
                    elif ty_info.rust_obj in trait_structs:
                        return ConvInfo(ty_info = ty_info, arg_name = ty_info.var_name,
                            arg_conv = ty_info.rust_obj + "* " + ty_info.var_name + "_conv = (" + ty_info.rust_obj + "*)" + ty_info.var_name + ";",
                            arg_conv_name = ty_info.var_name + "_conv", arg_conv_cleanup = None,
                            ret_conv = None, ret_conv_name = None, to_hu_conv = "TODO 2.5", to_hu_conv_name = None,
                            from_hu_conv = (ty_info.var_name + " == null ? 0 : " + ty_info.var_name + ".ptr", "this.ptrs_to.add(" + ty_info.var_name + ")")) # its a pointer, no conv needed
                    return ConvInfo(ty_info = ty_info, arg_name = ty_info.var_name,
                        arg_conv = ty_info.rust_obj + "* " + ty_info.var_name + "_conv = (" + ty_info.rust_obj + "*)" + ty_info.var_name + ";",
                        arg_conv_name = ty_info.var_name + "_conv", arg_conv_cleanup = None,
                        ret_conv = None, ret_conv_name = None, to_hu_conv = "TODO 3", to_hu_conv_name = None, from_hu_conv = None) # its a pointer, no conv needed
            elif ty_info.is_ptr:
                return ConvInfo(ty_info = ty_info, arg_name = ty_info.var_name,
                    arg_conv = None, arg_conv_name = ty_info.var_name, arg_conv_cleanup = None,
                    ret_conv = None, ret_conv_name = None, to_hu_conv = "TODO 4", to_hu_conv_name = None, from_hu_conv = None)
            else:
                return ConvInfo(ty_info = ty_info, arg_name = ty_info.var_name,
                    arg_conv = None, arg_conv_name = ty_info.var_name, arg_conv_cleanup = None,
                    ret_conv = None, ret_conv_name = None, to_hu_conv = None, to_hu_conv_name = None, from_hu_conv = None)
        elif not print_void:
            # We don't have a parameter name, and want one, just call it arg
            if ty_info.rust_obj is not None:
                assert(not is_free or ty_info.rust_obj not in opaque_structs)
                return ConvInfo(ty_info = ty_info, arg_name = ty_info.var_name,
                    arg_conv = ty_info.rust_obj + " arg_conv = *(" + ty_info.rust_obj + "*)arg;\nFREE((void*)arg);",
                    arg_conv_name = "arg_conv", arg_conv_cleanup = None,
                    ret_conv = None, ret_conv_name = None, to_hu_conv = "TODO 7", to_hu_conv_name = None, from_hu_conv = None)
            else:
                assert(not is_free)
                return ConvInfo(ty_info = ty_info, arg_name = ty_info.var_name,
                    arg_conv = None, arg_conv_name = "arg", arg_conv_cleanup = None,
                    ret_conv = None, ret_conv_name = None, to_hu_conv = "TODO 8", to_hu_conv_name = None, from_hu_conv = None)
        else:
            # We don't have a parameter name, and don't want one (cause we're returning)
            if ty_info.rust_obj is not None:
                if not ty_info.is_ptr:
                    if ty_info.rust_obj in unitary_enums:
                        return ConvInfo(ty_info = ty_info, arg_name = ty_info.var_name,
                            arg_conv = ty_info.rust_obj + " ret_conv = " + ty_info.rust_obj + "_from_java(_env, ret);",
                            arg_conv_name = "ret_conv", arg_conv_cleanup = None,
                            ret_conv = ("jclass ret = " + ty_info.rust_obj + "_to_java(_env, ", ");"), ret_conv_name = "ret",
                            to_hu_conv = None, to_hu_conv_name = None, from_hu_conv = None)
                    if ty_info.rust_obj in opaque_structs:
                        # If we're returning a newly-allocated struct, we don't want Rust to ever
                        # free, instead relying on the Java GC to lose the ref. We undo this in
                        # any _free function.
                        # To avoid any issues, we first assert that the incoming object is non-ref.
                        return ConvInfo(ty_info = ty_info, arg_name = ty_info.var_name,
                            ret_conv = (ty_info.rust_obj + " ret = ", ";"),
                            ret_conv_name = "((long)ret.inner) | (ret.is_owned ? 1 : 0)",
                            arg_conv = None, arg_conv_name = None, arg_conv_cleanup = None,
                            to_hu_conv = ty_info.java_hu_ty + " ret_hu_conv = new " + ty_info.java_hu_ty + "(null, ret);",
                            to_hu_conv_name = "ret_hu_conv", from_hu_conv = None)
                    elif ty_info.rust_obj in trait_structs:
                        return ConvInfo(ty_info = ty_info, arg_name = ty_info.var_name,
                            ret_conv = (ty_info.rust_obj + "* ret = MALLOC(sizeof(" + ty_info.rust_obj + "), \"" + ty_info.rust_obj + "\");\n*ret = ", ";"),
                            ret_conv_name = "(long)ret",
                            arg_conv = None, arg_conv_name = None, arg_conv_cleanup = None,
                            to_hu_conv = ty_info.java_hu_ty + " ret_hu_conv = new " + ty_info.java_hu_ty + "(null, ret);\nret_hu_conv.ptrs_to.add(this);",
                            to_hu_conv_name = "ret_hu_conv", from_hu_conv = None)
                    else:
                        return ConvInfo(ty_info = ty_info, arg_name = ty_info.var_name,
                            ret_conv = (ty_info.rust_obj + "* ret = MALLOC(sizeof(" + ty_info.rust_obj + "), \"" + ty_info.rust_obj + "\");\n*ret = ", ";"),
                            ret_conv_name = "(long)ret",
                            arg_conv = None, arg_conv_name = None, arg_conv_cleanup = None,
                            to_hu_conv = ty_info.java_hu_ty + " ret_hu_conv = new " + ty_info.java_hu_ty + "(null, ret);\nret_hu_conv.ptrs_to.add(this);",
                            to_hu_conv_name = "ret_hu_conv", from_hu_conv = None)
                elif ty_info.rust_obj in trait_structs:
                    return ConvInfo(ty_info = ty_info, arg_name = ty_info.var_name,
                        ret_conv = ("long ret = (long)", ";"), ret_conv_name = "ret",
                        arg_conv = None, arg_conv_name = None, arg_conv_cleanup = None,
                        to_hu_conv = ty_info.java_hu_ty + " ret_hu_conv = new " + ty_info.java_hu_ty + "(null, ret);\nret_hu_conv.ptrs_to.add(this);",
                        to_hu_conv_name = "ret_hu_conv", from_hu_conv = None)
                else:
                    return ConvInfo(ty_info = ty_info, arg_name = ty_info.var_name,
                        ret_conv = ("long ret = (long)", ";"), ret_conv_name = "ret",
                        arg_conv = None, arg_conv_name = None, arg_conv_cleanup = None,
                        to_hu_conv = "TODO c", to_hu_conv_name = None, from_hu_conv = None)
            else:
                return ConvInfo(ty_info = ty_info, arg_name = ty_info.var_name,
                    arg_conv = None, arg_conv_name = None, arg_conv_cleanup = None,
                    ret_conv = None, ret_conv_name = None,
                    to_hu_conv = None, to_hu_conv_name = None, from_hu_conv = None)

    def map_fn(line, re_match, ret_arr_len, c_call_string):
        out_java.write("\t// " + line)
        out_java.write("\tpublic static native ")
        out_c.write("JNIEXPORT ")

        is_free = re_match.group(2).endswith("_free")
        struct_meth = re_match.group(2).split("_")[0]

        ret_info = map_type(re_match.group(1), True, ret_arr_len, False, False)
        ret_info.print_ty()

        if ret_info.ret_conv is not None:
            ret_conv_pfx, ret_conv_sfx = ret_info.ret_conv

        out_java.write(" " + re_match.group(2) + "(")
        out_c.write(" JNICALL Java_org_ldk_impl_bindings_" + re_match.group(2).replace('_', '_1') + "(JNIEnv * _env, jclass _b")

        arg_names = []
        default_constructor_args = {}
        takes_self = False
        args_known = not ret_info.passed_as_ptr or ret_info.rust_obj in opaque_structs or ret_info.rust_obj in trait_structs
        for idx, arg in enumerate(re_match.group(3).split(',')):
            if idx != 0:
                out_java.write(", ")
            if arg != "void":
                out_c.write(", ")
            arg_conv_info = map_type(arg, False, None, is_free, False)
            if arg_conv_info.c_ty != "void":
                arg_conv_info.print_ty()
                arg_conv_info.print_name()
            if arg_conv_info.arg_name == "this_ptr" or arg_conv_info.arg_name == "this_arg":
                takes_self = True
            if arg_conv_info.passed_as_ptr and not arg_conv_info.rust_obj in opaque_structs:
                if not arg_conv_info.rust_obj in trait_structs and not arg_conv_info.rust_obj in unitary_enums:
                    args_known = False
            if arg_conv_info.arg_conv is not None and "Warning" in arg_conv_info.arg_conv:
                if arg_conv_info.rust_obj in constructor_fns:
                    assert not is_free
                    for explode_arg in constructor_fns[arg_conv_info.rust_obj].split(','):
                        explode_arg_conv = map_type(explode_arg, False, None, False, False)
                        if explode_arg_conv.c_ty == "void":
                            # We actually want to handle this case, but for now its only used in NetGraphMsgHandler::new()
                            # which ends up resulting in a redundant constructor - both without arguments for the NetworkGraph.
                            args_known = False
                        assert explode_arg_conv.arg_name != "this_ptr"
                        assert explode_arg_conv.arg_name != "this_arg"
                        if explode_arg_conv.passed_as_ptr and not explode_arg_conv.rust_obj in trait_structs:
                            args_known = False
                        if not arg_conv_info.arg_name in default_constructor_args:
                            default_constructor_args[arg_conv_info.arg_name] = []
                        default_constructor_args[arg_conv_info.arg_name].append(explode_arg_conv)
                else:
                    args_known = False
            arg_names.append(arg_conv_info)

        out_java_struct = None
        if ("LDK" + struct_meth in opaque_structs or "LDK" + struct_meth in trait_structs) and not is_free:
            out_java_struct = open(sys.argv[3] + "/structs/" + struct_meth + ".java", "a")
            if not args_known:
                out_java_struct.write("\t// Skipped " + re_match.group(2) + "\n")
                out_java_struct.close()
                out_java_struct = None
            else:
                meth_n = re_match.group(2)[len(struct_meth) + 1:]
                if ret_info.rust_obj == "LDK" + struct_meth:
                    out_java_struct.write("\tpublic static " + ret_info.java_hu_ty + " constructor_" + meth_n + "(")
                else:
                    out_java_struct.write("\tpublic " + ret_info.java_hu_ty + " " + meth_n + "(")
                for idx, arg in enumerate(arg_names):
                    if idx != 0:
                        if not takes_self or idx > 1:
                            out_java_struct.write(", ")
                    if arg.java_ty != "void" and arg.arg_name != "this_ptr" and arg.arg_name != "this_arg":
                        if arg.arg_name in default_constructor_args:
                            for explode_idx, explode_arg in enumerate(default_constructor_args[arg.arg_name]):
                                if explode_idx != 0:
                                    out_java_struct.write(", ")
                                assert explode_arg.rust_obj in opaque_structs or explode_arg.rust_obj in trait_structs
                                out_java_struct.write(explode_arg.java_hu_ty + " " + arg.arg_name + "_" + explode_arg.arg_name)
                        else:
                            out_java_struct.write(arg.java_hu_ty + " " + arg.arg_name)


        out_java.write(");\n")
        out_c.write(") {\n")
        if out_java_struct is not None:
            out_java_struct.write(") {\n")

        for info in arg_names:
            if info.arg_conv is not None:
                out_c.write("\t" + info.arg_conv.replace('\n', "\n\t") + "\n")

        if ret_info.ret_conv is not None:
            out_c.write("\t" + ret_conv_pfx.replace('\n', '\n\t'))
        elif ret_info.c_ty != "void":
            out_c.write("\t" + ret_info.c_ty + " ret_val = ")
        else:
            out_c.write("\t")

        if c_call_string is None:
            out_c.write(re_match.group(2) + "(")
        else:
            out_c.write(c_call_string)
        for idx, info in enumerate(arg_names):
            if info.arg_conv_name is not None:
                if idx != 0:
                    out_c.write(", ")
                elif c_call_string is not None:
                    continue
                out_c.write(info.arg_conv_name)
        out_c.write(")")
        if ret_info.ret_conv is not None:
            out_c.write(ret_conv_sfx.replace('\n', '\n\t'))
        else:
            out_c.write(";")
        for info in arg_names:
            if info.arg_conv_cleanup is not None:
                out_c.write("\n\t" + info.arg_conv_cleanup.replace("\n", "\n\t"))
        if ret_info.ret_conv is not None:
            out_c.write("\n\treturn " + ret_info.ret_conv_name + ";")
        elif ret_info.c_ty != "void":
            out_c.write("\n\treturn ret_val;")
        out_c.write("\n}\n\n")
        if out_java_struct is not None:
            out_java_struct.write("\t\t")
            if ret_info.java_ty != "void":
                out_java_struct.write(ret_info.java_ty + " ret = ")
            out_java_struct.write("bindings." + re_match.group(2) + "(")
            for idx, info in enumerate(arg_names):
                if idx != 0:
                    out_java_struct.write(", ")
                if info.arg_name == "this_ptr" or info.arg_name == "this_arg":
                    out_java_struct.write("this.ptr")
                elif info.arg_name in default_constructor_args:
                    out_java_struct.write("bindings." + info.java_hu_ty + "_new(")
                    for explode_idx, explode_arg in enumerate(default_constructor_args[info.arg_name]):
                        if explode_idx != 0:
                            out_java_struct.write(", ")
                        expl_arg_name = info.arg_name + "_" + explode_arg.arg_name
                        out_java_struct.write(explode_arg.from_hu_conv[0].replace(explode_arg.arg_name, expl_arg_name))
                    out_java_struct.write(")")
                elif info.from_hu_conv is not None:
                    out_java_struct.write(info.from_hu_conv[0])
                else:
                    out_java_struct.write(info.arg_name)
            out_java_struct.write(");\n")
            if ret_info.to_hu_conv is not None:
                out_java_struct.write("\t\t" + ret_info.to_hu_conv.replace("\n", "\n\t\t") + "\n")

            for info in arg_names:
                if info.arg_name == "this_ptr" or info.arg_name == "this_arg":
                    pass
                elif info.arg_name in default_constructor_args:
                    for explode_arg in default_constructor_args[info.arg_name]:
                        expl_arg_name = info.arg_name + "_" + explode_arg.arg_name
                        out_java_struct.write("\t\t" + explode_arg.from_hu_conv[1].replace(explode_arg.arg_name, expl_arg_name).replace("this", ret_info.to_hu_conv_name) + ";\n")
                elif info.from_hu_conv is not None and info.from_hu_conv[1] != "":
                    if ret_info.rust_obj == "LDK" + struct_meth and ret_info.to_hu_conv_name is not None:
                        out_java_struct.write("\t\t" + info.from_hu_conv[1].replace("this", ret_info.to_hu_conv_name) + ";\n")
                    else:
                        out_java_struct.write("\t\t" + info.from_hu_conv[1] + ";\n")

            if ret_info.to_hu_conv_name is not None:
                out_java_struct.write("\t\treturn " + ret_info.to_hu_conv_name + ";\n")
            elif ret_info.java_ty != "void" and ret_info.rust_obj != "LDK" + struct_meth:
                out_java_struct.write("\t\treturn ret;\n")
            out_java_struct.write("\t}\n\n")
            out_java_struct.close()

    def map_unitary_enum(struct_name, field_lines):
        with open(sys.argv[3] + "/enums/" + struct_name + ".java", "w") as out_java_enum:
            out_java_enum.write("package org.ldk.enums;\n\n")
            unitary_enums.add(struct_name)
            out_c.write("static inline " + struct_name + " " + struct_name + "_from_java(JNIEnv *env, jclass val) {\n")
            out_c.write("\tswitch ((*env)->CallIntMethod(env, val, ordinal_meth)) {\n")
            ord_v = 0
            for idx, struct_line in enumerate(field_lines):
                if idx == 0:
                    out_java_enum.write("public enum " + struct_name + " {\n")
                elif idx == len(field_lines) - 3:
                    assert(struct_line.endswith("_Sentinel,"))
                elif idx == len(field_lines) - 2:
                    out_java_enum.write("\t; static native void init();\n")
                    out_java_enum.write("\tstatic { init(); }\n")
                    out_java_enum.write("}")
                    out_java.write("\tstatic { " + struct_name + ".values(); /* Force enum statics to run */ }\n")
                elif idx == len(field_lines) - 1:
                    assert(struct_line == "")
                else:
                    out_java_enum.write(struct_line + "\n")
                    out_c.write("\t\tcase %d: return %s;\n" % (ord_v, struct_line.strip().strip(",")))
                    ord_v = ord_v + 1
            out_c.write("\t}\n")
            out_c.write("\tabort();\n")
            out_c.write("}\n")

            ord_v = 0
            out_c.write("static jclass " + struct_name + "_class = NULL;\n")
            for idx, struct_line in enumerate(field_lines):
                if idx > 0 and idx < len(field_lines) - 3:
                    variant = struct_line.strip().strip(",")
                    out_c.write("static jfieldID " + struct_name + "_" + variant + " = NULL;\n")
            out_c.write("JNIEXPORT void JNICALL Java_org_ldk_enums_" + struct_name.replace("_", "_1") + "_init (JNIEnv * env, jclass clz) {\n")
            out_c.write("\t" + struct_name + "_class = (*env)->NewGlobalRef(env, clz);\n")
            out_c.write("\tCHECK(" + struct_name + "_class != NULL);\n")
            for idx, struct_line in enumerate(field_lines):
                if idx > 0 and idx < len(field_lines) - 3:
                    variant = struct_line.strip().strip(",")
                    out_c.write("\t" + struct_name + "_" + variant + " = (*env)->GetStaticFieldID(env, " + struct_name + "_class, \"" + variant + "\", \"Lorg/ldk/enums/" + struct_name + ";\");\n")
                    out_c.write("\tCHECK(" + struct_name + "_" + variant + " != NULL);\n")
            out_c.write("}\n")
            out_c.write("static inline jclass " + struct_name + "_to_java(JNIEnv *env, " + struct_name + " val) {\n")
            out_c.write("\tswitch (val) {\n")
            for idx, struct_line in enumerate(field_lines):
                if idx > 0 and idx < len(field_lines) - 3:
                    variant = struct_line.strip().strip(",")
                    out_c.write("\t\tcase " + variant + ":\n")
                    out_c.write("\t\t\treturn (*env)->GetStaticObjectField(env, " + struct_name + "_class, " + struct_name + "_" + variant + ");\n")
                    ord_v = ord_v + 1
            out_c.write("\t\tdefault: abort();\n")
            out_c.write("\t}\n")
            out_c.write("}\n\n")

    def map_complex_enum(struct_name, union_enum_items):
        java_hu_type = struct_name.replace("LDK", "")
        complex_enums.add(struct_name)
        with open(sys.argv[3] + "/structs/" + java_hu_type + ".java", "w") as out_java_enum:
            out_java_enum.write(hu_struct_file_prefix)
            out_java_enum.write("public class " + java_hu_type + " extends CommonBase {\n")
            out_java_enum.write("\tprivate " + java_hu_type + "(Object _dummy, long ptr) { super(ptr); }\n")
            out_java_enum.write("\t@Override @SuppressWarnings(\"deprecation\")\n")
            out_java_enum.write("\tprotected void finalize() throws Throwable {\n")
            out_java_enum.write("\t\tsuper.finalize();\n")
            out_java_enum.write("\t\tbindings." + java_hu_type + "_free(ptr);\n")
            out_java_enum.write("\t}\n")
            out_java_enum.write("\tlong conv_to_c() { assert false; return 0; /* Should only be called on subclasses */ }\n")
            out_java_enum.write("\tstatic " + java_hu_type + " constr_from_ptr(long ptr) {\n")
            out_java_enum.write("\t\tbindings." + struct_name + " raw_val = bindings." + struct_name + "_ref_from_ptr(ptr);\n")
            java_hu_subclasses = ""

            tag_field_lines = union_enum_items["field_lines"]
            init_meth_jty_strs = {}
            for idx, struct_line in enumerate(tag_field_lines):
                if idx == 0:
                    out_java.write("\tpublic static class " + struct_name + " {\n")
                    out_java.write("\t\tprivate " + struct_name + "() {}\n")
                elif idx == len(tag_field_lines) - 3:
                    assert(struct_line.endswith("_Sentinel,"))
                elif idx == len(tag_field_lines) - 2:
                    out_java.write("\t\tstatic native void init();\n")
                    out_java.write("\t}\n")
                elif idx == len(tag_field_lines) - 1:
                    assert(struct_line == "")
                else:
                    var_name = struct_line.strip(' ,')[len(struct_name) + 1:]
                    out_java.write("\t\tpublic final static class " + var_name + " extends " + struct_name + " {\n")
                    java_hu_subclasses = java_hu_subclasses + "\tpublic final static class " + var_name + " extends " + java_hu_type + " {\n"
                    out_java_enum.write("\t\tif (raw_val.getClass() == bindings." + struct_name + "." + var_name + ".class) {\n")
                    out_java_enum.write("\t\t\treturn new " + var_name + "(ptr, (bindings." + struct_name + "." + var_name + ")raw_val);\n")
                    out_c.write("static jclass " + struct_name + "_" + var_name + "_class = NULL;\n")
                    out_c.write("static jmethodID " + struct_name + "_" + var_name + "_meth = NULL;\n")
                    init_meth_jty_str = ""
                    init_meth_params = ""
                    init_meth_body = ""
                    hu_conv_body = ""
                    if "LDK" + var_name in union_enum_items:
                        enum_var_lines = union_enum_items["LDK" + var_name]
                        for idx, field in enumerate(enum_var_lines):
                            if idx != 0 and idx < len(enum_var_lines) - 2:
                                field_ty = map_type(field.strip(' ;'), False, None, False, True)
                                out_java.write("\t\t\tpublic " + field_ty.java_ty + " " + field_ty.arg_name + ";\n")
                                java_hu_subclasses = java_hu_subclasses + "\t\tpublic " + field_ty.java_hu_ty + " " + field_ty.arg_name + ";\n"
                                if field_ty.to_hu_conv is not None:
                                    hu_conv_body = hu_conv_body + "\t\t\t" + field_ty.java_ty + " " + field_ty.arg_name + " = obj." + field_ty.arg_name + ";\n"
                                    hu_conv_body = hu_conv_body + "\t\t\t" + field_ty.to_hu_conv.replace("\n", "\n\t\t\t") + "\n"
                                    hu_conv_body = hu_conv_body + "\t\t\tthis." + field_ty.arg_name + " = " + field_ty.to_hu_conv_name + ";\n"
                                else:
                                    hu_conv_body = hu_conv_body + "\t\t\tthis." + field_ty.arg_name + " = obj." + field_ty.arg_name + ";\n"
                                init_meth_jty_str = init_meth_jty_str + field_ty.java_fn_ty_arg
                                if idx > 1:
                                    init_meth_params = init_meth_params + ", "
                                init_meth_params = init_meth_params + field_ty.java_ty + " " + field_ty.arg_name
                                init_meth_body = init_meth_body + "this." + field_ty.arg_name + " = " + field_ty.arg_name + "; "
                        out_java.write("\t\t\t" + var_name + "(" + init_meth_params + ") { ")
                        out_java.write(init_meth_body)
                        out_java.write("}\n")
                    out_java.write("\t\t}\n")
                    out_java_enum.write("\t\t}\n")
                    java_hu_subclasses = java_hu_subclasses + "\t\tprivate " + var_name + "(long ptr, bindings." + struct_name + "." + var_name + " obj) {\n\t\t\tsuper(null, ptr);\n"
                    java_hu_subclasses = java_hu_subclasses + hu_conv_body
                    java_hu_subclasses = java_hu_subclasses + "\t\t}\n\t\t@Override long conv_to_c() { return 0; /*XXX*/ }\n"
                    java_hu_subclasses = java_hu_subclasses + "\t}\n"
                    init_meth_jty_strs[var_name] = init_meth_jty_str
            out_java_enum.write("\t\tassert false; return null; // Unreachable without extending the (internal) bindings interface\n\t}\n\n")
            out_java_enum.write(java_hu_subclasses)
            out_java.write("\tstatic { " + struct_name + ".init(); }\n")
            out_java.write("\tpublic static native " + struct_name + " " + struct_name + "_ref_from_ptr(long ptr);\n");

            out_c.write("JNIEXPORT void JNICALL Java_org_ldk_impl_bindings_00024" + struct_name.replace("_", "_1") + "_init (JNIEnv * env, jclass _a) {\n")
            for idx, struct_line in enumerate(tag_field_lines):
                if idx != 0 and idx < len(tag_field_lines) - 3:
                    var_name = struct_line.strip(' ,')[len(struct_name) + 1:]
                    out_c.write("\t" + struct_name + "_" + var_name + "_class =\n")
                    out_c.write("\t\t(*env)->NewGlobalRef(env, (*env)->FindClass(env, \"Lorg/ldk/impl/bindings$" + struct_name + "$" + var_name + ";\"));\n")
                    out_c.write("\tCHECK(" + struct_name + "_" + var_name + "_class != NULL);\n")
                    out_c.write("\t" + struct_name + "_" + var_name + "_meth = (*env)->GetMethodID(env, " + struct_name + "_" + var_name + "_class, \"<init>\", \"(" + init_meth_jty_strs[var_name] + ")V\");\n")
                    out_c.write("\tCHECK(" + struct_name + "_" + var_name + "_meth != NULL);\n")
            out_c.write("}\n")
            out_c.write("JNIEXPORT jobject JNICALL Java_org_ldk_impl_bindings_" + struct_name.replace("_", "_1") + "_1ref_1from_1ptr (JNIEnv * _env, jclass _c, jlong ptr) {\n")
            out_c.write("\t" + struct_name + " *obj = (" + struct_name + "*)ptr;\n")
            out_c.write("\tswitch(obj->tag) {\n")
            for idx, struct_line in enumerate(tag_field_lines):
                if idx != 0 and idx < len(tag_field_lines) - 3:
                    var_name = struct_line.strip(' ,')[len(struct_name) + 1:]
                    out_c.write("\t\tcase " + struct_name + "_" + var_name + ": {\n")
                    c_params_text = ""
                    if "LDK" + var_name in union_enum_items:
                        enum_var_lines = union_enum_items["LDK" + var_name]
                        for idx, field in enumerate(enum_var_lines):
                            if idx != 0 and idx < len(enum_var_lines) - 2:
                                field_map = map_type(field.strip(' ;'), False, None, False, True)
                                if field_map.ret_conv is not None:
                                    out_c.write("\t\t\t" + field_map.ret_conv[0].replace("\n", "\n\t\t\t"))
                                    out_c.write("obj->" + camel_to_snake(var_name) + "." + field_map.arg_name)
                                    out_c.write(field_map.ret_conv[1].replace("\n", "\n\t\t\t") + "\n")
                                    c_params_text = c_params_text + ", " + field_map.ret_conv_name
                                else:
                                    c_params_text = c_params_text + ", obj->" + camel_to_snake(var_name) + "." + field_map.arg_name
                    out_c.write("\t\t\treturn (*_env)->NewObject(_env, " + struct_name + "_" + var_name + "_class, " + struct_name + "_" + var_name + "_meth" + c_params_text + ");\n")
                    out_c.write("\t\t}\n")
            out_c.write("\t\tdefault: abort();\n")
            out_c.write("\t}\n}\n")
            out_java_enum.write("}\n")

    def map_trait(struct_name, field_var_lines, trait_fn_lines):
        with open(sys.argv[3] + "/structs/" + struct_name.replace("LDK","") + ".java", "w") as out_java_trait:
            out_c.write("typedef struct " + struct_name + "_JCalls {\n")
            out_c.write("\tatomic_size_t refcnt;\n")
            out_c.write("\tJavaVM *vm;\n")
            out_c.write("\tjweak o;\n")
            for var_line in field_var_lines:
                if var_line.group(1) in trait_structs:
                    out_c.write("\t" + var_line.group(1) + "_JCalls* " + var_line.group(2) + ";\n")
            for fn_line in trait_fn_lines:
                if fn_line.group(2) != "free" and fn_line.group(2) != "clone":
                    out_c.write("\tjmethodID " + fn_line.group(2) + "_meth;\n")
            out_c.write("} " + struct_name + "_JCalls;\n")

            out_java_trait.write(hu_struct_file_prefix)
            out_java_trait.write("public class " + struct_name.replace("LDK","") + " extends CommonBase {\n")
            out_java_trait.write("\t" + struct_name.replace("LDK", "") + "(Object _dummy, long ptr) { super(ptr); }\n")
            out_java_trait.write("\tpublic " + struct_name.replace("LDK", "") + "(bindings." + struct_name + " arg") # XXX: Should be priv ( but is currently used in tests
            for var_line in field_var_lines:
                if var_line.group(1) in trait_structs:
                    out_java_trait.write(", bindings." + var_line.group(1) + " " + var_line.group(2))
            out_java_trait.write(") {\n")
            out_java_trait.write("\t\tsuper(bindings." + struct_name + "_new(arg")
            for var_line in field_var_lines:
                if var_line.group(1) in trait_structs:
                    out_java_trait.write(", " + var_line.group(2))
            out_java_trait.write("));\n")
            out_java_trait.write("\t\tthis.ptrs_to.add(arg);\n")
            out_java_trait.write("\t}\n")
            out_java_trait.write("\t@Override @SuppressWarnings(\"deprecation\")\n")
            out_java_trait.write("\tprotected void finalize() throws Throwable {\n")
            out_java_trait.write("\t\tbindings." + struct_name.replace("LDK","") + "_free(ptr); super.finalize();\n")
            out_java_trait.write("\t}\n\n")

            java_trait_constr = "\tpublic " + struct_name.replace("LDK", "") + "(" + struct_name.replace("LDK", "") + "Interface arg) {\n"
            java_trait_constr = java_trait_constr + "\t\tthis(new bindings." + struct_name + "() {\n"
            #out_java_trait.write("\tpublic static interface " + struct_name.replace("LDK", "") + "Interface {\n")
            out_java.write("\tpublic interface " + struct_name + " {\n")
            java_meths = []
            for fn_line in trait_fn_lines:
                java_meth_descr = "("
                if fn_line.group(2) != "free" and fn_line.group(2) != "clone":
                    ret_ty_info = map_type(fn_line.group(1), True, None, False, False)

                    out_java.write("\t\t " + ret_ty_info.java_ty + " " + fn_line.group(2) + "(")
                    java_trait_constr = java_trait_constr + "\t\t\t@Override public " + ret_ty_info.java_ty + " " + fn_line.group(2) + "("
                    #out_java_trait.write("\t\t" + ret_ty_info.java_hu_ty + " " + fn_line.group(2) + "(")
                    is_const = fn_line.group(3) is not None
                    out_c.write(fn_line.group(1) + fn_line.group(2) + "_jcall(")
                    if is_const:
                        out_c.write("const void* this_arg")
                    else:
                        out_c.write("void* this_arg")

                    arg_names = []
                    for idx, arg in enumerate(fn_line.group(4).split(',')):
                        if arg == "":
                            continue
                        if idx >= 2:
                            out_java.write(", ")
                            java_trait_constr = java_trait_constr + ", "
                            #out_java_trait.write(", ")
                        out_c.write(", ")
                        arg_conv_info = map_type(arg, True, None, False, False)
                        out_c.write(arg.strip())
                        out_java.write(arg_conv_info.java_ty + " " + arg_conv_info.arg_name)
                        #out_java_trait.write(arg_conv_info.java_ty + " " + arg_conv_info.arg_name)
                        java_trait_constr = java_trait_constr + arg_conv_info.java_ty + " " + arg_conv_info.arg_name
                        arg_names.append(arg_conv_info)
                        java_meth_descr = java_meth_descr + arg_conv_info.java_fn_ty_arg
                    java_meth_descr = java_meth_descr + ")" + ret_ty_info.java_fn_ty_arg
                    java_meths.append(java_meth_descr)

                    out_java.write(");\n")
                    #out_java_trait.write(");\n")
                    java_trait_constr = java_trait_constr + ") {\n"
                    out_c.write(") {\n")
                    out_c.write("\t" + struct_name + "_JCalls *j_calls = (" + struct_name + "_JCalls*) this_arg;\n")
                    out_c.write("\tJNIEnv *_env;\n")
                    out_c.write("\tDO_ASSERT((*j_calls->vm)->GetEnv(j_calls->vm, (void**)&_env, JNI_VERSION_1_8) == JNI_OK);\n")

                    for arg_info in arg_names:
                        if arg_info.ret_conv is not None:
                            out_c.write("\t" + arg_info.ret_conv[0].replace('\n', '\n\t'));
                            out_c.write(arg_info.arg_name)
                            out_c.write(arg_info.ret_conv[1].replace('\n', '\n\t') + "\n")

                    out_c.write("\tjobject obj = (*_env)->NewLocalRef(_env, j_calls->o);\n\tCHECK(obj != NULL);\n")
                    if ret_ty_info.c_ty.endswith("Array"):
                        out_c.write("\t" + ret_ty_info.c_ty + " ret = (*_env)->CallObjectMethod(_env, obj, j_calls->" + fn_line.group(2) + "_meth")
                    elif not ret_ty_info.passed_as_ptr:
                        out_c.write("\treturn (*_env)->Call" + ret_ty_info.java_ty.title() + "Method(_env, obj, j_calls->" + fn_line.group(2) + "_meth")
                    else:
                        out_c.write("\t" + fn_line.group(1).strip() + "* ret = (" + fn_line.group(1).strip() + "*)(*_env)->CallLongMethod(_env, obj, j_calls->" + fn_line.group(2) + "_meth");
                    if ret_ty_info.java_ty != "void":
                        java_trait_constr = java_trait_constr + "\t\t\t\treturn arg." + fn_line.group(2) + "("
                    else:
                        java_trait_constr = java_trait_constr + "\t\t\t\targ." + fn_line.group(2) + "("

                    for arg_info in arg_names:
                        if arg_info.ret_conv is not None:
                            out_c.write(", " + arg_info.ret_conv_name)
                        else:
                            out_c.write(", " + arg_info.arg_name)
                    out_c.write(");\n");
                    if ret_ty_info.arg_conv is not None:
                        out_c.write("\t" + ret_ty_info.arg_conv.replace("\n", "\n\t").replace("arg", "ret") + "\n\treturn " + ret_ty_info.arg_conv_name.replace("arg", "ret") + ";\n")

                    if ret_ty_info.passed_as_ptr:
                        out_c.write("\t" + fn_line.group(1).strip() + " res = *ret;\n")
                        out_c.write("\tFREE(ret);\n")
                        out_c.write("\treturn res;\n")
                    out_c.write("}\n")
                    java_trait_constr = java_trait_constr + ");\n\t\t\t}\n"
                elif fn_line.group(2) == "free":
                    out_c.write("static void " + struct_name + "_JCalls_free(void* this_arg) {\n")
                    out_c.write("\t" + struct_name + "_JCalls *j_calls = (" + struct_name + "_JCalls*) this_arg;\n")
                    out_c.write("\tif (atomic_fetch_sub_explicit(&j_calls->refcnt, 1, memory_order_acquire) == 1) {\n")
                    out_c.write("\t\tJNIEnv *env;\n")
                    out_c.write("\t\tDO_ASSERT((*j_calls->vm)->GetEnv(j_calls->vm, (void**)&env, JNI_VERSION_1_8) == JNI_OK);\n")
                    out_c.write("\t\t(*env)->DeleteWeakGlobalRef(env, j_calls->o);\n")
                    out_c.write("\t\tFREE(j_calls);\n")
                    out_c.write("\t}\n}\n")
            #out_java_trait.write("\t}\n")
            #out_java_trait.write(java_trait_constr + "\t\t});\n\t}\n")

            # Write out a clone function whether we need one or not, as we use them in moving to rust
            out_c.write("static void* " + struct_name + "_JCalls_clone(const void* this_arg) {\n")
            out_c.write("\t" + struct_name + "_JCalls *j_calls = (" + struct_name + "_JCalls*) this_arg;\n")
            out_c.write("\tatomic_fetch_add_explicit(&j_calls->refcnt, 1, memory_order_release);\n")
            for var_line in field_var_lines:
                if var_line.group(1) in trait_structs:
                    out_c.write("\tatomic_fetch_add_explicit(&j_calls->" + var_line.group(2) + "->refcnt, 1, memory_order_release);\n")
            out_c.write("\treturn (void*) this_arg;\n")
            out_c.write("}\n")

            out_java.write("\t}\n")

            out_java.write("\tpublic static native long " + struct_name + "_new(" + struct_name + " impl")
            out_c.write("static inline " + struct_name + " " + struct_name + "_init (JNIEnv * env, jclass _a, jobject o")
            for var_line in field_var_lines:
                if var_line.group(1) in trait_structs:
                    out_java.write(", " + var_line.group(1) + " " + var_line.group(2))
                    out_c.write(", jobject " + var_line.group(2))
            out_java.write(");\n")
            out_c.write(") {\n")

            out_c.write("\tjclass c = (*env)->GetObjectClass(env, o);\n")
            out_c.write("\tCHECK(c != NULL);\n")
            out_c.write("\t" + struct_name + "_JCalls *calls = MALLOC(sizeof(" + struct_name + "_JCalls), \"" + struct_name + "_JCalls\");\n")
            out_c.write("\tatomic_init(&calls->refcnt, 1);\n")
            out_c.write("\tDO_ASSERT((*env)->GetJavaVM(env, &calls->vm) == 0);\n")
            out_c.write("\tcalls->o = (*env)->NewWeakGlobalRef(env, o);\n")
            for (fn_line, java_meth_descr) in zip(trait_fn_lines, java_meths):
                if fn_line.group(2) != "free" and fn_line.group(2) != "clone":
                    out_c.write("\tcalls->" + fn_line.group(2) + "_meth = (*env)->GetMethodID(env, c, \"" + fn_line.group(2) + "\", \"" + java_meth_descr + "\");\n")
                    out_c.write("\tCHECK(calls->" + fn_line.group(2) + "_meth != NULL);\n")
            out_c.write("\n\t" + struct_name + " ret = {\n")
            out_c.write("\t\t.this_arg = (void*) calls,\n")
            for fn_line in trait_fn_lines:
                if fn_line.group(2) != "free" and fn_line.group(2) != "clone":
                    out_c.write("\t\t." + fn_line.group(2) + " = " + fn_line.group(2) + "_jcall,\n")
                elif fn_line.group(2) == "free":
                    out_c.write("\t\t.free = " + struct_name + "_JCalls_free,\n")
                else:
                    clone_fns.add(struct_name + "_clone")
                    out_c.write("\t\t.clone = " + struct_name + "_JCalls_clone,\n")
            for var_line in field_var_lines:
                if var_line.group(1) in trait_structs:
                    out_c.write("\t\t." + var_line.group(2) + " = " + var_line.group(1) + "_init(env, _a, " + var_line.group(2) + "),\n")
            out_c.write("\t};\n")
            for var_line in field_var_lines:
                if var_line.group(1) in trait_structs:
                    out_c.write("\tcalls->" + var_line.group(2) + " = ret." + var_line.group(2) + ".this_arg;\n")
            out_c.write("\treturn ret;\n")
            out_c.write("}\n")

            out_c.write("JNIEXPORT long JNICALL Java_org_ldk_impl_bindings_" + struct_name.replace("_", "_1") + "_1new (JNIEnv * env, jclass _a, jobject o")
            for var_line in field_var_lines:
                if var_line.group(1) in trait_structs:
                    out_c.write(", jobject " + var_line.group(2))
            out_c.write(") {\n")
            out_c.write("\t" + struct_name + " *res_ptr = MALLOC(sizeof(" + struct_name + "), \"" + struct_name + "\");\n")
            out_c.write("\t*res_ptr = " + struct_name + "_init(env, _a, o")
            for var_line in field_var_lines:
                if var_line.group(1) in trait_structs:
                    out_c.write(", " + var_line.group(2))
            out_c.write(");\n")
            out_c.write("\treturn (long)res_ptr;\n")
            out_c.write("}\n")

            out_java.write("\tpublic static native " + struct_name + " " + struct_name + "_get_obj_from_jcalls(long val);\n")
            out_c.write("JNIEXPORT jobject JNICALL Java_org_ldk_impl_bindings_" + struct_name.replace("_", "_1") + "_1get_1obj_1from_1jcalls (JNIEnv * env, jclass _a, jlong val) {\n")
            out_c.write("\tjobject ret = (*env)->NewLocalRef(env, ((" + struct_name + "_JCalls*)val)->o);\n")
            out_c.write("\tCHECK(ret != NULL);\n")
            out_c.write("\treturn ret;\n")
            out_c.write("}\n")

        for fn_line in trait_fn_lines:
            # For now, just disable enabling the _call_log - we don't know how to inverse-map String
            is_log = fn_line.group(2) == "log" and struct_name == "LDKLogger"
            if fn_line.group(2) != "free" and fn_line.group(2) != "clone" and fn_line.group(2) != "eq" and not is_log:
                dummy_line = fn_line.group(1) + struct_name.replace("LDK", "") + "_" + fn_line.group(2) + " " + struct_name + "* this_arg" + fn_line.group(4) + "\n"
                map_fn(dummy_line, re.compile("([A-Za-z_0-9]*) *([A-Za-z_0-9]*) *(.*)").match(dummy_line), None, "(this_arg_conv->" + fn_line.group(2) + ")(this_arg_conv->this_arg")

    out_c.write("""#include \"org_ldk_impl_bindings.h\"
#include <rust_types.h>
#include <lightning.h>
#include <string.h>
#include <stdatomic.h>
""")

    if sys.argv[4] == "false":
        out_c.write("#define MALLOC(a, _) malloc(a)\n")
        out_c.write("#define FREE(p) if ((p) > 1024) { free(p); }\n")
        out_c.write("#define DO_ASSERT(a) (void)(a)\n")
        out_c.write("#define CHECK(a)\n")
    else:
        out_c.write("""#include <assert.h>
// Always run a, then assert it is true:
#define DO_ASSERT(a) do { bool _assert_val = (a); assert(_assert_val); } while(0)
// Assert a is true or do nothing
#define CHECK(a) DO_ASSERT(a)

// Running a leak check across all the allocations and frees of the JDK is a mess,
// so instead we implement our own naive leak checker here, relying on the -wrap
// linker option to wrap malloc/calloc/realloc/free, tracking everyhing allocated
// and free'd in Rust or C across the generated bindings shared library.
#include <threads.h>
#include <execinfo.h>
#include <unistd.h>
static mtx_t allocation_mtx;

void __attribute__((constructor)) init_mtx() {
	DO_ASSERT(mtx_init(&allocation_mtx, mtx_plain) == thrd_success);
}

#define BT_MAX 128
typedef struct allocation {
	struct allocation* next;
	void* ptr;
	const char* struct_name;
	void* bt[BT_MAX];
	int bt_len;
} allocation;
static allocation* allocation_ll = NULL;

void* __real_malloc(size_t len);
void* __real_calloc(size_t nmemb, size_t len);
static void new_allocation(void* res, const char* struct_name) {
	allocation* new_alloc = __real_malloc(sizeof(allocation));
	new_alloc->ptr = res;
	new_alloc->struct_name = struct_name;
	new_alloc->bt_len = backtrace(new_alloc->bt, BT_MAX);
	DO_ASSERT(mtx_lock(&allocation_mtx) == thrd_success);
	new_alloc->next = allocation_ll;
	allocation_ll = new_alloc;
	DO_ASSERT(mtx_unlock(&allocation_mtx) == thrd_success);
}
static void* MALLOC(size_t len, const char* struct_name) {
	void* res = __real_malloc(len);
	new_allocation(res, struct_name);
	return res;
}
void __real_free(void* ptr);
static void alloc_freed(void* ptr) {
	allocation* p = NULL;
	DO_ASSERT(mtx_lock(&allocation_mtx) == thrd_success);
	allocation* it = allocation_ll;
	while (it->ptr != ptr) { p = it; it = it->next; }
	if (p) { p->next = it->next; } else { allocation_ll = it->next; }
	DO_ASSERT(mtx_unlock(&allocation_mtx) == thrd_success);
	DO_ASSERT(it->ptr == ptr);
	__real_free(it);
}
static void FREE(void* ptr) {
	if ((long)ptr < 1024) return; // Rust loves to create pointers to the NULL page for dummys
	alloc_freed(ptr);
	__real_free(ptr);
}

void* __wrap_malloc(size_t len) {
	void* res = __real_malloc(len);
	new_allocation(res, "malloc call");
	return res;
}
void* __wrap_calloc(size_t nmemb, size_t len) {
	void* res = __real_calloc(nmemb, len);
	new_allocation(res, "calloc call");
	return res;
}
void __wrap_free(void* ptr) {
	alloc_freed(ptr);
	__real_free(ptr);
}

void* __real_realloc(void* ptr, size_t newlen);
void* __wrap_realloc(void* ptr, size_t len) {
	alloc_freed(ptr);
	void* res = __real_realloc(ptr, len);
	new_allocation(res, "realloc call");
	return res;
}
void __wrap_reallocarray(void* ptr, size_t new_sz) {
	// Rust doesn't seem to use reallocarray currently
	assert(false);
}

void __attribute__((destructor)) check_leaks() {
	for (allocation* a = allocation_ll; a != NULL; a = a->next) {
		fprintf(stderr, "%s %p remains:\\n", a->struct_name, a->ptr);
		backtrace_symbols_fd(a->bt, a->bt_len, STDERR_FILENO);
		fprintf(stderr, "\\n\\n");
	}
	DO_ASSERT(allocation_ll == NULL);
}
""")
    out_java.write("""package org.ldk.impl;
import org.ldk.enums.*;

public class bindings {
	public static class VecOrSliceDef {
		public long dataptr;
		public long datalen;
		public long stride;
		public VecOrSliceDef(long dataptr, long datalen, long stride) {
			this.dataptr = dataptr; this.datalen = datalen; this.stride = stride;
		}
	}
	static {
		System.loadLibrary(\"lightningjni\");
		init(java.lang.Enum.class, VecOrSliceDef.class);
	}
	static native void init(java.lang.Class c, java.lang.Class slicedef);

	public static native boolean deref_bool(long ptr);
	public static native long deref_long(long ptr);
	public static native void free_heap_ptr(long ptr);
	public static native byte[] read_bytes(long ptr, long len);
	public static native byte[] get_u8_slice_bytes(long slice_ptr);
	public static native long bytes_to_u8_vec(byte[] bytes);
	public static native long new_txpointer_copy_data(byte[] txdata);
	public static native long vec_slice_len(long vec);
	public static native long new_empty_slice_vec();

""")
    out_c.write("""
static jmethodID ordinal_meth = NULL;
static jmethodID slicedef_meth = NULL;
static jclass slicedef_cls = NULL;
JNIEXPORT void Java_org_ldk_impl_bindings_init(JNIEnv * env, jclass _b, jclass enum_class, jclass slicedef_class) {
	ordinal_meth = (*env)->GetMethodID(env, enum_class, "ordinal", "()I");
	CHECK(ordinal_meth != NULL);
	slicedef_meth = (*env)->GetMethodID(env, slicedef_class, "<init>", "(JJJ)V");
	CHECK(slicedef_meth != NULL);
	slicedef_cls = (*env)->NewGlobalRef(env, slicedef_class);
	CHECK(slicedef_cls != NULL);
}

JNIEXPORT jboolean JNICALL Java_org_ldk_impl_bindings_deref_1bool (JNIEnv * env, jclass _a, jlong ptr) {
	return *((bool*)ptr);
}
JNIEXPORT jlong JNICALL Java_org_ldk_impl_bindings_deref_1long (JNIEnv * env, jclass _a, jlong ptr) {
	return *((long*)ptr);
}
JNIEXPORT void JNICALL Java_org_ldk_impl_bindings_free_1heap_1ptr (JNIEnv * env, jclass _a, jlong ptr) {
	FREE((void*)ptr);
}
JNIEXPORT jbyteArray JNICALL Java_org_ldk_impl_bindings_read_1bytes (JNIEnv * _env, jclass _b, jlong ptr, jlong len) {
	jbyteArray ret_arr = (*_env)->NewByteArray(_env, len);
	(*_env)->SetByteArrayRegion(_env, ret_arr, 0, len, (unsigned char*)ptr);
	return ret_arr;
}
JNIEXPORT jbyteArray JNICALL Java_org_ldk_impl_bindings_get_1u8_1slice_1bytes (JNIEnv * _env, jclass _b, jlong slice_ptr) {
	LDKu8slice *slice = (LDKu8slice*)slice_ptr;
	jbyteArray ret_arr = (*_env)->NewByteArray(_env, slice->datalen);
	(*_env)->SetByteArrayRegion(_env, ret_arr, 0, slice->datalen, slice->data);
	return ret_arr;
}
JNIEXPORT long JNICALL Java_org_ldk_impl_bindings_bytes_1to_1u8_1vec (JNIEnv * _env, jclass _b, jbyteArray bytes) {
	LDKCVec_u8Z *vec = (LDKCVec_u8Z*)MALLOC(sizeof(LDKCVec_u8Z), "LDKCVec_u8");
	vec->datalen = (*_env)->GetArrayLength(_env, bytes);
	vec->data = (uint8_t*)MALLOC(vec->datalen, "LDKCVec_u8Z Bytes");
	(*_env)->GetByteArrayRegion (_env, bytes, 0, vec->datalen, vec->data);
	return (long)vec;
}
JNIEXPORT long JNICALL Java_org_ldk_impl_bindings_new_1txpointer_1copy_1data (JNIEnv * env, jclass _b, jbyteArray bytes) {
	LDKTransaction *txdata = (LDKTransaction*)MALLOC(sizeof(LDKTransaction), "LDKTransaction");
	txdata->datalen = (*env)->GetArrayLength(env, bytes);
	txdata->data = (uint8_t*)MALLOC(txdata->datalen, "Tx Data Bytes");
	txdata->data_is_owned = true;
	(*env)->GetByteArrayRegion (env, bytes, 0, txdata->datalen, txdata->data);
	return (long)txdata;
}
JNIEXPORT jlong JNICALL Java_org_ldk_impl_bindings_vec_1slice_1len (JNIEnv * env, jclass _a, jlong ptr) {
        // Check offsets of a few Vec types are all consistent as we're meant to be generic across types
	_Static_assert(offsetof(LDKCVec_u8Z, datalen) == offsetof(LDKCVec_SignatureZ, datalen), "Vec<*> needs to be mapped identically");
	_Static_assert(offsetof(LDKCVec_u8Z, datalen) == offsetof(LDKCVec_MessageSendEventZ, datalen), "Vec<*> needs to be mapped identically");
	_Static_assert(offsetof(LDKCVec_u8Z, datalen) == offsetof(LDKCVec_EventZ, datalen), "Vec<*> needs to be mapped identically");
	_Static_assert(offsetof(LDKCVec_u8Z, datalen) == offsetof(LDKCVec_C2Tuple_usizeTransactionZZ, datalen), "Vec<*> needs to be mapped identically");
	LDKCVec_u8Z *vec = (LDKCVec_u8Z*)ptr;
	return (long)vec->datalen;
}
JNIEXPORT long JNICALL Java_org_ldk_impl_bindings_new_1empty_1slice_1vec (JNIEnv * _env, jclass _b) {
        // Check sizes of a few Vec types are all consistent as we're meant to be generic across types
	_Static_assert(sizeof(LDKCVec_u8Z) == sizeof(LDKCVec_SignatureZ), "Vec<*> needs to be mapped identically");
	_Static_assert(sizeof(LDKCVec_u8Z) == sizeof(LDKCVec_MessageSendEventZ), "Vec<*> needs to be mapped identically");
	_Static_assert(sizeof(LDKCVec_u8Z) == sizeof(LDKCVec_EventZ), "Vec<*> needs to be mapped identically");
	_Static_assert(sizeof(LDKCVec_u8Z) == sizeof(LDKCVec_C2Tuple_usizeTransactionZZ), "Vec<*> needs to be mapped identically");
	LDKCVec_u8Z *vec = (LDKCVec_u8Z*)MALLOC(sizeof(LDKCVec_u8Z), "Empty LDKCVec");
	vec->data = NULL;
	vec->datalen = 0;
	return (long)vec;
}

// We assume that CVec_u8Z and u8slice are the same size and layout (and thus pointers to the two can be mixed)
_Static_assert(sizeof(LDKCVec_u8Z) == sizeof(LDKu8slice), "Vec<u8> and [u8] need to have been mapped identically");
_Static_assert(offsetof(LDKCVec_u8Z, data) == offsetof(LDKu8slice, data), "Vec<u8> and [u8] need to have been mapped identically");
_Static_assert(offsetof(LDKCVec_u8Z, datalen) == offsetof(LDKu8slice, datalen), "Vec<u8> and [u8] need to have been mapped identically");

""")

    with open(sys.argv[3] + "/structs/CommonBase.java", "a") as out_java_struct:
        out_java_struct.write("""package org.ldk.structs;
import java.util.LinkedList;
class CommonBase {
	final long ptr;
	LinkedList<Object> ptrs_to = new LinkedList();
	protected CommonBase(long ptr) { this.ptr = ptr; }
	public long _test_only_get_ptr() { return this.ptr; }
}
""")

    in_block_comment = False
    cur_block_obj = None

    const_val_regex = re.compile("^extern const ([A-Za-z_0-9]*) ([A-Za-z_0-9]*);$")

    line_indicates_result_regex = re.compile("^   (LDKCResultPtr_[A-Za-z_0-9]*) contents;$")
    line_indicates_vec_regex = re.compile("^   ([A-Za-z_0-9]*) \*data;$")
    line_indicates_opaque_regex = re.compile("^   bool is_owned;$")
    line_indicates_trait_regex = re.compile("^   ([A-Za-z_0-9]* \*?)\(\*([A-Za-z_0-9]*)\)\((const )?void \*this_arg(.*)\);$")
    assert(line_indicates_trait_regex.match("   uintptr_t (*send_data)(void *this_arg, LDKu8slice data, bool resume_read);"))
    assert(line_indicates_trait_regex.match("   LDKCVec_MessageSendEventZ (*get_and_clear_pending_msg_events)(const void *this_arg);"))
    assert(line_indicates_trait_regex.match("   void *(*clone)(const void *this_arg);"))
    line_field_var_regex = re.compile("^   ([A-Za-z_0-9]*) ([A-Za-z_0-9]*);$")
    assert(line_field_var_regex.match("   LDKMessageSendEventsProvider MessageSendEventsProvider;"))
    struct_name_regex = re.compile("^typedef (struct|enum|union) (MUST_USE_STRUCT )?(LDK[A-Za-z_0-9]*) {$")
    assert(struct_name_regex.match("typedef struct LDKCVecTempl_u8 {"))
    assert(struct_name_regex.match("typedef enum LDKNetwork {"))
    struct_alias_regex = re.compile("^typedef (LDK[A-Za-z_0-9]*) (LDK[A-Za-z_0-9]*);$")
    assert(struct_alias_regex.match("typedef LDKCResultTempl_bool__PeerHandleError LDKCResult_boolPeerHandleErrorZ;"))

    result_templ_structs = set()
    union_enum_items = {}
    result_ptr_struct_items = {}
    for line in in_h:
        if in_block_comment:
            if line.endswith("*/\n"):
                in_block_comment = False
        elif cur_block_obj is not None:
            cur_block_obj  = cur_block_obj + line
            if line.startswith("} "):
                field_lines = []
                struct_name = None
                vec_ty = None
                obj_lines = cur_block_obj.split("\n")
                is_opaque = False
                result_contents = None
                is_unitary_enum = False
                is_union_enum = False
                is_union = False
                is_tuple = False
                trait_fn_lines = []
                field_var_lines = []

                for idx, struct_line in enumerate(obj_lines):
                    if struct_line.strip().startswith("/*"):
                        in_block_comment = True
                    if in_block_comment:
                        if struct_line.endswith("*/"):
                            in_block_comment = False
                    else:
                        struct_name_match = struct_name_regex.match(struct_line)
                        if struct_name_match is not None:
                            struct_name = struct_name_match.group(3)
                            if struct_name_match.group(1) == "enum":
                                if not struct_name.endswith("_Tag"):
                                    is_unitary_enum = True
                                else:
                                    is_union_enum = True
                            elif struct_name_match.group(1) == "union":
                                is_union = True
                        if line_indicates_opaque_regex.match(struct_line):
                            is_opaque = True
                        result_match = line_indicates_result_regex.match(struct_line)
                        if result_match is not None:
                            result_contents = result_match.group(1)
                        vec_ty_match = line_indicates_vec_regex.match(struct_line)
                        if vec_ty_match is not None and struct_name.startswith("LDKCVecTempl_"):
                            vec_ty = vec_ty_match.group(1)
                        elif struct_name.startswith("LDKC2TupleTempl_") or struct_name.startswith("LDKC3TupleTempl_"):
                            is_tuple = True
                        trait_fn_match = line_indicates_trait_regex.match(struct_line)
                        if trait_fn_match is not None:
                            trait_fn_lines.append(trait_fn_match)
                        field_var_match = line_field_var_regex.match(struct_line)
                        if field_var_match is not None:
                            field_var_lines.append(field_var_match)
                        field_lines.append(struct_line)

                assert(struct_name is not None)
                assert(len(trait_fn_lines) == 0 or not (is_opaque or is_unitary_enum or is_union_enum or is_union or result_contents is not None or vec_ty is not None))
                assert(not is_opaque or not (len(trait_fn_lines) != 0 or is_unitary_enum or is_union_enum or is_union or result_contents is not None or vec_ty is not None))
                assert(not is_unitary_enum or not (len(trait_fn_lines) != 0 or is_opaque or is_union_enum or is_union or result_contents is not None or vec_ty is not None))
                assert(not is_union_enum or not (len(trait_fn_lines) != 0 or is_unitary_enum or is_opaque or is_union or result_contents is not None or vec_ty is not None))
                assert(not is_union or not (len(trait_fn_lines) != 0 or is_unitary_enum or is_union_enum or is_opaque or result_contents is not None or vec_ty is not None))
                assert(result_contents is None or not (len(trait_fn_lines) != 0 or is_unitary_enum or is_union_enum or is_opaque or is_union or vec_ty is not None))
                assert(vec_ty is None or not (len(trait_fn_lines) != 0 or is_unitary_enum or is_union_enum or is_opaque or is_union or result_contents is not None))

                if is_opaque:
                    opaque_structs.add(struct_name)
                    with open(sys.argv[3] + "/structs/" + struct_name.replace("LDK","") + ".java", "w") as out_java_struct:
                        out_java_struct.write(hu_struct_file_prefix)
                        out_java_struct.write("public class " + struct_name.replace("LDK","") + " extends CommonBase")
                        if struct_name.startswith("LDKLocked"):
                            out_java_struct.write(" implements AutoCloseable")
                        out_java_struct.write(" {\n")
                        out_java_struct.write("\t" + struct_name.replace("LDK", "") + "(Object _dummy, long ptr) { super(ptr); }\n")
                        if struct_name.startswith("LDKLocked"):
                            out_java_struct.write("\t@Override public void close() {\n")
                        else:
                            out_java_struct.write("\t@Override @SuppressWarnings(\"deprecation\")\n")
                            out_java_struct.write("\tprotected void finalize() throws Throwable {\n")
                            out_java_struct.write("\t\tsuper.finalize();\n")
                        out_java_struct.write("\t\tbindings." + struct_name.replace("LDK","") + "_free(ptr);\n")
                        out_java_struct.write("\t}\n\n")
                elif result_contents is not None:
                    result_templ_structs.add(struct_name)
                    assert result_contents in result_ptr_struct_items
                elif struct_name.startswith("LDKCResultPtr_"):
                    for line in field_lines:
                        if line.endswith("*result;"):
                            res_ty = line[:-8].strip()
                        elif line.endswith("*err;"):
                            err_ty = line[:-5].strip()
                    result_ptr_struct_items[struct_name] = (res_ty, err_ty)
                elif is_tuple:
                    out_java.write("\tpublic static native long " + struct_name + "_new(")
                    out_c.write("JNIEXPORT jlong JNICALL Java_org_ldk_impl_bindings_" + struct_name.replace("_", "_1") + "_1new(JNIEnv *_env, jclass _b")
                    ty_list = []
                    for idx, line in enumerate(field_lines):
                        if idx != 0 and idx < len(field_lines) - 2:
                            ty_info = java_c_types(line.strip(';'), None)
                            if idx != 1:
                                out_java.write(", ")
                            e = chr(ord('a') + idx - 1)
                            out_java.write(ty_info.java_ty + " " + e)
                            out_c.write(", " + ty_info.c_ty + " " + e)
                            ty_list.append(ty_info)
                    tuple_types[struct_name] = (ty_list, struct_name)
                    out_java.write(");\n")
                    out_c.write(") {\n")
                    out_c.write("\t" + struct_name + "* ret = MALLOC(sizeof(" + struct_name + "), \"" + struct_name + "\");\n")
                    for idx, line in enumerate(field_lines):
                        if idx != 0 and idx < len(field_lines) - 2:
                            ty_info = map_type(line.strip(';'), False, None, False, False)
                            e = chr(ord('a') + idx - 1)
                            if ty_info.arg_conv is not None:
                                out_c.write("\t" + ty_info.arg_conv.replace("\n", "\n\t"))
                                out_c.write("\n\tret->" + e + " = " + ty_info.arg_conv_name + ";\n")
                            else:
                                out_c.write("\tret->" + e + " = " + e + ";\n")
                            if ty_info.arg_conv_cleanup is not None:
                                out_c.write("\t//TODO: Really need to call " + ty_info.arg_conv_cleanup + " here\n")
                    out_c.write("\treturn (long)ret;\n")
                    out_c.write("}\n")
                elif vec_ty is not None:
                    if vec_ty in opaque_structs:
                        out_java.write("\tpublic static native long[] " + struct_name + "_arr_info(long vec_ptr);\n")
                        out_c.write("JNIEXPORT jlongArray JNICALL Java_org_ldk_impl_bindings_" + struct_name.replace("_", "_1") + "_1arr_1info(JNIEnv *env, jclass _b, jlong ptr) {\n")
                    else:
                        out_java.write("\tpublic static native VecOrSliceDef " + struct_name + "_arr_info(long vec_ptr);\n")
                        out_c.write("JNIEXPORT jobject JNICALL Java_org_ldk_impl_bindings_" + struct_name.replace("_", "_1") + "_1arr_1info(JNIEnv *env, jclass _b, jlong ptr) {\n")
                    out_c.write("\t" + struct_name + " *vec = (" + struct_name + "*)ptr;\n")
                    if vec_ty in opaque_structs:
                        out_c.write("\tjlongArray ret = (*env)->NewLongArray(env, vec->datalen);\n")
                        out_c.write("\tjlong *ret_elems = (*env)->GetPrimitiveArrayCritical(env, ret, NULL);\n")
                        out_c.write("\tfor (size_t i = 0; i < vec->datalen; i++) {\n")
                        out_c.write("\t\tCHECK((((long)vec->data[i].inner) & 1) == 0);\n")
                        out_c.write("\t\tret_elems[i] = (long)vec->data[i].inner | (vec->data[i].is_owned ? 1 : 0);\n")
                        out_c.write("\t}\n")
                        out_c.write("\t(*env)->ReleasePrimitiveArrayCritical(env, ret, ret_elems, 0);\n")
                        out_c.write("\treturn ret;\n")
                    else:
                        out_c.write("\treturn (*env)->NewObject(env, slicedef_cls, slicedef_meth, (long)vec->data, (long)vec->datalen, sizeof(" + vec_ty + "));\n")
                    out_c.write("}\n")

                    ty_info = map_type(vec_ty + " arr_elem", False, None, False, False)
                    if len(ty_info.java_fn_ty_arg) == 1: # ie we're a primitive of some form
                        out_java.write("\tpublic static native long " + struct_name + "_new(" + ty_info.java_ty + "[] elems);\n")
                        out_c.write("JNIEXPORT jlong JNICALL Java_org_ldk_impl_bindings_" + struct_name.replace("_", "_1") + "_1new(JNIEnv *env, jclass _b, j" + ty_info.java_ty + "Array elems){\n")
                        out_c.write("\t" + struct_name + " *ret = MALLOC(sizeof(" + struct_name + "), \"" + struct_name + "\");\n")
                        out_c.write("\tret->datalen = (*env)->GetArrayLength(env, elems);\n")
                        out_c.write("\tif (ret->datalen == 0) {\n")
                        out_c.write("\t\tret->data = NULL;\n")
                        out_c.write("\t} else {\n")
                        out_c.write("\t\tret->data = MALLOC(sizeof(" + vec_ty + ") * ret->datalen, \"" + struct_name + " Data\");\n")
                        out_c.write("\t\t" + ty_info.c_ty + " *java_elems = (*env)->GetPrimitiveArrayCritical(env, elems, NULL);\n")
                        out_c.write("\t\tfor (size_t i = 0; i < ret->datalen; i++) {\n")
                        if ty_info.arg_conv is not None:
                            out_c.write("\t\t\t" + ty_info.c_ty + " arr_elem = java_elems[i];\n")
                            out_c.write("\t\t\t" + ty_info.arg_conv.replace("\n", "\n\t\t\t") + "\n")
                            out_c.write("\t\t\tret->data[i] = " + ty_info.arg_conv_name + ";\n")
                            assert ty_info.arg_conv_cleanup is None
                        else:
                            out_c.write("\t\t\tret->data[i] = java_elems[i];\n")
                        out_c.write("\t\t}\n")
                        out_c.write("\t\t(*env)->ReleasePrimitiveArrayCritical(env, elems, java_elems, 0);\n")
                        out_c.write("\t}\n")
                        out_c.write("\treturn (long)ret;\n")
                        out_c.write("}\n")
                elif is_union_enum:
                    assert(struct_name.endswith("_Tag"))
                    struct_name = struct_name[:-4]
                    union_enum_items[struct_name] = {"field_lines": field_lines}
                elif struct_name.endswith("_Body") and struct_name.split("_")[0] in union_enum_items:
                    enum_var_name = struct_name.split("_")
                    union_enum_items[enum_var_name[0]][enum_var_name[1]] = field_lines
                elif struct_name in union_enum_items:
                    map_complex_enum(struct_name, union_enum_items[struct_name])
                elif is_unitary_enum:
                    map_unitary_enum(struct_name, field_lines)
                elif len(trait_fn_lines) > 0:
                    trait_structs.add(struct_name)
                    map_trait(struct_name, field_var_lines, trait_fn_lines)
                elif struct_name == "LDKTxOut":
                    with open(sys.argv[3] + "/structs/TxOut.java", "w") as out_java_struct:
                        out_java_struct.write(hu_struct_file_prefix)
                        out_java_struct.write("public class TxOut extends CommonBase{\n")
                        out_java_struct.write("\tTxOut(java.lang.Object _dummy, long ptr) { super(ptr); }\n")
                        # TODO: TxOut body
                        out_java_struct.write("}")
                elif struct_name == "LDKTransaction":
                    with open(sys.argv[3] + "/structs/Transaction.java", "w") as out_java_struct:
                        out_java_struct.write(hu_struct_file_prefix)
                        out_java_struct.write("public class Transaction extends CommonBase{\n")
                        out_java_struct.write("\tTransaction(java.lang.Object _dummy, long ptr) { super(ptr); }\n")
                        # TODO: Transaction body
                        out_java_struct.write("}")
                else:
                    pass # Everything remaining is a byte[] or some form
                cur_block_obj = None
        else:
            fn_ptr = fn_ptr_regex.match(line)
            fn_ret_arr = fn_ret_arr_regex.match(line)
            reg_fn = reg_fn_regex.match(line)
            const_val = const_val_regex.match(line)

            if line.startswith("#include <"):
                pass
            elif line.startswith("/*"):
                #out_java.write("\t" + line)
                if not line.endswith("*/\n"):
                    in_block_comment = True
            elif line.startswith("typedef enum "):
                cur_block_obj = line
            elif line.startswith("typedef struct "):
                cur_block_obj = line
            elif line.startswith("typedef union "):
                cur_block_obj = line
            elif line.startswith("typedef "):
                alias_match =  struct_alias_regex.match(line)
                if alias_match.group(1) in tuple_types:
                    tuple_types[alias_match.group(2)] = (tuple_types[alias_match.group(1)][0], alias_match.group(2))
                    tuple_types[alias_match.group(1)] = (tuple_types[alias_match.group(1)][0], alias_match.group(2))
                    for idx, ty_info in enumerate(tuple_types[alias_match.group(1)][0]):
                        e = chr(ord('a') + idx)
                        out_java.write("\tpublic static native " + ty_info.java_ty + " " + alias_match.group(2) + "_get_" + e + "(long ptr);\n")
                        # XXX: Write C method!
                elif alias_match.group(1) in result_templ_structs:
                    human_ty = alias_match.group(2).replace("LDKCResult", "Result_").replace("__", "_").replace("Templ", "")
                    with open(sys.argv[3] + "/structs/" + human_ty + ".java", "w") as out_java_struct:
                        out_java_struct.write(hu_struct_file_prefix)
                        out_java_struct.write("public class " + human_ty + " extends CommonBase {\n")
                        out_java_struct.write("\tprivate " + human_ty + "(Object _dummy, long ptr) { super(ptr); }\n")
                        out_java_struct.write("\tprotected void finalize() throws Throwable {\n")
                        out_java_struct.write("\t\tbindings." + alias_match.group(2).replace("LDK","") + "_free(ptr); super.finalize();\n")
                        out_java_struct.write("\t}\n\n")

                        contents_ty = alias_match.group(1).replace("LDKCResultTempl", "LDKCResultPtr")
                        res_ty, err_ty = result_ptr_struct_items[contents_ty]
                        res_map = map_type(res_ty + " res", True, None, False, True)
                        err_map = map_type(err_ty + " err", True, None, False, True)

                        out_java.write("\tpublic static native boolean " + alias_match.group(2) + "_result_ok(long arg);\n")
                        out_c.write("JNIEXPORT jboolean JNICALL Java_org_ldk_impl_bindings_" + alias_match.group(2).replace("_", "_1") + "_1result_1ok (JNIEnv * env, jclass _a, jlong arg) {\n")
                        out_c.write("\treturn ((" + alias_match.group(2) + "*)arg)->result_ok;\n")
                        out_c.write("}\n")

                        out_java.write("\tpublic static native " + res_map.java_ty + " " + alias_match.group(2) + "_get_ok(long arg);\n")
                        out_c.write("JNIEXPORT " + res_map.c_ty + " JNICALL Java_org_ldk_impl_bindings_" + alias_match.group(2).replace("_", "_1") + "_1get_1ok (JNIEnv * _env, jclass _a, jlong arg) {\n")
                        out_c.write("\t" + alias_match.group(2) + " *val = (" + alias_match.group(2) + "*)arg;\n")
                        out_c.write("\tCHECK(val->result_ok);\n\t")
                        out_java_struct.write("\tpublic static final class " + human_ty + "_OK extends " + human_ty + " {\n")
                        if res_map.ret_conv is not None:
                            out_c.write(res_map.ret_conv[0].replace("\n", "\n\t") + "(*val->contents.result)")
                            out_c.write(res_map.ret_conv[1].replace("\n", "\n\t") + "\n\treturn " + res_map.ret_conv_name)
                        else:
                            out_c.write("return *val->contents.result")
                        out_c.write(";\n}\n")

                        out_java_struct.write("\t\tpublic " + res_map.java_hu_ty + " res;\n")
                        out_java_struct.write("\t\tprivate " + human_ty + "_OK(Object _dummy, long ptr) {\n")
                        out_java_struct.write("\t\t\tsuper(_dummy, ptr);\n")
                        if res_map.to_hu_conv is not None:
                            out_java_struct.write("\t\t\t" + res_map.java_ty + " res = bindings." + alias_match.group(2) + "_get_ok(ptr);\n")
                            out_java_struct.write("\t\t\t" + res_map.to_hu_conv.replace("\n", "\n\t\t\t"))
                            out_java_struct.write("\n\t\t\tthis.res = " + res_map.to_hu_conv_name + ";\n")
                        else:
                            out_java_struct.write("\t\t\tthis.res = bindings." + alias_match.group(2) + "_get_ok(ptr);\n")
                        out_java_struct.write("\t\t}\n\n")

                        out_java.write("\tpublic static native " + err_map.java_ty + " " + alias_match.group(2) + "_get_err(long arg);\n")
                        out_c.write("JNIEXPORT " + err_map.c_ty + " JNICALL Java_org_ldk_impl_bindings_" + alias_match.group(2).replace("_", "_1") + "_1get_1err (JNIEnv * _env, jclass _a, jlong arg) {\n")
                        out_c.write("\t" + alias_match.group(2) + " *val = (" + alias_match.group(2) + "*)arg;\n")
                        out_c.write("\tCHECK(!val->result_ok);\n\t")
                        out_java_struct.write("\t}\n\tpublic static final class " + human_ty + "_Err extends " + human_ty + " {\n")
                        if err_map.ret_conv is not None:
                            out_c.write(err_map.ret_conv[0].replace("\n", "\n\t") + "(*val->contents.err)")
                            out_c.write(err_map.ret_conv[1].replace("\n", "\n\t") + "\n\treturn " + err_map.ret_conv_name)
                        else:
                            out_c.write("return *val->contents.err")
                        out_c.write(";\n}\n")

                        out_java_struct.write("\t\tpublic " + err_map.java_hu_ty + " err;\n")
                        out_java_struct.write("\t\tprivate " + human_ty + "_Err(Object _dummy, long ptr) {\n")
                        out_java_struct.write("\t\t\tsuper(_dummy, ptr);\n")
                        if err_map.to_hu_conv is not None:
                            out_java_struct.write("\t\t\t" + err_map.java_ty + " err = bindings." + alias_match.group(2) + "_get_err(ptr);\n")
                            out_java_struct.write("\t\t\t" + err_map.to_hu_conv.replace("\n", "\n\t\t\t"))
                            out_java_struct.write("\n\t\t\tthis.err = " + err_map.to_hu_conv_name + ";\n")
                        else:
                            out_java_struct.write("\t\t\tthis.err = bindings." + alias_match.group(2) + "_get_err(ptr);\n")
                        out_java_struct.write("\t\t}\n\t}\n}\n")
            elif fn_ptr is not None:
                map_fn(line, fn_ptr, None, None)
            elif fn_ret_arr is not None:
                map_fn(line, fn_ret_arr, fn_ret_arr.group(4), None)
            elif reg_fn is not None:
                map_fn(line, reg_fn, None, None)
            elif const_val_regex is not None:
                # TODO Map const variables
                pass
            else:
                assert(line == "\n")

    out_java.write("}\n")
    for struct_name in opaque_structs:
        with open(sys.argv[3] + "/structs/" + struct_name.replace("LDK","") + ".java", "a") as out_java_struct:
            out_java_struct.write("}\n")
    for struct_name in trait_structs:
        with open(sys.argv[3] + "/structs/" + struct_name.replace("LDK","") + ".java", "a") as out_java_struct:
            out_java_struct.write("}\n")
