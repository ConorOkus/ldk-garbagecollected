import { TxOut } from '../structs/TxOut.mjs';
import { BigEndianScalar } from '../structs/BigEndianScalar.mjs';
import { AccessError } from '../enums/AccessError.mjs';
import { COption_NoneZ } from '../enums/COption_NoneZ.mjs';
import { ChannelMonitorUpdateStatus } from '../enums/ChannelMonitorUpdateStatus.mjs';
import { ConfirmationTarget } from '../enums/ConfirmationTarget.mjs';
import { CreationError } from '../enums/CreationError.mjs';
import { Currency } from '../enums/Currency.mjs';
import { HTLCClaim } from '../enums/HTLCClaim.mjs';
import { IOError } from '../enums/IOError.mjs';
import { Level } from '../enums/Level.mjs';
import { Network } from '../enums/Network.mjs';
import { Recipient } from '../enums/Recipient.mjs';
import { Secp256k1Error } from '../enums/Secp256k1Error.mjs';
import { SemanticError } from '../enums/SemanticError.mjs';
import { SiPrefix } from '../enums/SiPrefix.mjs';
import { Bech32Error } from '../structs/Bech32Error.mjs';
import { Option_HTLCClaimZ } from '../structs/Option_HTLCClaimZ.mjs';
import { Result_NoneNoneZ } from '../structs/Result_NoneNoneZ.mjs';
import { CounterpartyCommitmentSecrets } from '../structs/CounterpartyCommitmentSecrets.mjs';
import { DecodeError } from '../structs/DecodeError.mjs';
import { Result_CounterpartyCommitmentSecretsDecodeErrorZ } from '../structs/Result_CounterpartyCommitmentSecretsDecodeErrorZ.mjs';
import { TxCreationKeys } from '../structs/TxCreationKeys.mjs';
import { Result_TxCreationKeysDecodeErrorZ } from '../structs/Result_TxCreationKeysDecodeErrorZ.mjs';
import { ChannelPublicKeys } from '../structs/ChannelPublicKeys.mjs';
import { Result_ChannelPublicKeysDecodeErrorZ } from '../structs/Result_ChannelPublicKeysDecodeErrorZ.mjs';
import { Option_u32Z } from '../structs/Option_u32Z.mjs';
import { HTLCOutputInCommitment } from '../structs/HTLCOutputInCommitment.mjs';
import { Result_HTLCOutputInCommitmentDecodeErrorZ } from '../structs/Result_HTLCOutputInCommitmentDecodeErrorZ.mjs';
import { CounterpartyChannelTransactionParameters } from '../structs/CounterpartyChannelTransactionParameters.mjs';
import { Result_CounterpartyChannelTransactionParametersDecodeErrorZ } from '../structs/Result_CounterpartyChannelTransactionParametersDecodeErrorZ.mjs';
import { ChannelTransactionParameters } from '../structs/ChannelTransactionParameters.mjs';
import { Result_ChannelTransactionParametersDecodeErrorZ } from '../structs/Result_ChannelTransactionParametersDecodeErrorZ.mjs';
import { HolderCommitmentTransaction } from '../structs/HolderCommitmentTransaction.mjs';
import { Result_HolderCommitmentTransactionDecodeErrorZ } from '../structs/Result_HolderCommitmentTransactionDecodeErrorZ.mjs';
import { BuiltCommitmentTransaction } from '../structs/BuiltCommitmentTransaction.mjs';
import { Result_BuiltCommitmentTransactionDecodeErrorZ } from '../structs/Result_BuiltCommitmentTransactionDecodeErrorZ.mjs';
import { TrustedClosingTransaction } from '../structs/TrustedClosingTransaction.mjs';
import { Result_TrustedClosingTransactionNoneZ } from '../structs/Result_TrustedClosingTransactionNoneZ.mjs';
import { CommitmentTransaction } from '../structs/CommitmentTransaction.mjs';
import { Result_CommitmentTransactionDecodeErrorZ } from '../structs/Result_CommitmentTransactionDecodeErrorZ.mjs';
import { TrustedCommitmentTransaction } from '../structs/TrustedCommitmentTransaction.mjs';
import { Result_TrustedCommitmentTransactionNoneZ } from '../structs/Result_TrustedCommitmentTransactionNoneZ.mjs';
import { Result_CVec_SignatureZNoneZ } from '../structs/Result_CVec_SignatureZNoneZ.mjs';
import { ShutdownScript } from '../structs/ShutdownScript.mjs';
import { Result_ShutdownScriptDecodeErrorZ } from '../structs/Result_ShutdownScriptDecodeErrorZ.mjs';
import { InvalidShutdownScript } from '../structs/InvalidShutdownScript.mjs';
import { Result_ShutdownScriptInvalidShutdownScriptZ } from '../structs/Result_ShutdownScriptInvalidShutdownScriptZ.mjs';
import { BlindedPath } from '../structs/BlindedPath.mjs';
import { Result_BlindedPathNoneZ } from '../structs/Result_BlindedPathNoneZ.mjs';
import { Result_BlindedPathDecodeErrorZ } from '../structs/Result_BlindedPathDecodeErrorZ.mjs';
import { BlindedHop } from '../structs/BlindedHop.mjs';
import { Result_BlindedHopDecodeErrorZ } from '../structs/Result_BlindedHopDecodeErrorZ.mjs';
import { ChannelDetails } from '../structs/ChannelDetails.mjs';
import { Route } from '../structs/Route.mjs';
import { LightningError } from '../structs/LightningError.mjs';
import { Result_RouteLightningErrorZ } from '../structs/Result_RouteLightningErrorZ.mjs';
import { RouteHop } from '../structs/RouteHop.mjs';
import { Option_u64Z } from '../structs/Option_u64Z.mjs';
import { InFlightHtlcs } from '../structs/InFlightHtlcs.mjs';
import { Result_InFlightHtlcsDecodeErrorZ } from '../structs/Result_InFlightHtlcsDecodeErrorZ.mjs';
import { Result_RouteHopDecodeErrorZ } from '../structs/Result_RouteHopDecodeErrorZ.mjs';
import { Result_RouteDecodeErrorZ } from '../structs/Result_RouteDecodeErrorZ.mjs';
import { RouteParameters } from '../structs/RouteParameters.mjs';
import { Result_RouteParametersDecodeErrorZ } from '../structs/Result_RouteParametersDecodeErrorZ.mjs';
import { RouteHint } from '../structs/RouteHint.mjs';
import { PaymentParameters } from '../structs/PaymentParameters.mjs';
import { Result_PaymentParametersDecodeErrorZ } from '../structs/Result_PaymentParametersDecodeErrorZ.mjs';
import { RouteHintHop } from '../structs/RouteHintHop.mjs';
import { Result_RouteHintDecodeErrorZ } from '../structs/Result_RouteHintDecodeErrorZ.mjs';
import { Result_RouteHintHopDecodeErrorZ } from '../structs/Result_RouteHintHopDecodeErrorZ.mjs';
import { PaymentPurpose } from '../structs/PaymentPurpose.mjs';
import { Result_PaymentPurposeDecodeErrorZ } from '../structs/Result_PaymentPurposeDecodeErrorZ.mjs';
import { ClosureReason } from '../structs/ClosureReason.mjs';
import { Option_ClosureReasonZ } from '../structs/Option_ClosureReasonZ.mjs';
import { Result_COption_ClosureReasonZDecodeErrorZ } from '../structs/Result_COption_ClosureReasonZDecodeErrorZ.mjs';
import { HTLCDestination } from '../structs/HTLCDestination.mjs';
import { Option_HTLCDestinationZ } from '../structs/Option_HTLCDestinationZ.mjs';
import { Result_COption_HTLCDestinationZDecodeErrorZ } from '../structs/Result_COption_HTLCDestinationZDecodeErrorZ.mjs';
import { Option_u128Z } from '../structs/Option_u128Z.mjs';
import { ChannelUpdate } from '../structs/ChannelUpdate.mjs';
import { NetworkUpdate } from '../structs/NetworkUpdate.mjs';
import { Option_NetworkUpdateZ } from '../structs/Option_NetworkUpdateZ.mjs';
import { OutPoint } from '../structs/OutPoint.mjs';
import { DelayedPaymentOutputDescriptor } from '../structs/DelayedPaymentOutputDescriptor.mjs';
import { StaticPaymentOutputDescriptor } from '../structs/StaticPaymentOutputDescriptor.mjs';
import { SpendableOutputDescriptor } from '../structs/SpendableOutputDescriptor.mjs';
import { ChannelTypeFeatures } from '../structs/ChannelTypeFeatures.mjs';
import { Option_EventZ } from '../structs/Option_EventZ.mjs';
import { Result_COption_EventZDecodeErrorZ } from '../structs/Result_COption_EventZDecodeErrorZ.mjs';
import { AcceptChannel } from '../structs/AcceptChannel.mjs';
import { OpenChannel } from '../structs/OpenChannel.mjs';
import { FundingCreated } from '../structs/FundingCreated.mjs';
import { FundingSigned } from '../structs/FundingSigned.mjs';
import { ChannelReady } from '../structs/ChannelReady.mjs';
import { AnnouncementSignatures } from '../structs/AnnouncementSignatures.mjs';
import { CommitmentUpdate } from '../structs/CommitmentUpdate.mjs';
import { RevokeAndACK } from '../structs/RevokeAndACK.mjs';
import { ClosingSigned } from '../structs/ClosingSigned.mjs';
import { Shutdown } from '../structs/Shutdown.mjs';
import { ChannelReestablish } from '../structs/ChannelReestablish.mjs';
import { ChannelAnnouncement } from '../structs/ChannelAnnouncement.mjs';
import { ErrorMessage } from '../structs/ErrorMessage.mjs';
import { WarningMessage } from '../structs/WarningMessage.mjs';
import { ErrorAction } from '../structs/ErrorAction.mjs';
import { QueryChannelRange } from '../structs/QueryChannelRange.mjs';
import { QueryShortChannelIds } from '../structs/QueryShortChannelIds.mjs';
import { ReplyChannelRange } from '../structs/ReplyChannelRange.mjs';
import { GossipTimestampFilter } from '../structs/GossipTimestampFilter.mjs';
import { MessageSendEvent } from '../structs/MessageSendEvent.mjs';
import { Result_TxOutAccessErrorZ } from '../structs/Result_TxOutAccessErrorZ.mjs';
import { TwoTuple_usizeTransactionZ } from '../structs/TwoTuple_usizeTransactionZ.mjs';
import { TwoTuple_TxidBlockHashZ } from '../structs/TwoTuple_TxidBlockHashZ.mjs';
import { HTLCUpdate } from '../structs/HTLCUpdate.mjs';
import { MonitorEvent } from '../structs/MonitorEvent.mjs';
import { ThreeTuple_OutPointCVec_MonitorEventZPublicKeyZ } from '../structs/ThreeTuple_OutPointCVec_MonitorEventZPublicKeyZ.mjs';
import { FixedPenaltyScorer } from '../structs/FixedPenaltyScorer.mjs';
import { Result_FixedPenaltyScorerDecodeErrorZ } from '../structs/Result_FixedPenaltyScorerDecodeErrorZ.mjs';
import { TwoTuple_u64u64Z } from '../structs/TwoTuple_u64u64Z.mjs';
import { Option_C2Tuple_u64u64ZZ } from '../structs/Option_C2Tuple_u64u64ZZ.mjs';
import { NodeId } from '../structs/NodeId.mjs';
import { Record } from '../structs/Record.mjs';
import { Logger, LoggerInterface } from '../structs/Logger.mjs';
import { NetworkGraph } from '../structs/NetworkGraph.mjs';
import { ProbabilisticScorer } from '../structs/ProbabilisticScorer.mjs';
import { Result_ProbabilisticScorerDecodeErrorZ } from '../structs/Result_ProbabilisticScorerDecodeErrorZ.mjs';
import { InitFeatures } from '../structs/InitFeatures.mjs';
import { Result_InitFeaturesDecodeErrorZ } from '../structs/Result_InitFeaturesDecodeErrorZ.mjs';
import { ChannelFeatures } from '../structs/ChannelFeatures.mjs';
import { Result_ChannelFeaturesDecodeErrorZ } from '../structs/Result_ChannelFeaturesDecodeErrorZ.mjs';
import { NodeFeatures } from '../structs/NodeFeatures.mjs';
import { Result_NodeFeaturesDecodeErrorZ } from '../structs/Result_NodeFeaturesDecodeErrorZ.mjs';
import { InvoiceFeatures } from '../structs/InvoiceFeatures.mjs';
import { Result_InvoiceFeaturesDecodeErrorZ } from '../structs/Result_InvoiceFeaturesDecodeErrorZ.mjs';
import { Result_ChannelTypeFeaturesDecodeErrorZ } from '../structs/Result_ChannelTypeFeaturesDecodeErrorZ.mjs';
import { OfferFeatures } from '../structs/OfferFeatures.mjs';
import { Result_OfferFeaturesDecodeErrorZ } from '../structs/Result_OfferFeaturesDecodeErrorZ.mjs';
import { InvoiceRequestFeatures } from '../structs/InvoiceRequestFeatures.mjs';
import { Result_InvoiceRequestFeaturesDecodeErrorZ } from '../structs/Result_InvoiceRequestFeaturesDecodeErrorZ.mjs';
import { Result_NodeIdDecodeErrorZ } from '../structs/Result_NodeIdDecodeErrorZ.mjs';
import { Result_COption_NetworkUpdateZDecodeErrorZ } from '../structs/Result_COption_NetworkUpdateZDecodeErrorZ.mjs';
import { Access, AccessInterface } from '../structs/Access.mjs';
import { Option_AccessZ } from '../structs/Option_AccessZ.mjs';
import { Result_boolLightningErrorZ } from '../structs/Result_boolLightningErrorZ.mjs';
import { ThreeTuple_ChannelAnnouncementChannelUpdateChannelUpdateZ } from '../structs/ThreeTuple_ChannelAnnouncementChannelUpdateChannelUpdateZ.mjs';
import { Option_C3Tuple_ChannelAnnouncementChannelUpdateChannelUpdateZZ } from '../structs/Option_C3Tuple_ChannelAnnouncementChannelUpdateChannelUpdateZZ.mjs';
import { Result_NoneLightningErrorZ } from '../structs/Result_NoneLightningErrorZ.mjs';
import { ChannelUpdateInfo } from '../structs/ChannelUpdateInfo.mjs';
import { Result_ChannelUpdateInfoDecodeErrorZ } from '../structs/Result_ChannelUpdateInfoDecodeErrorZ.mjs';
import { ChannelInfo } from '../structs/ChannelInfo.mjs';
import { Result_ChannelInfoDecodeErrorZ } from '../structs/Result_ChannelInfoDecodeErrorZ.mjs';
import { RoutingFees } from '../structs/RoutingFees.mjs';
import { Result_RoutingFeesDecodeErrorZ } from '../structs/Result_RoutingFeesDecodeErrorZ.mjs';
import { Hostname } from '../structs/Hostname.mjs';
import { NetAddress } from '../structs/NetAddress.mjs';
import { NodeAnnouncementInfo } from '../structs/NodeAnnouncementInfo.mjs';
import { Result_NodeAnnouncementInfoDecodeErrorZ } from '../structs/Result_NodeAnnouncementInfoDecodeErrorZ.mjs';
import { NodeAlias } from '../structs/NodeAlias.mjs';
import { Result_NodeAliasDecodeErrorZ } from '../structs/Result_NodeAliasDecodeErrorZ.mjs';
import { NodeInfo } from '../structs/NodeInfo.mjs';
import { Result_NodeInfoDecodeErrorZ } from '../structs/Result_NodeInfoDecodeErrorZ.mjs';
import { Result_NetworkGraphDecodeErrorZ } from '../structs/Result_NetworkGraphDecodeErrorZ.mjs';
import { Option_CVec_NetAddressZZ } from '../structs/Option_CVec_NetAddressZZ.mjs';
import { Result_DelayedPaymentOutputDescriptorDecodeErrorZ } from '../structs/Result_DelayedPaymentOutputDescriptorDecodeErrorZ.mjs';
import { Result_StaticPaymentOutputDescriptorDecodeErrorZ } from '../structs/Result_StaticPaymentOutputDescriptorDecodeErrorZ.mjs';
import { Result_SpendableOutputDescriptorDecodeErrorZ } from '../structs/Result_SpendableOutputDescriptorDecodeErrorZ.mjs';
import { TwoTuple_SignatureCVec_SignatureZZ } from '../structs/TwoTuple_SignatureCVec_SignatureZZ.mjs';
import { Result_C2Tuple_SignatureCVec_SignatureZZNoneZ } from '../structs/Result_C2Tuple_SignatureCVec_SignatureZZNoneZ.mjs';
import { Result_SignatureNoneZ } from '../structs/Result_SignatureNoneZ.mjs';
import { TwoTuple_SignatureSignatureZ } from '../structs/TwoTuple_SignatureSignatureZ.mjs';
import { Result_C2Tuple_SignatureSignatureZNoneZ } from '../structs/Result_C2Tuple_SignatureSignatureZNoneZ.mjs';
import { Result_SecretKeyNoneZ } from '../structs/Result_SecretKeyNoneZ.mjs';
import { Result_PublicKeyNoneZ } from '../structs/Result_PublicKeyNoneZ.mjs';
import { Option_ScalarZ } from '../structs/Option_ScalarZ.mjs';
import { Result_SharedSecretNoneZ } from '../structs/Result_SharedSecretNoneZ.mjs';
import { ClosingTransaction } from '../structs/ClosingTransaction.mjs';
import { UnsignedChannelAnnouncement } from '../structs/UnsignedChannelAnnouncement.mjs';
import { BaseSign, BaseSignInterface } from '../structs/BaseSign.mjs';
import { Sign, SignInterface } from '../structs/Sign.mjs';
import { Result_SignDecodeErrorZ } from '../structs/Result_SignDecodeErrorZ.mjs';
import { Result_RecoverableSignatureNoneZ } from '../structs/Result_RecoverableSignatureNoneZ.mjs';
import { Result_CVec_CVec_u8ZZNoneZ } from '../structs/Result_CVec_CVec_u8ZZNoneZ.mjs';
import { InMemorySigner } from '../structs/InMemorySigner.mjs';
import { Result_InMemorySignerDecodeErrorZ } from '../structs/Result_InMemorySignerDecodeErrorZ.mjs';
import { Result_TransactionNoneZ } from '../structs/Result_TransactionNoneZ.mjs';
import { Option_u16Z } from '../structs/Option_u16Z.mjs';
import { APIError } from '../structs/APIError.mjs';
import { Result_NoneAPIErrorZ } from '../structs/Result_NoneAPIErrorZ.mjs';
import { Result__u832APIErrorZ } from '../structs/Result__u832APIErrorZ.mjs';
import { PaymentSendFailure } from '../structs/PaymentSendFailure.mjs';
import { Result_NonePaymentSendFailureZ } from '../structs/Result_NonePaymentSendFailureZ.mjs';
import { Result_PaymentHashPaymentSendFailureZ } from '../structs/Result_PaymentHashPaymentSendFailureZ.mjs';
import { TwoTuple_PaymentHashPaymentIdZ } from '../structs/TwoTuple_PaymentHashPaymentIdZ.mjs';
import { Result_C2Tuple_PaymentHashPaymentIdZPaymentSendFailureZ } from '../structs/Result_C2Tuple_PaymentHashPaymentIdZPaymentSendFailureZ.mjs';
import { TwoTuple_PaymentHashPaymentSecretZ } from '../structs/TwoTuple_PaymentHashPaymentSecretZ.mjs';
import { Result_C2Tuple_PaymentHashPaymentSecretZNoneZ } from '../structs/Result_C2Tuple_PaymentHashPaymentSecretZNoneZ.mjs';
import { Result_C2Tuple_PaymentHashPaymentSecretZAPIErrorZ } from '../structs/Result_C2Tuple_PaymentHashPaymentSecretZAPIErrorZ.mjs';
import { Result_PaymentSecretNoneZ } from '../structs/Result_PaymentSecretNoneZ.mjs';
import { Result_PaymentSecretAPIErrorZ } from '../structs/Result_PaymentSecretAPIErrorZ.mjs';
import { Result_PaymentPreimageAPIErrorZ } from '../structs/Result_PaymentPreimageAPIErrorZ.mjs';
import { CounterpartyForwardingInfo } from '../structs/CounterpartyForwardingInfo.mjs';
import { Result_CounterpartyForwardingInfoDecodeErrorZ } from '../structs/Result_CounterpartyForwardingInfoDecodeErrorZ.mjs';
import { ChannelCounterparty } from '../structs/ChannelCounterparty.mjs';
import { Result_ChannelCounterpartyDecodeErrorZ } from '../structs/Result_ChannelCounterpartyDecodeErrorZ.mjs';
import { Result_ChannelDetailsDecodeErrorZ } from '../structs/Result_ChannelDetailsDecodeErrorZ.mjs';
import { PhantomRouteHints } from '../structs/PhantomRouteHints.mjs';
import { Result_PhantomRouteHintsDecodeErrorZ } from '../structs/Result_PhantomRouteHintsDecodeErrorZ.mjs';
import { ChannelMonitor } from '../structs/ChannelMonitor.mjs';
import { ChannelMonitorUpdate } from '../structs/ChannelMonitorUpdate.mjs';
import { Watch, WatchInterface } from '../structs/Watch.mjs';
import { BroadcasterInterface, BroadcasterInterfaceInterface } from '../structs/BroadcasterInterface.mjs';
import { KeysInterface, KeysInterfaceInterface } from '../structs/KeysInterface.mjs';
import { FeeEstimator, FeeEstimatorInterface } from '../structs/FeeEstimator.mjs';
import { ChannelManager } from '../structs/ChannelManager.mjs';
import { TwoTuple_BlockHashChannelManagerZ } from '../structs/TwoTuple_BlockHashChannelManagerZ.mjs';
import { Result_C2Tuple_BlockHashChannelManagerZDecodeErrorZ } from '../structs/Result_C2Tuple_BlockHashChannelManagerZDecodeErrorZ.mjs';
import { ChannelConfig } from '../structs/ChannelConfig.mjs';
import { Result_ChannelConfigDecodeErrorZ } from '../structs/Result_ChannelConfigDecodeErrorZ.mjs';
import { Result_OutPointDecodeErrorZ } from '../structs/Result_OutPointDecodeErrorZ.mjs';
import { Type, TypeInterface } from '../structs/Type.mjs';
import { Option_TypeZ } from '../structs/Option_TypeZ.mjs';
import { Result_COption_TypeZDecodeErrorZ } from '../structs/Result_COption_TypeZDecodeErrorZ.mjs';
import { PaymentError } from '../structs/PaymentError.mjs';
import { Result_PaymentIdPaymentErrorZ } from '../structs/Result_PaymentIdPaymentErrorZ.mjs';
import { Result_NonePaymentErrorZ } from '../structs/Result_NonePaymentErrorZ.mjs';
import { Result_StringErrorZ } from '../structs/Result_StringErrorZ.mjs';
import { Result_PublicKeyErrorZ } from '../structs/Result_PublicKeyErrorZ.mjs';
import { Result_ChannelMonitorUpdateDecodeErrorZ } from '../structs/Result_ChannelMonitorUpdateDecodeErrorZ.mjs';
import { Option_MonitorEventZ } from '../structs/Option_MonitorEventZ.mjs';
import { Result_COption_MonitorEventZDecodeErrorZ } from '../structs/Result_COption_MonitorEventZDecodeErrorZ.mjs';
import { Result_HTLCUpdateDecodeErrorZ } from '../structs/Result_HTLCUpdateDecodeErrorZ.mjs';
import { TwoTuple_OutPointScriptZ } from '../structs/TwoTuple_OutPointScriptZ.mjs';
import { TwoTuple_u32ScriptZ } from '../structs/TwoTuple_u32ScriptZ.mjs';
import { TwoTuple_TxidCVec_C2Tuple_u32ScriptZZZ } from '../structs/TwoTuple_TxidCVec_C2Tuple_u32ScriptZZZ.mjs';
import { TwoTuple_u32TxOutZ } from '../structs/TwoTuple_u32TxOutZ.mjs';
import { TwoTuple_TxidCVec_C2Tuple_u32TxOutZZZ } from '../structs/TwoTuple_TxidCVec_C2Tuple_u32TxOutZZZ.mjs';
import { Balance } from '../structs/Balance.mjs';
import { TwoTuple_BlockHashChannelMonitorZ } from '../structs/TwoTuple_BlockHashChannelMonitorZ.mjs';
import { Result_C2Tuple_BlockHashChannelMonitorZDecodeErrorZ } from '../structs/Result_C2Tuple_BlockHashChannelMonitorZDecodeErrorZ.mjs';
import { TwoTuple_PublicKeyTypeZ } from '../structs/TwoTuple_PublicKeyTypeZ.mjs';
import { CustomOnionMessageContents, CustomOnionMessageContentsInterface } from '../structs/CustomOnionMessageContents.mjs';
import { Option_CustomOnionMessageContentsZ } from '../structs/Option_CustomOnionMessageContentsZ.mjs';
import { Result_COption_CustomOnionMessageContentsZDecodeErrorZ } from '../structs/Result_COption_CustomOnionMessageContentsZDecodeErrorZ.mjs';
import { Option_NetAddressZ } from '../structs/Option_NetAddressZ.mjs';
import { PeerHandleError } from '../structs/PeerHandleError.mjs';
import { Result_CVec_u8ZPeerHandleErrorZ } from '../structs/Result_CVec_u8ZPeerHandleErrorZ.mjs';
import { Result_NonePeerHandleErrorZ } from '../structs/Result_NonePeerHandleErrorZ.mjs';
import { Result_boolPeerHandleErrorZ } from '../structs/Result_boolPeerHandleErrorZ.mjs';
import { SendError } from '../structs/SendError.mjs';
import { Result_NoneSendErrorZ } from '../structs/Result_NoneSendErrorZ.mjs';
import { GraphSyncError } from '../structs/GraphSyncError.mjs';
import { Result_u32GraphSyncErrorZ } from '../structs/Result_u32GraphSyncErrorZ.mjs';
import { ParseError } from '../structs/ParseError.mjs';
import { Result_SiPrefixParseErrorZ } from '../structs/Result_SiPrefixParseErrorZ.mjs';
import { Invoice } from '../structs/Invoice.mjs';
import { ParseOrSemanticError } from '../structs/ParseOrSemanticError.mjs';
import { Result_InvoiceParseOrSemanticErrorZ } from '../structs/Result_InvoiceParseOrSemanticErrorZ.mjs';
import { SignedRawInvoice } from '../structs/SignedRawInvoice.mjs';
import { Result_SignedRawInvoiceParseErrorZ } from '../structs/Result_SignedRawInvoiceParseErrorZ.mjs';
import { RawInvoice } from '../structs/RawInvoice.mjs';
import { InvoiceSignature } from '../structs/InvoiceSignature.mjs';
import { ThreeTuple_RawInvoice_u832InvoiceSignatureZ } from '../structs/ThreeTuple_RawInvoice_u832InvoiceSignatureZ.mjs';
import { PayeePubKey } from '../structs/PayeePubKey.mjs';
import { Result_PayeePubKeyErrorZ } from '../structs/Result_PayeePubKeyErrorZ.mjs';
import { PrivateRoute } from '../structs/PrivateRoute.mjs';
import { PositiveTimestamp } from '../structs/PositiveTimestamp.mjs';
import { Result_PositiveTimestampCreationErrorZ } from '../structs/Result_PositiveTimestampCreationErrorZ.mjs';
import { Result_NoneSemanticErrorZ } from '../structs/Result_NoneSemanticErrorZ.mjs';
import { Result_InvoiceSemanticErrorZ } from '../structs/Result_InvoiceSemanticErrorZ.mjs';
import { Description } from '../structs/Description.mjs';
import { Result_DescriptionCreationErrorZ } from '../structs/Result_DescriptionCreationErrorZ.mjs';
import { Result_PrivateRouteCreationErrorZ } from '../structs/Result_PrivateRouteCreationErrorZ.mjs';
import { Result_NoneErrorZ } from '../structs/Result_NoneErrorZ.mjs';
import { Result_NetAddressDecodeErrorZ } from '../structs/Result_NetAddressDecodeErrorZ.mjs';
import { UpdateAddHTLC } from '../structs/UpdateAddHTLC.mjs';
import { UpdateFulfillHTLC } from '../structs/UpdateFulfillHTLC.mjs';
import { UpdateFailHTLC } from '../structs/UpdateFailHTLC.mjs';
import { UpdateFailMalformedHTLC } from '../structs/UpdateFailMalformedHTLC.mjs';
import { Result_AcceptChannelDecodeErrorZ } from '../structs/Result_AcceptChannelDecodeErrorZ.mjs';
import { Result_AnnouncementSignaturesDecodeErrorZ } from '../structs/Result_AnnouncementSignaturesDecodeErrorZ.mjs';
import { Result_ChannelReestablishDecodeErrorZ } from '../structs/Result_ChannelReestablishDecodeErrorZ.mjs';
import { Result_ClosingSignedDecodeErrorZ } from '../structs/Result_ClosingSignedDecodeErrorZ.mjs';
import { ClosingSignedFeeRange } from '../structs/ClosingSignedFeeRange.mjs';
import { Result_ClosingSignedFeeRangeDecodeErrorZ } from '../structs/Result_ClosingSignedFeeRangeDecodeErrorZ.mjs';
import { CommitmentSigned } from '../structs/CommitmentSigned.mjs';
import { Result_CommitmentSignedDecodeErrorZ } from '../structs/Result_CommitmentSignedDecodeErrorZ.mjs';
import { Result_FundingCreatedDecodeErrorZ } from '../structs/Result_FundingCreatedDecodeErrorZ.mjs';
import { Result_FundingSignedDecodeErrorZ } from '../structs/Result_FundingSignedDecodeErrorZ.mjs';
import { Result_ChannelReadyDecodeErrorZ } from '../structs/Result_ChannelReadyDecodeErrorZ.mjs';
import { Init } from '../structs/Init.mjs';
import { Result_InitDecodeErrorZ } from '../structs/Result_InitDecodeErrorZ.mjs';
import { Result_OpenChannelDecodeErrorZ } from '../structs/Result_OpenChannelDecodeErrorZ.mjs';
import { Result_RevokeAndACKDecodeErrorZ } from '../structs/Result_RevokeAndACKDecodeErrorZ.mjs';
import { Result_ShutdownDecodeErrorZ } from '../structs/Result_ShutdownDecodeErrorZ.mjs';
import { Result_UpdateFailHTLCDecodeErrorZ } from '../structs/Result_UpdateFailHTLCDecodeErrorZ.mjs';
import { Result_UpdateFailMalformedHTLCDecodeErrorZ } from '../structs/Result_UpdateFailMalformedHTLCDecodeErrorZ.mjs';
import { UpdateFee } from '../structs/UpdateFee.mjs';
import { Result_UpdateFeeDecodeErrorZ } from '../structs/Result_UpdateFeeDecodeErrorZ.mjs';
import { Result_UpdateFulfillHTLCDecodeErrorZ } from '../structs/Result_UpdateFulfillHTLCDecodeErrorZ.mjs';
import { Result_UpdateAddHTLCDecodeErrorZ } from '../structs/Result_UpdateAddHTLCDecodeErrorZ.mjs';
import { OnionMessage } from '../structs/OnionMessage.mjs';
import { Result_OnionMessageDecodeErrorZ } from '../structs/Result_OnionMessageDecodeErrorZ.mjs';
import { Ping } from '../structs/Ping.mjs';
import { Result_PingDecodeErrorZ } from '../structs/Result_PingDecodeErrorZ.mjs';
import { Pong } from '../structs/Pong.mjs';
import { Result_PongDecodeErrorZ } from '../structs/Result_PongDecodeErrorZ.mjs';
import { Result_UnsignedChannelAnnouncementDecodeErrorZ } from '../structs/Result_UnsignedChannelAnnouncementDecodeErrorZ.mjs';
import { Result_ChannelAnnouncementDecodeErrorZ } from '../structs/Result_ChannelAnnouncementDecodeErrorZ.mjs';
import { UnsignedChannelUpdate } from '../structs/UnsignedChannelUpdate.mjs';
import { Result_UnsignedChannelUpdateDecodeErrorZ } from '../structs/Result_UnsignedChannelUpdateDecodeErrorZ.mjs';
import { Result_ChannelUpdateDecodeErrorZ } from '../structs/Result_ChannelUpdateDecodeErrorZ.mjs';
import { Result_ErrorMessageDecodeErrorZ } from '../structs/Result_ErrorMessageDecodeErrorZ.mjs';
import { Result_WarningMessageDecodeErrorZ } from '../structs/Result_WarningMessageDecodeErrorZ.mjs';
import { UnsignedNodeAnnouncement } from '../structs/UnsignedNodeAnnouncement.mjs';
import { Result_UnsignedNodeAnnouncementDecodeErrorZ } from '../structs/Result_UnsignedNodeAnnouncementDecodeErrorZ.mjs';
import { NodeAnnouncement } from '../structs/NodeAnnouncement.mjs';
import { Result_NodeAnnouncementDecodeErrorZ } from '../structs/Result_NodeAnnouncementDecodeErrorZ.mjs';
import { Result_QueryShortChannelIdsDecodeErrorZ } from '../structs/Result_QueryShortChannelIdsDecodeErrorZ.mjs';
import { ReplyShortChannelIdsEnd } from '../structs/ReplyShortChannelIdsEnd.mjs';
import { Result_ReplyShortChannelIdsEndDecodeErrorZ } from '../structs/Result_ReplyShortChannelIdsEndDecodeErrorZ.mjs';
import { Result_QueryChannelRangeDecodeErrorZ } from '../structs/Result_QueryChannelRangeDecodeErrorZ.mjs';
import { Result_ReplyChannelRangeDecodeErrorZ } from '../structs/Result_ReplyChannelRangeDecodeErrorZ.mjs';
import { Result_GossipTimestampFilterDecodeErrorZ } from '../structs/Result_GossipTimestampFilterDecodeErrorZ.mjs';
import { SignOrCreationError } from '../structs/SignOrCreationError.mjs';
import { Result_InvoiceSignOrCreationErrorZ } from '../structs/Result_InvoiceSignOrCreationErrorZ.mjs';
import { WatchedOutput } from '../structs/WatchedOutput.mjs';
import { Filter, FilterInterface } from '../structs/Filter.mjs';
import { Option_FilterZ } from '../structs/Option_FilterZ.mjs';
import { LockedChannelMonitor } from '../structs/LockedChannelMonitor.mjs';
import { Result_LockedChannelMonitorNoneZ } from '../structs/Result_LockedChannelMonitorNoneZ.mjs';
import { MonitorUpdateId } from '../structs/MonitorUpdateId.mjs';
import { TwoTuple_OutPointCVec_MonitorUpdateIdZZ } from '../structs/TwoTuple_OutPointCVec_MonitorUpdateIdZZ.mjs';
import { MessageSendEventsProvider, MessageSendEventsProviderInterface } from '../structs/MessageSendEventsProvider.mjs';
import { OnionMessageProvider, OnionMessageProviderInterface } from '../structs/OnionMessageProvider.mjs';
import { EventHandler, EventHandlerInterface } from '../structs/EventHandler.mjs';
import { EventsProvider, EventsProviderInterface } from '../structs/EventsProvider.mjs';
import { BigSize } from '../structs/BigSize.mjs';
import { ChannelUsage } from '../structs/ChannelUsage.mjs';
import { Score, ScoreInterface } from '../structs/Score.mjs';
import { LockableScore, LockableScoreInterface } from '../structs/LockableScore.mjs';
import { WriteableScore, WriteableScoreInterface } from '../structs/WriteableScore.mjs';
import { Persister, PersisterInterface } from '../structs/Persister.mjs';
import { PrintableString } from '../structs/PrintableString.mjs';
import { FutureCallback, FutureCallbackInterface } from '../structs/FutureCallback.mjs';
import { Future } from '../structs/Future.mjs';
import { ChannelHandshakeConfig } from '../structs/ChannelHandshakeConfig.mjs';
import { ChannelHandshakeLimits } from '../structs/ChannelHandshakeLimits.mjs';
import { UserConfig } from '../structs/UserConfig.mjs';
import { BestBlock } from '../structs/BestBlock.mjs';
import { Listen, ListenInterface } from '../structs/Listen.mjs';
import { Confirm, ConfirmInterface } from '../structs/Confirm.mjs';
import { Persist, PersistInterface } from '../structs/Persist.mjs';
import { ChainMonitor } from '../structs/ChainMonitor.mjs';
import { KeysManager } from '../structs/KeysManager.mjs';
import { PhantomKeysManager } from '../structs/PhantomKeysManager.mjs';
import { ChainParameters } from '../structs/ChainParameters.mjs';
import { ChannelMessageHandler, ChannelMessageHandlerInterface } from '../structs/ChannelMessageHandler.mjs';
import { ChannelManagerReadArgs } from '../structs/ChannelManagerReadArgs.mjs';
import { ExpandedKey } from '../structs/ExpandedKey.mjs';
import { DataLossProtect } from '../structs/DataLossProtect.mjs';
import { RoutingMessageHandler, RoutingMessageHandlerInterface } from '../structs/RoutingMessageHandler.mjs';
import { OnionMessageHandler, OnionMessageHandlerInterface } from '../structs/OnionMessageHandler.mjs';
import { CustomMessageReader, CustomMessageReaderInterface } from '../structs/CustomMessageReader.mjs';
import { CustomMessageHandler, CustomMessageHandlerInterface } from '../structs/CustomMessageHandler.mjs';
import { IgnoringMessageHandler } from '../structs/IgnoringMessageHandler.mjs';
import { CustomOnionMessageHandler, CustomOnionMessageHandlerInterface } from '../structs/CustomOnionMessageHandler.mjs';
import { ErroringMessageHandler } from '../structs/ErroringMessageHandler.mjs';
import { MessageHandler } from '../structs/MessageHandler.mjs';
import { SocketDescriptor, SocketDescriptorInterface } from '../structs/SocketDescriptor.mjs';
import { PeerManager } from '../structs/PeerManager.mjs';
import { DirectedChannelTransactionParameters } from '../structs/DirectedChannelTransactionParameters.mjs';
import { ReadOnlyNetworkGraph } from '../structs/ReadOnlyNetworkGraph.mjs';
import { P2PGossipSync } from '../structs/P2PGossipSync.mjs';
import { DirectedChannelInfo } from '../structs/DirectedChannelInfo.mjs';
import { EffectiveCapacity } from '../structs/EffectiveCapacity.mjs';
import { DefaultRouter } from '../structs/DefaultRouter.mjs';
import { Router, RouterInterface } from '../structs/Router.mjs';
import { ScorerAccountingForInFlightHtlcs } from '../structs/ScorerAccountingForInFlightHtlcs.mjs';
import { MultiThreadedLockableScore } from '../structs/MultiThreadedLockableScore.mjs';
import { MultiThreadedScoreLock } from '../structs/MultiThreadedScoreLock.mjs';
import { ProbabilisticScoringParameters } from '../structs/ProbabilisticScoringParameters.mjs';
import { OnionMessenger } from '../structs/OnionMessenger.mjs';
import { Destination } from '../structs/Destination.mjs';
import { OnionMessageContents } from '../structs/OnionMessageContents.mjs';
import { RapidGossipSync } from '../structs/RapidGossipSync.mjs';
import { RawDataPart } from '../structs/RawDataPart.mjs';
import { Sha256 } from '../structs/Sha256.mjs';
import { ExpiryTime } from '../structs/ExpiryTime.mjs';
import { MinFinalCltvExpiry } from '../structs/MinFinalCltvExpiry.mjs';
import { Fallback } from '../structs/Fallback.mjs';
import { Payer, PayerInterface } from '../structs/Payer.mjs';
import { InvoicePayer } from '../structs/InvoicePayer.mjs';
import { Retry } from '../structs/Retry.mjs';

