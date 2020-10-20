package org.ldk.structs;

import org.ldk.impl.bindings;
import org.ldk.enums.*;
import org.ldk.util.*;
import java.util.Arrays;

@SuppressWarnings("unchecked") // We correctly assign various generic arrays
public class Filter extends CommonBase {
	Filter(Object _dummy, long ptr) { super(ptr); }
	public Filter(bindings.LDKFilter arg) {
		super(bindings.LDKFilter_new(arg));
		this.ptrs_to.add(arg);
	}
	@Override @SuppressWarnings("deprecation")
	protected void finalize() throws Throwable {
		bindings.Filter_free(ptr); super.finalize();
	}

	public void register_tx(byte[] txid, byte[] script_pubkey) {
		bindings.Filter_register_tx(this.ptr, txid, script_pubkey);
	}

	public void register_output(OutPoint outpoint, byte[] script_pubkey) {
		bindings.Filter_register_output(this.ptr, outpoint == null ? 0 : outpoint.ptr & ~1, script_pubkey);
		this.ptrs_to.add(outpoint);
	}

}