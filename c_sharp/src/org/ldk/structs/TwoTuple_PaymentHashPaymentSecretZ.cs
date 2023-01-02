using org.ldk.impl;
using org.ldk.enums;
using org.ldk.util;
using System;

namespace org { namespace ldk { namespace structs {


/**
 * A Tuple
 */
public class TwoTuple_PaymentHashPaymentSecretZ : CommonBase {
	internal TwoTuple_PaymentHashPaymentSecretZ(object _dummy, long ptr) : base(ptr) { }
	~TwoTuple_PaymentHashPaymentSecretZ() {
		if (ptr != 0) { bindings.C2Tuple_PaymentHashPaymentSecretZ_free(ptr); }
	}

	/**
	 * 
	 */
	public byte[] get_a() {
		byte[] ret = bindings.C2Tuple_PaymentHashPaymentSecretZ_get_a(this.ptr);
		GC.KeepAlive(this);
		return ret;
	}

	/**
	 * 
	 */
	public byte[] get_b() {
		byte[] ret = bindings.C2Tuple_PaymentHashPaymentSecretZ_get_b(this.ptr);
		GC.KeepAlive(this);
		return ret;
	}

	internal long clone_ptr() {
		long ret = bindings.C2Tuple_PaymentHashPaymentSecretZ_clone_ptr(this.ptr);
		GC.KeepAlive(this);
		return ret;
	}

	/**
	 * Creates a new tuple which has the same data as `orig`
	 * but with all dynamically-allocated buffers duplicated in new buffers.
	 */
	public TwoTuple_PaymentHashPaymentSecretZ clone() {
		long ret = bindings.C2Tuple_PaymentHashPaymentSecretZ_clone(this.ptr);
		GC.KeepAlive(this);
		if (ret >= 0 && ret <= 4096) { return null; }
		TwoTuple_PaymentHashPaymentSecretZ ret_hu_conv = new TwoTuple_PaymentHashPaymentSecretZ(null, ret);
		if (ret_hu_conv != null) { ret_hu_conv.ptrs_to.AddLast(this); };
		return ret_hu_conv;
	}

	/**
	 * Creates a new C2Tuple_PaymentHashPaymentSecretZ from the contained elements.
	 */
	public static TwoTuple_PaymentHashPaymentSecretZ of(byte[] a, byte[] b) {
		long ret = bindings.C2Tuple_PaymentHashPaymentSecretZ_new(InternalUtils.check_arr_len(a, 32), InternalUtils.check_arr_len(b, 32));
		GC.KeepAlive(a);
		GC.KeepAlive(b);
		if (ret >= 0 && ret <= 4096) { return null; }
		TwoTuple_PaymentHashPaymentSecretZ ret_hu_conv = new TwoTuple_PaymentHashPaymentSecretZ(null, ret);
		if (ret_hu_conv != null) { ret_hu_conv.ptrs_to.AddLast(ret_hu_conv); };
		return ret_hu_conv;
	}

}
} } }