import { CommonBase, UInt5, WitnessVersion, UnqualifiedError } from './CommonBase.mjs';
import * as bindings from '../bindings.mjs'

/**
 * An Event which you should probably take some action in response to.
 * 
 * Note that while Writeable and Readable are implemented for Event, you probably shouldn't use
 * them directly as they don't round-trip exactly (for example FundingGenerationReady is never
 * written as it makes no sense to respond to it after reconnecting to peers).
 */
export class Event extends CommonBase {
	protected constructor(_dummy: null, ptr: bigint) { super(ptr, bindings.Event_free); }
	/* @internal */
	public static constr_from_ptr(ptr: bigint): Event {
		const raw_ty: number = bindings.LDKEvent_ty_from_ptr(ptr);
		switch (raw_ty) {
			case 0: return new Event_FundingGenerationReady(ptr);
			case 1: return new Event_PaymentClaimable(ptr);
			case 2: return new Event_PaymentClaimed(ptr);
			case 3: return new Event_PaymentSent(ptr);
			case 4: return new Event_PaymentFailed(ptr);
			case 5: return new Event_PaymentPathSuccessful(ptr);
			case 6: return new Event_PaymentPathFailed(ptr);
			case 7: return new Event_ProbeSuccessful(ptr);
			case 8: return new Event_ProbeFailed(ptr);
			case 9: return new Event_PendingHTLCsForwardable(ptr);
			case 10: return new Event_HTLCIntercepted(ptr);
			case 11: return new Event_SpendableOutputs(ptr);
			case 12: return new Event_PaymentForwarded(ptr);
			case 13: return new Event_ChannelReady(ptr);
			case 14: return new Event_ChannelClosed(ptr);
			case 15: return new Event_DiscardFunding(ptr);
			case 16: return new Event_OpenChannelRequest(ptr);
			case 17: return new Event_HTLCHandlingFailed(ptr);
			default:
				throw new Error('oops, this should be unreachable'); // Unreachable without extending the (internal) bindings interface
		}
	}

