package org.ldk.structs;

import org.ldk.impl.bindings;
import org.ldk.enums.*;
import org.ldk.util.*;
import java.util.Arrays;
import java.lang.ref.Reference;
import javax.annotation.Nullable;

public class Result_PhantomRouteHintsDecodeErrorZ extends CommonBase {
	private Result_PhantomRouteHintsDecodeErrorZ(Object _dummy, long ptr) { super(ptr); }
	protected void finalize() throws Throwable {
		if (ptr != 0) { bindings.CResult_PhantomRouteHintsDecodeErrorZ_free(ptr); } super.finalize();
	}

	static Result_PhantomRouteHintsDecodeErrorZ constr_from_ptr(long ptr) {
		if (bindings.CResult_PhantomRouteHintsDecodeErrorZ_is_ok(ptr)) {
			return new Result_PhantomRouteHintsDecodeErrorZ_OK(null, ptr);
		} else {
			return new Result_PhantomRouteHintsDecodeErrorZ_Err(null, ptr);
		}
	}
	public static final class Result_PhantomRouteHintsDecodeErrorZ_OK extends Result_PhantomRouteHintsDecodeErrorZ {
		public final PhantomRouteHints res;
		private Result_PhantomRouteHintsDecodeErrorZ_OK(Object _dummy, long ptr) {
			super(_dummy, ptr);
			long res = bindings.CResult_PhantomRouteHintsDecodeErrorZ_get_ok(ptr);
			org.ldk.structs.PhantomRouteHints res_hu_conv = null; if (res < 0 || res > 4096) { res_hu_conv = new org.ldk.structs.PhantomRouteHints(null, res); }
			res_hu_conv.ptrs_to.add(this);
			this.res = res_hu_conv;
		}
	}

	public static final class Result_PhantomRouteHintsDecodeErrorZ_Err extends Result_PhantomRouteHintsDecodeErrorZ {
		public final DecodeError err;
		private Result_PhantomRouteHintsDecodeErrorZ_Err(Object _dummy, long ptr) {
			super(_dummy, ptr);
			long err = bindings.CResult_PhantomRouteHintsDecodeErrorZ_get_err(ptr);
			org.ldk.structs.DecodeError err_hu_conv = null; if (err < 0 || err > 4096) { err_hu_conv = new org.ldk.structs.DecodeError(null, err); }
			err_hu_conv.ptrs_to.add(this);
			this.err = err_hu_conv;
		}
	}

	/**
	 * Creates a new CResult_PhantomRouteHintsDecodeErrorZ in the success state.
	 */
	public static Result_PhantomRouteHintsDecodeErrorZ ok(PhantomRouteHints o) {
		long ret = bindings.CResult_PhantomRouteHintsDecodeErrorZ_ok(o == null ? 0 : o.ptr);
		Reference.reachabilityFence(o);
		if (ret >= 0 && ret <= 4096) { return null; }
		Result_PhantomRouteHintsDecodeErrorZ ret_hu_conv = Result_PhantomRouteHintsDecodeErrorZ.constr_from_ptr(ret);
		ret_hu_conv.ptrs_to.add(o);
		return ret_hu_conv;
	}

	/**
	 * Creates a new CResult_PhantomRouteHintsDecodeErrorZ in the error state.
	 */
	public static Result_PhantomRouteHintsDecodeErrorZ err(DecodeError e) {
		long ret = bindings.CResult_PhantomRouteHintsDecodeErrorZ_err(e == null ? 0 : e.ptr);
		Reference.reachabilityFence(e);
		if (ret >= 0 && ret <= 4096) { return null; }
		Result_PhantomRouteHintsDecodeErrorZ ret_hu_conv = Result_PhantomRouteHintsDecodeErrorZ.constr_from_ptr(ret);
		ret_hu_conv.ptrs_to.add(e);
		return ret_hu_conv;
	}

	/**
	 * Checks if the given object is currently in the success state
	 */
	public boolean is_ok() {
		boolean ret = bindings.CResult_PhantomRouteHintsDecodeErrorZ_is_ok(this.ptr);
		Reference.reachabilityFence(this);
		return ret;
	}

	long clone_ptr() {
		long ret = bindings.CResult_PhantomRouteHintsDecodeErrorZ_clone_ptr(this.ptr);
		Reference.reachabilityFence(this);
		return ret;
	}

	/**
	 * Creates a new CResult_PhantomRouteHintsDecodeErrorZ which has the same data as `orig`
	 * but with all dynamically-allocated buffers duplicated in new buffers.
	 */
	public Result_PhantomRouteHintsDecodeErrorZ clone() {
		long ret = bindings.CResult_PhantomRouteHintsDecodeErrorZ_clone(this.ptr);
		Reference.reachabilityFence(this);
		if (ret >= 0 && ret <= 4096) { return null; }
		Result_PhantomRouteHintsDecodeErrorZ ret_hu_conv = Result_PhantomRouteHintsDecodeErrorZ.constr_from_ptr(ret);
		return ret_hu_conv;
	}

}
