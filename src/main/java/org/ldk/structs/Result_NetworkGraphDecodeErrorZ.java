package org.ldk.structs;

import org.ldk.impl.bindings;
import org.ldk.enums.*;
import org.ldk.util.*;
import java.util.Arrays;

@SuppressWarnings("unchecked") // We correctly assign various generic arrays
public class Result_NetworkGraphDecodeErrorZ extends CommonBase {
	private Result_NetworkGraphDecodeErrorZ(Object _dummy, long ptr) { super(ptr); }
	protected void finalize() throws Throwable {
		if (ptr != 0) { bindings.CResult_NetworkGraphDecodeErrorZ_free(ptr); } super.finalize();
	}

	static Result_NetworkGraphDecodeErrorZ constr_from_ptr(long ptr) {
		if (bindings.LDKCResult_NetworkGraphDecodeErrorZ_result_ok(ptr)) {
			return new Result_NetworkGraphDecodeErrorZ_OK(null, ptr);
		} else {
			return new Result_NetworkGraphDecodeErrorZ_Err(null, ptr);
		}
	}
	public static final class Result_NetworkGraphDecodeErrorZ_OK extends Result_NetworkGraphDecodeErrorZ {
		public final NetworkGraph res;
		private Result_NetworkGraphDecodeErrorZ_OK(Object _dummy, long ptr) {
			super(_dummy, ptr);
			long res = bindings.LDKCResult_NetworkGraphDecodeErrorZ_get_ok(ptr);
			NetworkGraph res_hu_conv = new NetworkGraph(null, res);
			res_hu_conv.ptrs_to.add(this);
			this.res = res_hu_conv;
		}
		public Result_NetworkGraphDecodeErrorZ_OK(NetworkGraph res) {
			this(null, bindings.CResult_NetworkGraphDecodeErrorZ_ok(res == null ? 0 : res.ptr & ~1));
			this.ptrs_to.add(res);
		}
	}

	public static final class Result_NetworkGraphDecodeErrorZ_Err extends Result_NetworkGraphDecodeErrorZ {
		public final DecodeError err;
		private Result_NetworkGraphDecodeErrorZ_Err(Object _dummy, long ptr) {
			super(_dummy, ptr);
			long err = bindings.LDKCResult_NetworkGraphDecodeErrorZ_get_err(ptr);
			DecodeError err_hu_conv = new DecodeError(null, err);
			err_hu_conv.ptrs_to.add(this);
			this.err = err_hu_conv;
		}
		public Result_NetworkGraphDecodeErrorZ_Err(DecodeError err) {
			this(null, bindings.CResult_NetworkGraphDecodeErrorZ_err(err == null ? 0 : err.ptr & ~1));
			this.ptrs_to.add(err);
		}
	}
}