	public clone_ptr(): bigint {
		const ret: bigint = bindings.Event_clone_ptr(this.ptr);
		return ret;
	}

	/**
	 * Creates a copy of the Event
	 */
	public clone(): Event {
		const ret: bigint = bindings.Event_clone(this.ptr);
		const ret_hu_conv: Event = Event.constr_from_ptr(ret);
		CommonBase.add_ref_from(ret_hu_conv, this);
		return ret_hu_conv;
	}

	/**
	 * Utility method to constructs a new FundingGenerationReady-variant Event
	 */
	public static constructor_funding_generation_ready(temporary_channel_id: Uint8Array, counterparty_node_id: Uint8Array, channel_value_satoshis: bigint, output_script: Uint8Array, user_channel_id: bigint): Event {
		const ret: bigint = bindings.Event_funding_generation_ready(bindings.encodeUint8Array(bindings.check_arr_len(temporary_channel_id, 32)), bindings.encodeUint8Array(bindings.check_arr_len(counterparty_node_id, 33)), channel_value_satoshis, bindings.encodeUint8Array(output_script), bindings.encodeUint128(user_channel_id));
		const ret_hu_conv: Event = Event.constr_from_ptr(ret);
		CommonBase.add_ref_from(ret_hu_conv, ret_hu_conv);
		return ret_hu_conv;
	}

