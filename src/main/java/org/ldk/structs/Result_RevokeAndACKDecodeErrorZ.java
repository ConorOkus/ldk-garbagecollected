package org.ldk.structs;

import org.ldk.impl.bindings;
import org.ldk.enums.*;
import org.ldk.util.*;
import java.util.Arrays;

@SuppressWarnings("unchecked") // We correctly assign various generic arrays
public class Result_RevokeAndACKDecodeErrorZ extends CommonBase {
	private Result_RevokeAndACKDecodeErrorZ(Object _dummy, long ptr) { super(ptr); }
	protected void finalize() throws Throwable {
		if (ptr != 0) { bindings.CResult_RevokeAndACKDecodeErrorZ_free(ptr); } super.finalize();
	}

	static Result_RevokeAndACKDecodeErrorZ constr_from_ptr(long ptr) {
		if (bindings.LDKCResult_RevokeAndACKDecodeErrorZ_result_ok(ptr)) {
			return new Result_RevokeAndACKDecodeErrorZ_OK(null, ptr);
		} else {
			return new Result_RevokeAndACKDecodeErrorZ_Err(null, ptr);
		}
	}
	public static final class Result_RevokeAndACKDecodeErrorZ_OK extends Result_RevokeAndACKDecodeErrorZ {
		public final RevokeAndACK res;
		private Result_RevokeAndACKDecodeErrorZ_OK(Object _dummy, long ptr) {
			super(_dummy, ptr);
			long res = bindings.LDKCResult_RevokeAndACKDecodeErrorZ_get_ok(ptr);
			RevokeAndACK res_hu_conv = new RevokeAndACK(null, res);
			res_hu_conv.ptrs_to.add(this);
			this.res = res_hu_conv;
		}
		public Result_RevokeAndACKDecodeErrorZ_OK(RevokeAndACK res) {
			this(null, bindings.CResult_RevokeAndACKDecodeErrorZ_ok(res == null ? 0 : res.ptr & ~1));
			this.ptrs_to.add(res);
		}
	}

	public static final class Result_RevokeAndACKDecodeErrorZ_Err extends Result_RevokeAndACKDecodeErrorZ {
		public final DecodeError err;
		private Result_RevokeAndACKDecodeErrorZ_Err(Object _dummy, long ptr) {
			super(_dummy, ptr);
			long err = bindings.LDKCResult_RevokeAndACKDecodeErrorZ_get_err(ptr);
			DecodeError err_hu_conv = new DecodeError(null, err);
			err_hu_conv.ptrs_to.add(this);
			this.err = err_hu_conv;
		}
		public Result_RevokeAndACKDecodeErrorZ_Err(DecodeError err) {
			this(null, bindings.CResult_RevokeAndACKDecodeErrorZ_err(err == null ? 0 : err.ptr & ~1));
			this.ptrs_to.add(err);
		}
	}
}
