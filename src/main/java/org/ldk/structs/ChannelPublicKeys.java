package org.ldk.structs;

import org.ldk.impl.bindings;
import org.ldk.enums.*;
import org.ldk.util.*;
import java.util.Arrays;
import javax.annotation.Nullable;


/**
 * One counterparty's public keys which do not change over the life of a channel.
 */
@SuppressWarnings("unchecked") // We correctly assign various generic arrays
public class ChannelPublicKeys extends CommonBase {
	ChannelPublicKeys(Object _dummy, long ptr) { super(ptr); }
	@Override @SuppressWarnings("deprecation")
	protected void finalize() throws Throwable {
		super.finalize();
		if (ptr != 0) { bindings.ChannelPublicKeys_free(ptr); }
	}

	/**
	 * The public key which is used to sign all commitment transactions, as it appears in the
	 * on-chain channel lock-in 2-of-2 multisig output.
	 */
	public byte[] get_funding_pubkey() {
		byte[] ret = bindings.ChannelPublicKeys_get_funding_pubkey(this.ptr);
		return ret;
	}

	/**
	 * The public key which is used to sign all commitment transactions, as it appears in the
	 * on-chain channel lock-in 2-of-2 multisig output.
	 */
	public void set_funding_pubkey(byte[] val) {
		bindings.ChannelPublicKeys_set_funding_pubkey(this.ptr, val);
	}

	/**
	 * The base point which is used (with derive_public_revocation_key) to derive per-commitment
	 * revocation keys. This is combined with the per-commitment-secret generated by the
	 * counterparty to create a secret which the counterparty can reveal to revoke previous
	 * states.
	 */
	public byte[] get_revocation_basepoint() {
		byte[] ret = bindings.ChannelPublicKeys_get_revocation_basepoint(this.ptr);
		return ret;
	}

	/**
	 * The base point which is used (with derive_public_revocation_key) to derive per-commitment
	 * revocation keys. This is combined with the per-commitment-secret generated by the
	 * counterparty to create a secret which the counterparty can reveal to revoke previous
	 * states.
	 */
	public void set_revocation_basepoint(byte[] val) {
		bindings.ChannelPublicKeys_set_revocation_basepoint(this.ptr, val);
	}

	/**
	 * The public key on which the non-broadcaster (ie the countersignatory) receives an immediately
	 * spendable primary channel balance on the broadcaster's commitment transaction. This key is
	 * static across every commitment transaction.
	 */
	public byte[] get_payment_point() {
		byte[] ret = bindings.ChannelPublicKeys_get_payment_point(this.ptr);
		return ret;
	}

	/**
	 * The public key on which the non-broadcaster (ie the countersignatory) receives an immediately
	 * spendable primary channel balance on the broadcaster's commitment transaction. This key is
	 * static across every commitment transaction.
	 */
	public void set_payment_point(byte[] val) {
		bindings.ChannelPublicKeys_set_payment_point(this.ptr, val);
	}

	/**
	 * The base point which is used (with derive_public_key) to derive a per-commitment payment
	 * public key which receives non-HTLC-encumbered funds which are only available for spending
	 * after some delay (or can be claimed via the revocation path).
	 */
	public byte[] get_delayed_payment_basepoint() {
		byte[] ret = bindings.ChannelPublicKeys_get_delayed_payment_basepoint(this.ptr);
		return ret;
	}

	/**
	 * The base point which is used (with derive_public_key) to derive a per-commitment payment
	 * public key which receives non-HTLC-encumbered funds which are only available for spending
	 * after some delay (or can be claimed via the revocation path).
	 */
	public void set_delayed_payment_basepoint(byte[] val) {
		bindings.ChannelPublicKeys_set_delayed_payment_basepoint(this.ptr, val);
	}

	/**
	 * The base point which is used (with derive_public_key) to derive a per-commitment public key
	 * which is used to encumber HTLC-in-flight outputs.
	 */
	public byte[] get_htlc_basepoint() {
		byte[] ret = bindings.ChannelPublicKeys_get_htlc_basepoint(this.ptr);
		return ret;
	}

	/**
	 * The base point which is used (with derive_public_key) to derive a per-commitment public key
	 * which is used to encumber HTLC-in-flight outputs.
	 */
	public void set_htlc_basepoint(byte[] val) {
		bindings.ChannelPublicKeys_set_htlc_basepoint(this.ptr, val);
	}

	/**
	 * Constructs a new ChannelPublicKeys given each field
	 */
	public static ChannelPublicKeys of(byte[] funding_pubkey_arg, byte[] revocation_basepoint_arg, byte[] payment_point_arg, byte[] delayed_payment_basepoint_arg, byte[] htlc_basepoint_arg) {
		long ret = bindings.ChannelPublicKeys_new(funding_pubkey_arg, revocation_basepoint_arg, payment_point_arg, delayed_payment_basepoint_arg, htlc_basepoint_arg);
		if (ret >= 0 && ret <= 4096) { return null; }
		ChannelPublicKeys ret_hu_conv = null; if (ret < 0 || ret > 4096) { ret_hu_conv = new ChannelPublicKeys(null, ret); }
		ret_hu_conv.ptrs_to.add(ret_hu_conv);
		return ret_hu_conv;
	}

	/**
	 * Creates a copy of the ChannelPublicKeys
	 */
	public ChannelPublicKeys clone() {
		long ret = bindings.ChannelPublicKeys_clone(this.ptr);
		if (ret >= 0 && ret <= 4096) { return null; }
		ChannelPublicKeys ret_hu_conv = null; if (ret < 0 || ret > 4096) { ret_hu_conv = new ChannelPublicKeys(null, ret); }
		ret_hu_conv.ptrs_to.add(this);
		return ret_hu_conv;
	}

	/**
	 * Serialize the ChannelPublicKeys object into a byte array which can be read by ChannelPublicKeys_read
	 */
	public byte[] write() {
		byte[] ret = bindings.ChannelPublicKeys_write(this.ptr);
		return ret;
	}

	/**
	 * Read a ChannelPublicKeys from a byte array, created by ChannelPublicKeys_write
	 */
	public static Result_ChannelPublicKeysDecodeErrorZ read(byte[] ser) {
		long ret = bindings.ChannelPublicKeys_read(ser);
		if (ret >= 0 && ret <= 4096) { return null; }
		Result_ChannelPublicKeysDecodeErrorZ ret_hu_conv = Result_ChannelPublicKeysDecodeErrorZ.constr_from_ptr(ret);
		return ret_hu_conv;
	}

}