	/**
	 * Utility method to constructs a new PaymentClaimable-variant Event
	 */
	public static constructor_payment_claimable(receiver_node_id: Uint8Array, payment_hash: Uint8Array, amount_msat: bigint, purpose: PaymentPurpose, via_channel_id: Uint8Array, via_user_channel_id: Option_u128Z): Event {
		const ret: bigint = bindings.Event_payment_claimable(bindings.encodeUint8Array(bindings.check_arr_len(receiver_node_id, 33)), bindings.encodeUint8Array(bindings.check_arr_len(payment_hash, 32)), amount_msat, CommonBase.get_ptr_of(purpose), bindings.encodeUint8Array(bindings.check_arr_len(via_channel_id, 32)), CommonBase.get_ptr_of(via_user_channel_id));
		const ret_hu_conv: Event = Event.constr_from_ptr(ret);
		CommonBase.add_ref_from(ret_hu_conv, ret_hu_conv);
		return ret_hu_conv;
	}

	/**
	 * Utility method to constructs a new PaymentClaimed-variant Event
	 */
	public static constructor_payment_claimed(receiver_node_id: Uint8Array, payment_hash: Uint8Array, amount_msat: bigint, purpose: PaymentPurpose): Event {
		const ret: bigint = bindings.Event_payment_claimed(bindings.encodeUint8Array(bindings.check_arr_len(receiver_node_id, 33)), bindings.encodeUint8Array(bindings.check_arr_len(payment_hash, 32)), amount_msat, CommonBase.get_ptr_of(purpose));
		const ret_hu_conv: Event = Event.constr_from_ptr(ret);
		CommonBase.add_ref_from(ret_hu_conv, ret_hu_conv);
		return ret_hu_conv;
	}

	/**
	 * Utility method to constructs a new PaymentSent-variant Event
	 */
	public static constructor_payment_sent(payment_id: Uint8Array, payment_preimage: Uint8Array, payment_hash: Uint8Array, fee_paid_msat: Option_u64Z): Event {
		const ret: bigint = bindings.Event_payment_sent(bindings.encodeUint8Array(bindings.check_arr_len(payment_id, 32)), bindings.encodeUint8Array(bindings.check_arr_len(payment_preimage, 32)), bindings.encodeUint8Array(bindings.check_arr_len(payment_hash, 32)), CommonBase.get_ptr_of(fee_paid_msat));
		const ret_hu_conv: Event = Event.constr_from_ptr(ret);
		CommonBase.add_ref_from(ret_hu_conv, ret_hu_conv);
		return ret_hu_conv;
	}

	/**
	 * Utility method to constructs a new PaymentFailed-variant Event
	 */
	public static constructor_payment_failed(payment_id: Uint8Array, payment_hash: Uint8Array): Event {
		const ret: bigint = bindings.Event_payment_failed(bindings.encodeUint8Array(bindings.check_arr_len(payment_id, 32)), bindings.encodeUint8Array(bindings.check_arr_len(payment_hash, 32)));
		const ret_hu_conv: Event = Event.constr_from_ptr(ret);
		CommonBase.add_ref_from(ret_hu_conv, ret_hu_conv);
		return ret_hu_conv;
	}

	/**
	 * Utility method to constructs a new PaymentPathSuccessful-variant Event
	 */
	public static constructor_payment_path_successful(payment_id: Uint8Array, payment_hash: Uint8Array, path: RouteHop[]): Event {
		const ret: bigint = bindings.Event_payment_path_successful(bindings.encodeUint8Array(bindings.check_arr_len(payment_id, 32)), bindings.encodeUint8Array(bindings.check_arr_len(payment_hash, 32)), bindings.encodeUint64Array(path != null ? path.map(path_conv_10 => path_conv_10 == null ? 0n : CommonBase.get_ptr_of(path_conv_10)) : null));
		const ret_hu_conv: Event = Event.constr_from_ptr(ret);
		CommonBase.add_ref_from(ret_hu_conv, ret_hu_conv);
		path.forEach((path_conv_10: RouteHop) => { CommonBase.add_ref_from(ret_hu_conv, path_conv_10); });
		return ret_hu_conv;
	}

	/**
	 * Utility method to constructs a new PaymentPathFailed-variant Event
	 */
	public static constructor_payment_path_failed(payment_id: Uint8Array, payment_hash: Uint8Array, payment_failed_permanently: boolean, network_update: Option_NetworkUpdateZ, all_paths_failed: boolean, path: RouteHop[], short_channel_id: Option_u64Z, retry: RouteParameters): Event {
		const ret: bigint = bindings.Event_payment_path_failed(bindings.encodeUint8Array(bindings.check_arr_len(payment_id, 32)), bindings.encodeUint8Array(bindings.check_arr_len(payment_hash, 32)), payment_failed_permanently, CommonBase.get_ptr_of(network_update), all_paths_failed, bindings.encodeUint64Array(path != null ? path.map(path_conv_10 => path_conv_10 == null ? 0n : CommonBase.get_ptr_of(path_conv_10)) : null), CommonBase.get_ptr_of(short_channel_id), retry == null ? 0n : CommonBase.get_ptr_of(retry));
		const ret_hu_conv: Event = Event.constr_from_ptr(ret);
		CommonBase.add_ref_from(ret_hu_conv, ret_hu_conv);
		path.forEach((path_conv_10: RouteHop) => { CommonBase.add_ref_from(ret_hu_conv, path_conv_10); });
		CommonBase.add_ref_from(ret_hu_conv, retry);
		return ret_hu_conv;
	}

	/**
	 * Utility method to constructs a new ProbeSuccessful-variant Event
	 */
	public static constructor_probe_successful(payment_id: Uint8Array, payment_hash: Uint8Array, path: RouteHop[]): Event {
		const ret: bigint = bindings.Event_probe_successful(bindings.encodeUint8Array(bindings.check_arr_len(payment_id, 32)), bindings.encodeUint8Array(bindings.check_arr_len(payment_hash, 32)), bindings.encodeUint64Array(path != null ? path.map(path_conv_10 => path_conv_10 == null ? 0n : CommonBase.get_ptr_of(path_conv_10)) : null));
		const ret_hu_conv: Event = Event.constr_from_ptr(ret);
		CommonBase.add_ref_from(ret_hu_conv, ret_hu_conv);
		path.forEach((path_conv_10: RouteHop) => { CommonBase.add_ref_from(ret_hu_conv, path_conv_10); });
		return ret_hu_conv;
	}

	/**
	 * Utility method to constructs a new ProbeFailed-variant Event
	 */
	public static constructor_probe_failed(payment_id: Uint8Array, payment_hash: Uint8Array, path: RouteHop[], short_channel_id: Option_u64Z): Event {
		const ret: bigint = bindings.Event_probe_failed(bindings.encodeUint8Array(bindings.check_arr_len(payment_id, 32)), bindings.encodeUint8Array(bindings.check_arr_len(payment_hash, 32)), bindings.encodeUint64Array(path != null ? path.map(path_conv_10 => path_conv_10 == null ? 0n : CommonBase.get_ptr_of(path_conv_10)) : null), CommonBase.get_ptr_of(short_channel_id));
		const ret_hu_conv: Event = Event.constr_from_ptr(ret);
		CommonBase.add_ref_from(ret_hu_conv, ret_hu_conv);
		path.forEach((path_conv_10: RouteHop) => { CommonBase.add_ref_from(ret_hu_conv, path_conv_10); });
		return ret_hu_conv;
	}

	/**
	 * Utility method to constructs a new PendingHTLCsForwardable-variant Event
	 */
	public static constructor_pending_htlcs_forwardable(time_forwardable: bigint): Event {
		const ret: bigint = bindings.Event_pending_htlcs_forwardable(time_forwardable);
		const ret_hu_conv: Event = Event.constr_from_ptr(ret);
		CommonBase.add_ref_from(ret_hu_conv, ret_hu_conv);
		return ret_hu_conv;
	}

	/**
	 * Utility method to constructs a new HTLCIntercepted-variant Event
	 */
	public static constructor_htlcintercepted(intercept_id: Uint8Array, requested_next_hop_scid: bigint, payment_hash: Uint8Array, inbound_amount_msat: bigint, expected_outbound_amount_msat: bigint): Event {
		const ret: bigint = bindings.Event_htlcintercepted(bindings.encodeUint8Array(bindings.check_arr_len(intercept_id, 32)), requested_next_hop_scid, bindings.encodeUint8Array(bindings.check_arr_len(payment_hash, 32)), inbound_amount_msat, expected_outbound_amount_msat);
		const ret_hu_conv: Event = Event.constr_from_ptr(ret);
		CommonBase.add_ref_from(ret_hu_conv, ret_hu_conv);
		return ret_hu_conv;
	}

	/**
	 * Utility method to constructs a new SpendableOutputs-variant Event
	 */
	public static constructor_spendable_outputs(outputs: SpendableOutputDescriptor[]): Event {
		const ret: bigint = bindings.Event_spendable_outputs(bindings.encodeUint64Array(outputs != null ? outputs.map(outputs_conv_27 => CommonBase.get_ptr_of(outputs_conv_27)) : null));
		const ret_hu_conv: Event = Event.constr_from_ptr(ret);
		CommonBase.add_ref_from(ret_hu_conv, ret_hu_conv);
		return ret_hu_conv;
	}

	/**
	 * Utility method to constructs a new PaymentForwarded-variant Event
	 */
	public static constructor_payment_forwarded(prev_channel_id: Uint8Array, next_channel_id: Uint8Array, fee_earned_msat: Option_u64Z, claim_from_onchain_tx: boolean): Event {
		const ret: bigint = bindings.Event_payment_forwarded(bindings.encodeUint8Array(bindings.check_arr_len(prev_channel_id, 32)), bindings.encodeUint8Array(bindings.check_arr_len(next_channel_id, 32)), CommonBase.get_ptr_of(fee_earned_msat), claim_from_onchain_tx);
		const ret_hu_conv: Event = Event.constr_from_ptr(ret);
		CommonBase.add_ref_from(ret_hu_conv, ret_hu_conv);
		return ret_hu_conv;
	}

	/**
	 * Utility method to constructs a new ChannelReady-variant Event
	 */
	public static constructor_channel_ready(channel_id: Uint8Array, user_channel_id: bigint, counterparty_node_id: Uint8Array, channel_type: ChannelTypeFeatures): Event {
		const ret: bigint = bindings.Event_channel_ready(bindings.encodeUint8Array(bindings.check_arr_len(channel_id, 32)), bindings.encodeUint128(user_channel_id), bindings.encodeUint8Array(bindings.check_arr_len(counterparty_node_id, 33)), channel_type == null ? 0n : CommonBase.get_ptr_of(channel_type));
		const ret_hu_conv: Event = Event.constr_from_ptr(ret);
		CommonBase.add_ref_from(ret_hu_conv, ret_hu_conv);
		CommonBase.add_ref_from(ret_hu_conv, channel_type);
		return ret_hu_conv;
	}

	/**
	 * Utility method to constructs a new ChannelClosed-variant Event
	 */
	public static constructor_channel_closed(channel_id: Uint8Array, user_channel_id: bigint, reason: ClosureReason): Event {
		const ret: bigint = bindings.Event_channel_closed(bindings.encodeUint8Array(bindings.check_arr_len(channel_id, 32)), bindings.encodeUint128(user_channel_id), CommonBase.get_ptr_of(reason));
		const ret_hu_conv: Event = Event.constr_from_ptr(ret);
		CommonBase.add_ref_from(ret_hu_conv, ret_hu_conv);
		return ret_hu_conv;
	}

	/**
	 * Utility method to constructs a new DiscardFunding-variant Event
	 */
	public static constructor_discard_funding(channel_id: Uint8Array, transaction: Uint8Array): Event {
		const ret: bigint = bindings.Event_discard_funding(bindings.encodeUint8Array(bindings.check_arr_len(channel_id, 32)), bindings.encodeUint8Array(transaction));
		const ret_hu_conv: Event = Event.constr_from_ptr(ret);
		CommonBase.add_ref_from(ret_hu_conv, ret_hu_conv);
		return ret_hu_conv;
	}

	/**
	 * Utility method to constructs a new OpenChannelRequest-variant Event
	 */
	public static constructor_open_channel_request(temporary_channel_id: Uint8Array, counterparty_node_id: Uint8Array, funding_satoshis: bigint, push_msat: bigint, channel_type: ChannelTypeFeatures): Event {
		const ret: bigint = bindings.Event_open_channel_request(bindings.encodeUint8Array(bindings.check_arr_len(temporary_channel_id, 32)), bindings.encodeUint8Array(bindings.check_arr_len(counterparty_node_id, 33)), funding_satoshis, push_msat, channel_type == null ? 0n : CommonBase.get_ptr_of(channel_type));
		const ret_hu_conv: Event = Event.constr_from_ptr(ret);
		CommonBase.add_ref_from(ret_hu_conv, ret_hu_conv);
		CommonBase.add_ref_from(ret_hu_conv, channel_type);
		return ret_hu_conv;
	}

	/**
	 * Utility method to constructs a new HTLCHandlingFailed-variant Event
	 */
	public static constructor_htlchandling_failed(prev_channel_id: Uint8Array, failed_next_destination: HTLCDestination): Event {
		const ret: bigint = bindings.Event_htlchandling_failed(bindings.encodeUint8Array(bindings.check_arr_len(prev_channel_id, 32)), CommonBase.get_ptr_of(failed_next_destination));
		const ret_hu_conv: Event = Event.constr_from_ptr(ret);
		CommonBase.add_ref_from(ret_hu_conv, ret_hu_conv);
		return ret_hu_conv;
	}

	/**
	 * Serialize the Event object into a byte array which can be read by Event_read
	 */
	public write(): Uint8Array {
		const ret: number = bindings.Event_write(this.ptr);
		const ret_conv: Uint8Array = bindings.decodeUint8Array(ret);
		return ret_conv;
	}

}
/** A Event of type FundingGenerationReady */
export class Event_FundingGenerationReady extends Event {
	/**
	 * The random channel_id we picked which you'll need to pass into
	 * [`ChannelManager::funding_transaction_generated`].
	 * 
	 * [`ChannelManager::funding_transaction_generated`]: crate::ln::channelmanager::ChannelManager::funding_transaction_generated
	 */
	public temporary_channel_id: Uint8Array;
	/**
	 * The counterparty's node_id, which you'll need to pass back into
	 * [`ChannelManager::funding_transaction_generated`].
	 * 
	 * [`ChannelManager::funding_transaction_generated`]: crate::ln::channelmanager::ChannelManager::funding_transaction_generated
	 */
	public counterparty_node_id: Uint8Array;
	/**
	 * The value, in satoshis, that the output should have.
	 */
	public channel_value_satoshis: bigint;
	/**
	 * The script which should be used in the transaction output.
	 */
	public output_script: Uint8Array;
	/**
	 * The `user_channel_id` value passed in to [`ChannelManager::create_channel`], or a
	 * random value for an inbound channel. This may be zero for objects serialized with LDK
	 * versions prior to 0.0.113.
	 * 
	 * [`ChannelManager::create_channel`]: crate::ln::channelmanager::ChannelManager::create_channel
	 */
	public user_channel_id: bigint;
	/* @internal */
	public constructor(ptr: bigint) {
		super(null, ptr);
		const temporary_channel_id: number = bindings.LDKEvent_FundingGenerationReady_get_temporary_channel_id(ptr);
		const temporary_channel_id_conv: Uint8Array = bindings.decodeUint8Array(temporary_channel_id);
		this.temporary_channel_id = temporary_channel_id_conv;
		const counterparty_node_id: number = bindings.LDKEvent_FundingGenerationReady_get_counterparty_node_id(ptr);
		const counterparty_node_id_conv: Uint8Array = bindings.decodeUint8Array(counterparty_node_id);
		this.counterparty_node_id = counterparty_node_id_conv;
		this.channel_value_satoshis = bindings.LDKEvent_FundingGenerationReady_get_channel_value_satoshis(ptr);
		const output_script: number = bindings.LDKEvent_FundingGenerationReady_get_output_script(ptr);
		const output_script_conv: Uint8Array = bindings.decodeUint8Array(output_script);
		this.output_script = output_script_conv;
		const user_channel_id: number = bindings.LDKEvent_FundingGenerationReady_get_user_channel_id(ptr);
		const user_channel_id_conv: bigint = bindings.decodeUint128(user_channel_id);
		this.user_channel_id = user_channel_id_conv;
	}
}
/** A Event of type PaymentClaimable */
export class Event_PaymentClaimable extends Event {
	/**
	 * The node that will receive the payment after it has been claimed.
	 * This is useful to identify payments received via [phantom nodes].
	 * This field will always be filled in when the event was generated by LDK versions
	 * 0.0.113 and above.
	 * 
	 * [phantom nodes]: crate::chain::keysinterface::PhantomKeysManager
	 * 
	 * Note that this (or a relevant inner pointer) may be NULL or all-0s to represent None
	 */
	public receiver_node_id: Uint8Array;
	/**
	 * The hash for which the preimage should be handed to the ChannelManager. Note that LDK will
	 * not stop you from registering duplicate payment hashes for inbound payments.
	 */
	public payment_hash: Uint8Array;
	/**
	 * The value, in thousandths of a satoshi, that this payment is for.
	 */
	public amount_msat: bigint;
	/**
	 * Information for claiming this received payment, based on whether the purpose of the
	 * payment is to pay an invoice or to send a spontaneous payment.
	 */
	public purpose: PaymentPurpose;
	/**
	 * The `channel_id` indicating over which channel we received the payment.
	 * 
	 * Note that this (or a relevant inner pointer) may be NULL or all-0s to represent None
	 */
	public via_channel_id: Uint8Array;
	/**
	 * The `user_channel_id` indicating over which channel we received the payment.
	 */
	public via_user_channel_id: Option_u128Z;
	/* @internal */
	public constructor(ptr: bigint) {
		super(null, ptr);
		const receiver_node_id: number = bindings.LDKEvent_PaymentClaimable_get_receiver_node_id(ptr);
		const receiver_node_id_conv: Uint8Array = bindings.decodeUint8Array(receiver_node_id);
		this.receiver_node_id = receiver_node_id_conv;
		const payment_hash: number = bindings.LDKEvent_PaymentClaimable_get_payment_hash(ptr);
		const payment_hash_conv: Uint8Array = bindings.decodeUint8Array(payment_hash);
		this.payment_hash = payment_hash_conv;
		this.amount_msat = bindings.LDKEvent_PaymentClaimable_get_amount_msat(ptr);
		const purpose: bigint = bindings.LDKEvent_PaymentClaimable_get_purpose(ptr);
		const purpose_hu_conv: PaymentPurpose = PaymentPurpose.constr_from_ptr(purpose);
			CommonBase.add_ref_from(purpose_hu_conv, this);
		this.purpose = purpose_hu_conv;
		const via_channel_id: number = bindings.LDKEvent_PaymentClaimable_get_via_channel_id(ptr);
		const via_channel_id_conv: Uint8Array = bindings.decodeUint8Array(via_channel_id);
		this.via_channel_id = via_channel_id_conv;
		const via_user_channel_id: bigint = bindings.LDKEvent_PaymentClaimable_get_via_user_channel_id(ptr);
		const via_user_channel_id_hu_conv: Option_u128Z = Option_u128Z.constr_from_ptr(via_user_channel_id);
			CommonBase.add_ref_from(via_user_channel_id_hu_conv, this);
		this.via_user_channel_id = via_user_channel_id_hu_conv;
	}
}
/** A Event of type PaymentClaimed */
export class Event_PaymentClaimed extends Event {
	/**
	 * The node that received the payment.
	 * This is useful to identify payments which were received via [phantom nodes].
	 * This field will always be filled in when the event was generated by LDK versions
	 * 0.0.113 and above.
	 * 
	 * [phantom nodes]: crate::chain::keysinterface::PhantomKeysManager
	 * 
	 * Note that this (or a relevant inner pointer) may be NULL or all-0s to represent None
	 */
	public receiver_node_id: Uint8Array;
	/**
	 * The payment hash of the claimed payment. Note that LDK will not stop you from
	 * registering duplicate payment hashes for inbound payments.
	 */
	public payment_hash: Uint8Array;
	/**
	 * The value, in thousandths of a satoshi, that this payment is for.
	 */
	public amount_msat: bigint;
	/**
	 * The purpose of the claimed payment, i.e. whether the payment was for an invoice or a
	 * spontaneous payment.
	 */
	public purpose: PaymentPurpose;
	/* @internal */
	public constructor(ptr: bigint) {
		super(null, ptr);
		const receiver_node_id: number = bindings.LDKEvent_PaymentClaimed_get_receiver_node_id(ptr);
		const receiver_node_id_conv: Uint8Array = bindings.decodeUint8Array(receiver_node_id);
		this.receiver_node_id = receiver_node_id_conv;
		const payment_hash: number = bindings.LDKEvent_PaymentClaimed_get_payment_hash(ptr);
		const payment_hash_conv: Uint8Array = bindings.decodeUint8Array(payment_hash);
		this.payment_hash = payment_hash_conv;
		this.amount_msat = bindings.LDKEvent_PaymentClaimed_get_amount_msat(ptr);
		const purpose: bigint = bindings.LDKEvent_PaymentClaimed_get_purpose(ptr);
		const purpose_hu_conv: PaymentPurpose = PaymentPurpose.constr_from_ptr(purpose);
			CommonBase.add_ref_from(purpose_hu_conv, this);
		this.purpose = purpose_hu_conv;
	}
}
/** A Event of type PaymentSent */
export class Event_PaymentSent extends Event {
	/**
	 * The id returned by [`ChannelManager::send_payment`] and used with
	 * [`ChannelManager::retry_payment`].
	 * 
	 * [`ChannelManager::send_payment`]: crate::ln::channelmanager::ChannelManager::send_payment
	 * [`ChannelManager::retry_payment`]: crate::ln::channelmanager::ChannelManager::retry_payment
	 * 
	 * Note that this (or a relevant inner pointer) may be NULL or all-0s to represent None
	 */
	public payment_id: Uint8Array;
	/**
	 * The preimage to the hash given to ChannelManager::send_payment.
	 * Note that this serves as a payment receipt, if you wish to have such a thing, you must
	 * store it somehow!
	 */
	public payment_preimage: Uint8Array;
	/**
	 * The hash that was given to [`ChannelManager::send_payment`].
	 * 
	 * [`ChannelManager::send_payment`]: crate::ln::channelmanager::ChannelManager::send_payment
	 */
	public payment_hash: Uint8Array;
	/**
	 * The total fee which was spent at intermediate hops in this payment, across all paths.
	 * 
	 * Note that, like [`Route::get_total_fees`] this does *not* include any potential
	 * overpayment to the recipient node.
	 * 
	 * If the recipient or an intermediate node misbehaves and gives us free money, this may
	 * overstate the amount paid, though this is unlikely.
	 * 
	 * [`Route::get_total_fees`]: crate::routing::router::Route::get_total_fees
	 */
	public fee_paid_msat: Option_u64Z;
	/* @internal */
	public constructor(ptr: bigint) {
		super(null, ptr);
		const payment_id: number = bindings.LDKEvent_PaymentSent_get_payment_id(ptr);
		const payment_id_conv: Uint8Array = bindings.decodeUint8Array(payment_id);
		this.payment_id = payment_id_conv;
		const payment_preimage: number = bindings.LDKEvent_PaymentSent_get_payment_preimage(ptr);
		const payment_preimage_conv: Uint8Array = bindings.decodeUint8Array(payment_preimage);
		this.payment_preimage = payment_preimage_conv;
		const payment_hash: number = bindings.LDKEvent_PaymentSent_get_payment_hash(ptr);
		const payment_hash_conv: Uint8Array = bindings.decodeUint8Array(payment_hash);
		this.payment_hash = payment_hash_conv;
		const fee_paid_msat: bigint = bindings.LDKEvent_PaymentSent_get_fee_paid_msat(ptr);
		const fee_paid_msat_hu_conv: Option_u64Z = Option_u64Z.constr_from_ptr(fee_paid_msat);
			CommonBase.add_ref_from(fee_paid_msat_hu_conv, this);
		this.fee_paid_msat = fee_paid_msat_hu_conv;
	}
}
/** A Event of type PaymentFailed */
export class Event_PaymentFailed extends Event {
	/**
	 * The id returned by [`ChannelManager::send_payment`] and used with
	 * [`ChannelManager::retry_payment`] and [`ChannelManager::abandon_payment`].
	 * 
	 * [`ChannelManager::send_payment`]: crate::ln::channelmanager::ChannelManager::send_payment
	 * [`ChannelManager::retry_payment`]: crate::ln::channelmanager::ChannelManager::retry_payment
	 * [`ChannelManager::abandon_payment`]: crate::ln::channelmanager::ChannelManager::abandon_payment
	 */
	public payment_id: Uint8Array;
	/**
	 * The hash that was given to [`ChannelManager::send_payment`].
	 * 
	 * [`ChannelManager::send_payment`]: crate::ln::channelmanager::ChannelManager::send_payment
	 */
	public payment_hash: Uint8Array;
	/* @internal */
	public constructor(ptr: bigint) {
		super(null, ptr);
		const payment_id: number = bindings.LDKEvent_PaymentFailed_get_payment_id(ptr);
		const payment_id_conv: Uint8Array = bindings.decodeUint8Array(payment_id);
		this.payment_id = payment_id_conv;
		const payment_hash: number = bindings.LDKEvent_PaymentFailed_get_payment_hash(ptr);
		const payment_hash_conv: Uint8Array = bindings.decodeUint8Array(payment_hash);
		this.payment_hash = payment_hash_conv;
	}
}
/** A Event of type PaymentPathSuccessful */
export class Event_PaymentPathSuccessful extends Event {
	/**
	 * The id returned by [`ChannelManager::send_payment`] and used with
	 * [`ChannelManager::retry_payment`].
	 * 
	 * [`ChannelManager::send_payment`]: crate::ln::channelmanager::ChannelManager::send_payment
	 * [`ChannelManager::retry_payment`]: crate::ln::channelmanager::ChannelManager::retry_payment
	 */
	public payment_id: Uint8Array;
	/**
	 * The hash that was given to [`ChannelManager::send_payment`].
	 * 
	 * [`ChannelManager::send_payment`]: crate::ln::channelmanager::ChannelManager::send_payment
	 * 
	 * Note that this (or a relevant inner pointer) may be NULL or all-0s to represent None
	 */
	public payment_hash: Uint8Array;
	/**
	 * The payment path that was successful.
	 * 
	 * May contain a closed channel if the HTLC sent along the path was fulfilled on chain.
	 */
	public path: RouteHop[];
	/* @internal */
	public constructor(ptr: bigint) {
		super(null, ptr);
		const payment_id: number = bindings.LDKEvent_PaymentPathSuccessful_get_payment_id(ptr);
		const payment_id_conv: Uint8Array = bindings.decodeUint8Array(payment_id);
		this.payment_id = payment_id_conv;
		const payment_hash: number = bindings.LDKEvent_PaymentPathSuccessful_get_payment_hash(ptr);
		const payment_hash_conv: Uint8Array = bindings.decodeUint8Array(payment_hash);
		this.payment_hash = payment_hash_conv;
		const path: number = bindings.LDKEvent_PaymentPathSuccessful_get_path(ptr);
		const path_conv_10_len: number = bindings.getArrayLength(path);
			const path_conv_10_arr: RouteHop[] = new Array(path_conv_10_len).fill(null);
			for (var k = 0; k < path_conv_10_len; k++) {
				const path_conv_10: bigint = bindings.getU64ArrayElem(path, k);
				const path_conv_10_hu_conv: RouteHop = new RouteHop(null, path_conv_10);
				CommonBase.add_ref_from(path_conv_10_hu_conv, this);
				path_conv_10_arr[k] = path_conv_10_hu_conv;
			}
			bindings.freeWasmMemory(path)
		this.path = path_conv_10_arr;
	}
}
/** A Event of type PaymentPathFailed */
export class Event_PaymentPathFailed extends Event {
	/**
	 * The id returned by [`ChannelManager::send_payment`] and used with
	 * [`ChannelManager::retry_payment`] and [`ChannelManager::abandon_payment`].
	 * 
	 * [`ChannelManager::send_payment`]: crate::ln::channelmanager::ChannelManager::send_payment
	 * [`ChannelManager::retry_payment`]: crate::ln::channelmanager::ChannelManager::retry_payment
	 * [`ChannelManager::abandon_payment`]: crate::ln::channelmanager::ChannelManager::abandon_payment
	 * 
	 * Note that this (or a relevant inner pointer) may be NULL or all-0s to represent None
	 */
	public payment_id: Uint8Array;
	/**
	 * The hash that was given to [`ChannelManager::send_payment`].
	 * 
	 * [`ChannelManager::send_payment`]: crate::ln::channelmanager::ChannelManager::send_payment
	 */
	public payment_hash: Uint8Array;
	/**
	 * Indicates the payment was rejected for some reason by the recipient. This implies that
	 * the payment has failed, not just the route in question. If this is not set, you may
	 * retry the payment via a different route.
	 */
	public payment_failed_permanently: boolean;
	/**
	 * Any failure information conveyed via the Onion return packet by a node along the failed
	 * payment route.
	 * 
	 * Should be applied to the [`NetworkGraph`] so that routing decisions can take into
	 * account the update.
	 * 
	 * [`NetworkGraph`]: crate::routing::gossip::NetworkGraph
	 */
	public network_update: Option_NetworkUpdateZ;
	/**
	 * For both single-path and multi-path payments, this is set if all paths of the payment have
	 * failed. This will be set to false if (1) this is an MPP payment and (2) other parts of the
	 * larger MPP payment were still in flight when this event was generated.
	 * 
	 * Note that if you are retrying individual MPP parts, using this value to determine if a
	 * payment has fully failed is race-y. Because multiple failures can happen prior to events
	 * being processed, you may retry in response to a first failure, with a second failure
	 * (with `all_paths_failed` set) still pending. Then, when the second failure is processed
	 * you will see `all_paths_failed` set even though the retry of the first failure still
	 * has an associated in-flight HTLC. See (1) for an example of such a failure.
	 * 
	 * If you wish to retry individual MPP parts and learn when a payment has failed, you must
	 * call [`ChannelManager::abandon_payment`] and wait for a [`Event::PaymentFailed`] event.
	 * 
	 * (1) <https://github.com/lightningdevkit/rust-lightning/issues/1164>
	 * 
	 * [`ChannelManager::abandon_payment`]: crate::ln::channelmanager::ChannelManager::abandon_payment
	 */
	public all_paths_failed: boolean;
	/**
	 * The payment path that failed.
	 */
	public path: RouteHop[];
	/**
	 * The channel responsible for the failed payment path.
	 * 
	 * Note that for route hints or for the first hop in a path this may be an SCID alias and
	 * may not refer to a channel in the public network graph. These aliases may also collide
	 * with channels in the public network graph.
	 * 
	 * If this is `Some`, then the corresponding channel should be avoided when the payment is
	 * retried. May be `None` for older [`Event`] serializations.
	 */
	public short_channel_id: Option_u64Z;
	/**
	 * Parameters needed to compute a new [`Route`] when retrying the failed payment path.
	 * 
	 * See [`find_route`] for details.
	 * 
	 * [`Route`]: crate::routing::router::Route
	 * [`find_route`]: crate::routing::router::find_route
	 * 
	 * Note that this (or a relevant inner pointer) may be NULL or all-0s to represent None
	 */
	public retry: RouteParameters;
	/* @internal */
	public constructor(ptr: bigint) {
		super(null, ptr);
		const payment_id: number = bindings.LDKEvent_PaymentPathFailed_get_payment_id(ptr);
		const payment_id_conv: Uint8Array = bindings.decodeUint8Array(payment_id);
		this.payment_id = payment_id_conv;
		const payment_hash: number = bindings.LDKEvent_PaymentPathFailed_get_payment_hash(ptr);
		const payment_hash_conv: Uint8Array = bindings.decodeUint8Array(payment_hash);
		this.payment_hash = payment_hash_conv;
		this.payment_failed_permanently = bindings.LDKEvent_PaymentPathFailed_get_payment_failed_permanently(ptr);
		const network_update: bigint = bindings.LDKEvent_PaymentPathFailed_get_network_update(ptr);
		const network_update_hu_conv: Option_NetworkUpdateZ = Option_NetworkUpdateZ.constr_from_ptr(network_update);
			CommonBase.add_ref_from(network_update_hu_conv, this);
		this.network_update = network_update_hu_conv;
		this.all_paths_failed = bindings.LDKEvent_PaymentPathFailed_get_all_paths_failed(ptr);
		const path: number = bindings.LDKEvent_PaymentPathFailed_get_path(ptr);
		const path_conv_10_len: number = bindings.getArrayLength(path);
			const path_conv_10_arr: RouteHop[] = new Array(path_conv_10_len).fill(null);
			for (var k = 0; k < path_conv_10_len; k++) {
				const path_conv_10: bigint = bindings.getU64ArrayElem(path, k);
				const path_conv_10_hu_conv: RouteHop = new RouteHop(null, path_conv_10);
				CommonBase.add_ref_from(path_conv_10_hu_conv, this);
				path_conv_10_arr[k] = path_conv_10_hu_conv;
			}
			bindings.freeWasmMemory(path)
		this.path = path_conv_10_arr;
		const short_channel_id: bigint = bindings.LDKEvent_PaymentPathFailed_get_short_channel_id(ptr);
		const short_channel_id_hu_conv: Option_u64Z = Option_u64Z.constr_from_ptr(short_channel_id);
			CommonBase.add_ref_from(short_channel_id_hu_conv, this);
		this.short_channel_id = short_channel_id_hu_conv;
		const retry: bigint = bindings.LDKEvent_PaymentPathFailed_get_retry(ptr);
		const retry_hu_conv: RouteParameters = new RouteParameters(null, retry);
			CommonBase.add_ref_from(retry_hu_conv, this);
		this.retry = retry_hu_conv;
	}
}
/** A Event of type ProbeSuccessful */
export class Event_ProbeSuccessful extends Event {
	/**
	 * The id returned by [`ChannelManager::send_probe`].
	 * 
	 * [`ChannelManager::send_probe`]: crate::ln::channelmanager::ChannelManager::send_probe
	 */
	public payment_id: Uint8Array;
	/**
	 * The hash generated by [`ChannelManager::send_probe`].
	 * 
	 * [`ChannelManager::send_probe`]: crate::ln::channelmanager::ChannelManager::send_probe
	 */
	public payment_hash: Uint8Array;
	/**
	 * The payment path that was successful.
	 */
	public path: RouteHop[];
	/* @internal */
	public constructor(ptr: bigint) {
		super(null, ptr);
		const payment_id: number = bindings.LDKEvent_ProbeSuccessful_get_payment_id(ptr);
		const payment_id_conv: Uint8Array = bindings.decodeUint8Array(payment_id);
		this.payment_id = payment_id_conv;
		const payment_hash: number = bindings.LDKEvent_ProbeSuccessful_get_payment_hash(ptr);
		const payment_hash_conv: Uint8Array = bindings.decodeUint8Array(payment_hash);
		this.payment_hash = payment_hash_conv;
		const path: number = bindings.LDKEvent_ProbeSuccessful_get_path(ptr);
		const path_conv_10_len: number = bindings.getArrayLength(path);
			const path_conv_10_arr: RouteHop[] = new Array(path_conv_10_len).fill(null);
			for (var k = 0; k < path_conv_10_len; k++) {
				const path_conv_10: bigint = bindings.getU64ArrayElem(path, k);
				const path_conv_10_hu_conv: RouteHop = new RouteHop(null, path_conv_10);
				CommonBase.add_ref_from(path_conv_10_hu_conv, this);
				path_conv_10_arr[k] = path_conv_10_hu_conv;
			}
			bindings.freeWasmMemory(path)
		this.path = path_conv_10_arr;
	}
}
/** A Event of type ProbeFailed */
export class Event_ProbeFailed extends Event {
	/**
	 * The id returned by [`ChannelManager::send_probe`].
	 * 
	 * [`ChannelManager::send_probe`]: crate::ln::channelmanager::ChannelManager::send_probe
	 */
	public payment_id: Uint8Array;
	/**
	 * The hash generated by [`ChannelManager::send_probe`].
	 * 
	 * [`ChannelManager::send_probe`]: crate::ln::channelmanager::ChannelManager::send_probe
	 */
	public payment_hash: Uint8Array;
	/**
	 * The payment path that failed.
	 */
	public path: RouteHop[];
	/**
	 * The channel responsible for the failed probe.
	 * 
	 * Note that for route hints or for the first hop in a path this may be an SCID alias and
	 * may not refer to a channel in the public network graph. These aliases may also collide
	 * with channels in the public network graph.
	 */
	public short_channel_id: Option_u64Z;
	/* @internal */
	public constructor(ptr: bigint) {
		super(null, ptr);
		const payment_id: number = bindings.LDKEvent_ProbeFailed_get_payment_id(ptr);
		const payment_id_conv: Uint8Array = bindings.decodeUint8Array(payment_id);
		this.payment_id = payment_id_conv;
		const payment_hash: number = bindings.LDKEvent_ProbeFailed_get_payment_hash(ptr);
		const payment_hash_conv: Uint8Array = bindings.decodeUint8Array(payment_hash);
		this.payment_hash = payment_hash_conv;
		const path: number = bindings.LDKEvent_ProbeFailed_get_path(ptr);
		const path_conv_10_len: number = bindings.getArrayLength(path);
			const path_conv_10_arr: RouteHop[] = new Array(path_conv_10_len).fill(null);
			for (var k = 0; k < path_conv_10_len; k++) {
				const path_conv_10: bigint = bindings.getU64ArrayElem(path, k);
				const path_conv_10_hu_conv: RouteHop = new RouteHop(null, path_conv_10);
				CommonBase.add_ref_from(path_conv_10_hu_conv, this);
				path_conv_10_arr[k] = path_conv_10_hu_conv;
			}
			bindings.freeWasmMemory(path)
		this.path = path_conv_10_arr;
		const short_channel_id: bigint = bindings.LDKEvent_ProbeFailed_get_short_channel_id(ptr);
		const short_channel_id_hu_conv: Option_u64Z = Option_u64Z.constr_from_ptr(short_channel_id);
			CommonBase.add_ref_from(short_channel_id_hu_conv, this);
		this.short_channel_id = short_channel_id_hu_conv;
	}
}
/** A Event of type PendingHTLCsForwardable */
export class Event_PendingHTLCsForwardable extends Event {
	/**
	 * The minimum amount of time that should be waited prior to calling
	 * process_pending_htlc_forwards. To increase the effort required to correlate payments,
	 * you should wait a random amount of time in roughly the range (now + time_forwardable,
	 * now + 5*time_forwardable).
	 */
	public time_forwardable: bigint;
	/* @internal */
	public constructor(ptr: bigint) {
		super(null, ptr);
		this.time_forwardable = bindings.LDKEvent_PendingHTLCsForwardable_get_time_forwardable(ptr);
	}
}
/** A Event of type HTLCIntercepted */
export class Event_HTLCIntercepted extends Event {
	/**
	 * An id to help LDK identify which HTLC is being forwarded or failed.
	 */
	public intercept_id: Uint8Array;
	/**
	 * The fake scid that was programmed as the next hop's scid, generated using
	 * [`ChannelManager::get_intercept_scid`].
	 * 
	 * [`ChannelManager::get_intercept_scid`]: crate::ln::channelmanager::ChannelManager::get_intercept_scid
	 */
	public requested_next_hop_scid: bigint;
	/**
	 * The payment hash used for this HTLC.
	 */
	public payment_hash: Uint8Array;
	/**
	 * How many msats were received on the inbound edge of this HTLC.
	 */
	public inbound_amount_msat: bigint;
	/**
	 * How many msats the payer intended to route to the next node. Depending on the reason you are
	 * intercepting this payment, you might take a fee by forwarding less than this amount.
	 * 
	 * Note that LDK will NOT check that expected fees were factored into this value. You MUST
	 * check that whatever fee you want has been included here or subtract it as required. Further,
	 * LDK will not stop you from forwarding more than you received.
	 */
	public expected_outbound_amount_msat: bigint;
	/* @internal */
	public constructor(ptr: bigint) {
		super(null, ptr);
		const intercept_id: number = bindings.LDKEvent_HTLCIntercepted_get_intercept_id(ptr);
		const intercept_id_conv: Uint8Array = bindings.decodeUint8Array(intercept_id);
		this.intercept_id = intercept_id_conv;
		this.requested_next_hop_scid = bindings.LDKEvent_HTLCIntercepted_get_requested_next_hop_scid(ptr);
		const payment_hash: number = bindings.LDKEvent_HTLCIntercepted_get_payment_hash(ptr);
		const payment_hash_conv: Uint8Array = bindings.decodeUint8Array(payment_hash);
		this.payment_hash = payment_hash_conv;
		this.inbound_amount_msat = bindings.LDKEvent_HTLCIntercepted_get_inbound_amount_msat(ptr);
		this.expected_outbound_amount_msat = bindings.LDKEvent_HTLCIntercepted_get_expected_outbound_amount_msat(ptr);
	}
}
/** A Event of type SpendableOutputs */
export class Event_SpendableOutputs extends Event {
	/**
	 * The outputs which you should store as spendable by you.
	 */
	public outputs: SpendableOutputDescriptor[];
	/* @internal */
	public constructor(ptr: bigint) {
		super(null, ptr);
		const outputs: number = bindings.LDKEvent_SpendableOutputs_get_outputs(ptr);
		const outputs_conv_27_len: number = bindings.getArrayLength(outputs);
			const outputs_conv_27_arr: SpendableOutputDescriptor[] = new Array(outputs_conv_27_len).fill(null);
			for (var b = 0; b < outputs_conv_27_len; b++) {
				const outputs_conv_27: bigint = bindings.getU64ArrayElem(outputs, b);
				const outputs_conv_27_hu_conv: SpendableOutputDescriptor = SpendableOutputDescriptor.constr_from_ptr(outputs_conv_27);
				CommonBase.add_ref_from(outputs_conv_27_hu_conv, this);
				outputs_conv_27_arr[b] = outputs_conv_27_hu_conv;
			}
			bindings.freeWasmMemory(outputs)
		this.outputs = outputs_conv_27_arr;
	}
}
/** A Event of type PaymentForwarded */
export class Event_PaymentForwarded extends Event {
	/**
	 * The incoming channel between the previous node and us. This is only `None` for events
	 * generated or serialized by versions prior to 0.0.107.
	 * 
	 * Note that this (or a relevant inner pointer) may be NULL or all-0s to represent None
	 */
	public prev_channel_id: Uint8Array;
	/**
	 * The outgoing channel between the next node and us. This is only `None` for events
	 * generated or serialized by versions prior to 0.0.107.
	 * 
	 * Note that this (or a relevant inner pointer) may be NULL or all-0s to represent None
	 */
	public next_channel_id: Uint8Array;
	/**
	 * The fee, in milli-satoshis, which was earned as a result of the payment.
	 * 
	 * Note that if we force-closed the channel over which we forwarded an HTLC while the HTLC
	 * was pending, the amount the next hop claimed will have been rounded down to the nearest
	 * whole satoshi. Thus, the fee calculated here may be higher than expected as we still
	 * claimed the full value in millisatoshis from the source. In this case,
	 * `claim_from_onchain_tx` will be set.
	 * 
	 * If the channel which sent us the payment has been force-closed, we will claim the funds
	 * via an on-chain transaction. In that case we do not yet know the on-chain transaction
	 * fees which we will spend and will instead set this to `None`. It is possible duplicate
	 * `PaymentForwarded` events are generated for the same payment iff `fee_earned_msat` is
	 * `None`.
	 */
	public fee_earned_msat: Option_u64Z;
	/**
	 * If this is `true`, the forwarded HTLC was claimed by our counterparty via an on-chain
	 * transaction.
	 */
	public claim_from_onchain_tx: boolean;
	/* @internal */
	public constructor(ptr: bigint) {
		super(null, ptr);
		const prev_channel_id: number = bindings.LDKEvent_PaymentForwarded_get_prev_channel_id(ptr);
		const prev_channel_id_conv: Uint8Array = bindings.decodeUint8Array(prev_channel_id);
		this.prev_channel_id = prev_channel_id_conv;
		const next_channel_id: number = bindings.LDKEvent_PaymentForwarded_get_next_channel_id(ptr);
		const next_channel_id_conv: Uint8Array = bindings.decodeUint8Array(next_channel_id);
		this.next_channel_id = next_channel_id_conv;
		const fee_earned_msat: bigint = bindings.LDKEvent_PaymentForwarded_get_fee_earned_msat(ptr);
		const fee_earned_msat_hu_conv: Option_u64Z = Option_u64Z.constr_from_ptr(fee_earned_msat);
			CommonBase.add_ref_from(fee_earned_msat_hu_conv, this);
		this.fee_earned_msat = fee_earned_msat_hu_conv;
		this.claim_from_onchain_tx = bindings.LDKEvent_PaymentForwarded_get_claim_from_onchain_tx(ptr);
	}
}
/** A Event of type ChannelReady */
export class Event_ChannelReady extends Event {
	/**
	 * The channel_id of the channel that is ready.
	 */
	public channel_id: Uint8Array;
	/**
	 * The `user_channel_id` value passed in to [`ChannelManager::create_channel`] for outbound
	 * channels, or to [`ChannelManager::accept_inbound_channel`] for inbound channels if
	 * [`UserConfig::manually_accept_inbound_channels`] config flag is set to true. Otherwise
	 * `user_channel_id` will be randomized for an inbound channel.
	 * 
	 * [`ChannelManager::create_channel`]: crate::ln::channelmanager::ChannelManager::create_channel
	 * [`ChannelManager::accept_inbound_channel`]: crate::ln::channelmanager::ChannelManager::accept_inbound_channel
	 * [`UserConfig::manually_accept_inbound_channels`]: crate::util::config::UserConfig::manually_accept_inbound_channels
	 */
	public user_channel_id: bigint;
	/**
	 * The node_id of the channel counterparty.
	 */
	public counterparty_node_id: Uint8Array;
	/**
	 * The features that this channel will operate with.
	 */
	public channel_type: ChannelTypeFeatures;
	/* @internal */
	public constructor(ptr: bigint) {
		super(null, ptr);
		const channel_id: number = bindings.LDKEvent_ChannelReady_get_channel_id(ptr);
		const channel_id_conv: Uint8Array = bindings.decodeUint8Array(channel_id);
		this.channel_id = channel_id_conv;
		const user_channel_id: number = bindings.LDKEvent_ChannelReady_get_user_channel_id(ptr);
		const user_channel_id_conv: bigint = bindings.decodeUint128(user_channel_id);
		this.user_channel_id = user_channel_id_conv;
		const counterparty_node_id: number = bindings.LDKEvent_ChannelReady_get_counterparty_node_id(ptr);
		const counterparty_node_id_conv: Uint8Array = bindings.decodeUint8Array(counterparty_node_id);
		this.counterparty_node_id = counterparty_node_id_conv;
		const channel_type: bigint = bindings.LDKEvent_ChannelReady_get_channel_type(ptr);
		const channel_type_hu_conv: ChannelTypeFeatures = new ChannelTypeFeatures(null, channel_type);
			CommonBase.add_ref_from(channel_type_hu_conv, this);
		this.channel_type = channel_type_hu_conv;
	}
}
/** A Event of type ChannelClosed */
export class Event_ChannelClosed extends Event {
	/**
	 * The channel_id of the channel which has been closed. Note that on-chain transactions
	 * resolving the channel are likely still awaiting confirmation.
	 */
	public channel_id: Uint8Array;
	/**
	 * The `user_channel_id` value passed in to [`ChannelManager::create_channel`] for outbound
	 * channels, or to [`ChannelManager::accept_inbound_channel`] for inbound channels if
	 * [`UserConfig::manually_accept_inbound_channels`] config flag is set to true. Otherwise
	 * `user_channel_id` will be randomized for inbound channels.
	 * This may be zero for inbound channels serialized prior to 0.0.113 and will always be
	 * zero for objects serialized with LDK versions prior to 0.0.102.
	 * 
	 * [`ChannelManager::create_channel`]: crate::ln::channelmanager::ChannelManager::create_channel
	 * [`ChannelManager::accept_inbound_channel`]: crate::ln::channelmanager::ChannelManager::accept_inbound_channel
	 * [`UserConfig::manually_accept_inbound_channels`]: crate::util::config::UserConfig::manually_accept_inbound_channels
	 */
	public user_channel_id: bigint;
	/**
	 * The reason the channel was closed.
	 */
	public reason: ClosureReason;
	/* @internal */
	public constructor(ptr: bigint) {
		super(null, ptr);
		const channel_id: number = bindings.LDKEvent_ChannelClosed_get_channel_id(ptr);
		const channel_id_conv: Uint8Array = bindings.decodeUint8Array(channel_id);
		this.channel_id = channel_id_conv;
		const user_channel_id: number = bindings.LDKEvent_ChannelClosed_get_user_channel_id(ptr);
		const user_channel_id_conv: bigint = bindings.decodeUint128(user_channel_id);
		this.user_channel_id = user_channel_id_conv;
		const reason: bigint = bindings.LDKEvent_ChannelClosed_get_reason(ptr);
		const reason_hu_conv: ClosureReason = ClosureReason.constr_from_ptr(reason);
			CommonBase.add_ref_from(reason_hu_conv, this);
		this.reason = reason_hu_conv;
	}
}
/** A Event of type DiscardFunding */
export class Event_DiscardFunding extends Event {
	/**
	 * The channel_id of the channel which has been closed.
	 */
	public channel_id: Uint8Array;
	/**
	 * The full transaction received from the user
	 */
	public transaction: Uint8Array;
	/* @internal */
	public constructor(ptr: bigint) {
		super(null, ptr);
		const channel_id: number = bindings.LDKEvent_DiscardFunding_get_channel_id(ptr);
		const channel_id_conv: Uint8Array = bindings.decodeUint8Array(channel_id);
		this.channel_id = channel_id_conv;
		const transaction: number = bindings.LDKEvent_DiscardFunding_get_transaction(ptr);
		const transaction_conv: Uint8Array = bindings.decodeUint8Array(transaction);
		this.transaction = transaction_conv;
	}
}
/** A Event of type OpenChannelRequest */
export class Event_OpenChannelRequest extends Event {
	/**
	 * The temporary channel ID of the channel requested to be opened.
	 * 
	 * When responding to the request, the `temporary_channel_id` should be passed
	 * back to the ChannelManager through [`ChannelManager::accept_inbound_channel`] to accept,
	 * or through [`ChannelManager::force_close_without_broadcasting_txn`] to reject.
	 * 
	 * [`ChannelManager::accept_inbound_channel`]: crate::ln::channelmanager::ChannelManager::accept_inbound_channel
	 * [`ChannelManager::force_close_without_broadcasting_txn`]: crate::ln::channelmanager::ChannelManager::force_close_without_broadcasting_txn
	 */
	public temporary_channel_id: Uint8Array;
	/**
	 * The node_id of the counterparty requesting to open the channel.
	 * 
	 * When responding to the request, the `counterparty_node_id` should be passed
	 * back to the `ChannelManager` through [`ChannelManager::accept_inbound_channel`] to
	 * accept the request, or through [`ChannelManager::force_close_without_broadcasting_txn`] to reject the
	 * request.
	 * 
	 * [`ChannelManager::accept_inbound_channel`]: crate::ln::channelmanager::ChannelManager::accept_inbound_channel
	 * [`ChannelManager::force_close_without_broadcasting_txn`]: crate::ln::channelmanager::ChannelManager::force_close_without_broadcasting_txn
	 */
	public counterparty_node_id: Uint8Array;
	/**
	 * The channel value of the requested channel.
	 */
	public funding_satoshis: bigint;
	/**
	 * Our starting balance in the channel if the request is accepted, in milli-satoshi.
	 */
	public push_msat: bigint;
	/**
	 * The features that this channel will operate with. If you reject the channel, a
	 * well-behaved counterparty may automatically re-attempt the channel with a new set of
	 * feature flags.
	 * 
	 * Note that if [`ChannelTypeFeatures::supports_scid_privacy`] returns true on this type,
	 * the resulting [`ChannelManager`] will not be readable by versions of LDK prior to
	 * 0.0.106.
	 * 
	 * Furthermore, note that if [`ChannelTypeFeatures::supports_zero_conf`] returns true on this type,
	 * the resulting [`ChannelManager`] will not be readable by versions of LDK prior to
	 * 0.0.107. Channels setting this type also need to get manually accepted via
	 * [`crate::ln::channelmanager::ChannelManager::accept_inbound_channel_from_trusted_peer_0conf`],
	 * or will be rejected otherwise.
	 * 
	 * [`ChannelManager`]: crate::ln::channelmanager::ChannelManager
	 */
	public channel_type: ChannelTypeFeatures;
	/* @internal */
	public constructor(ptr: bigint) {
		super(null, ptr);
		const temporary_channel_id: number = bindings.LDKEvent_OpenChannelRequest_get_temporary_channel_id(ptr);
		const temporary_channel_id_conv: Uint8Array = bindings.decodeUint8Array(temporary_channel_id);
		this.temporary_channel_id = temporary_channel_id_conv;
		const counterparty_node_id: number = bindings.LDKEvent_OpenChannelRequest_get_counterparty_node_id(ptr);
		const counterparty_node_id_conv: Uint8Array = bindings.decodeUint8Array(counterparty_node_id);
		this.counterparty_node_id = counterparty_node_id_conv;
		this.funding_satoshis = bindings.LDKEvent_OpenChannelRequest_get_funding_satoshis(ptr);
		this.push_msat = bindings.LDKEvent_OpenChannelRequest_get_push_msat(ptr);
		const channel_type: bigint = bindings.LDKEvent_OpenChannelRequest_get_channel_type(ptr);
		const channel_type_hu_conv: ChannelTypeFeatures = new ChannelTypeFeatures(null, channel_type);
			CommonBase.add_ref_from(channel_type_hu_conv, this);
		this.channel_type = channel_type_hu_conv;
	}
}
/** A Event of type HTLCHandlingFailed */
export class Event_HTLCHandlingFailed extends Event {
	/**
	 * The channel over which the HTLC was received.
	 */
	public prev_channel_id: Uint8Array;
	/**
	 * Destination of the HTLC that failed to be processed.
	 */
	public failed_next_destination: HTLCDestination;
	/* @internal */
	public constructor(ptr: bigint) {
		super(null, ptr);
		const prev_channel_id: number = bindings.LDKEvent_HTLCHandlingFailed_get_prev_channel_id(ptr);
		const prev_channel_id_conv: Uint8Array = bindings.decodeUint8Array(prev_channel_id);
		this.prev_channel_id = prev_channel_id_conv;
		const failed_next_destination: bigint = bindings.LDKEvent_HTLCHandlingFailed_get_failed_next_destination(ptr);
		const failed_next_destination_hu_conv: HTLCDestination = HTLCDestination.constr_from_ptr(failed_next_destination);
			CommonBase.add_ref_from(failed_next_destination_hu_conv, this);
		this.failed_next_destination = failed_next_destination_hu_conv;
	}
}
