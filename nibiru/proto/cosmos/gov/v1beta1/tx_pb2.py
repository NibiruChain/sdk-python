# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/gov/v1beta1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmos.gov.v1beta1 import gov_pb2 as cosmos_dot_gov_dot_v1beta1_dot_gov__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1b\x63osmos/gov/v1beta1/tx.proto\x12\x12\x63osmos.gov.v1beta1\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1c\x63osmos/gov/v1beta1/gov.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\"\xeb\x01\n\x11MsgSubmitProposal\x12\x32\n\x07\x63ontent\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyB\x0b\xca\xb4-\x07\x43ontent\x12~\n\x0finitial_deposit\x18\x02 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBJ\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xf2\xde\x1f\x16yaml:\"initial_deposit\"\x12\x10\n\x08proposer\x18\x03 \x01(\t:\x10\xe8\xa0\x1f\x00\x98\xa0\x1f\x00\x80\xdc \x00\x88\xa0\x1f\x00\"W\n\x19MsgSubmitProposalResponse\x12:\n\x0bproposal_id\x18\x01 \x01(\x04\x42%\xea\xde\x1f\x0bproposal_id\xf2\xde\x1f\x12yaml:\"proposal_id\"\"\x96\x01\n\x07MsgVote\x12:\n\x0bproposal_id\x18\x01 \x01(\x04\x42%\xea\xde\x1f\x0bproposal_id\xf2\xde\x1f\x12yaml:\"proposal_id\"\x12\r\n\x05voter\x18\x02 \x01(\t\x12.\n\x06option\x18\x03 \x01(\x0e\x32\x1e.cosmos.gov.v1beta1.VoteOption:\x10\xe8\xa0\x1f\x00\x98\xa0\x1f\x00\x80\xdc \x00\x88\xa0\x1f\x00\"\x11\n\x0fMsgVoteResponse\"\x9e\x01\n\x0fMsgVoteWeighted\x12+\n\x0bproposal_id\x18\x01 \x01(\x04\x42\x16\xf2\xde\x1f\x12yaml:\"proposal_id\"\x12\r\n\x05voter\x18\x02 \x01(\t\x12=\n\x07options\x18\x03 \x03(\x0b\x32&.cosmos.gov.v1beta1.WeightedVoteOptionB\x04\xc8\xde\x1f\x00:\x10\xe8\xa0\x1f\x00\x98\xa0\x1f\x00\x80\xdc \x00\x88\xa0\x1f\x00\"\x19\n\x17MsgVoteWeightedResponse\"\xca\x01\n\nMsgDeposit\x12:\n\x0bproposal_id\x18\x01 \x01(\x04\x42%\xea\xde\x1f\x0bproposal_id\xf2\xde\x1f\x12yaml:\"proposal_id\"\x12\x11\n\tdepositor\x18\x02 \x01(\t\x12[\n\x06\x61mount\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins:\x10\xe8\xa0\x1f\x00\x98\xa0\x1f\x00\x80\xdc \x00\x88\xa0\x1f\x00\"\x14\n\x12MsgDepositResponse2\xec\x02\n\x03Msg\x12\x66\n\x0eSubmitProposal\x12%.cosmos.gov.v1beta1.MsgSubmitProposal\x1a-.cosmos.gov.v1beta1.MsgSubmitProposalResponse\x12H\n\x04Vote\x12\x1b.cosmos.gov.v1beta1.MsgVote\x1a#.cosmos.gov.v1beta1.MsgVoteResponse\x12`\n\x0cVoteWeighted\x12#.cosmos.gov.v1beta1.MsgVoteWeighted\x1a+.cosmos.gov.v1beta1.MsgVoteWeightedResponse\x12Q\n\x07\x44\x65posit\x12\x1e.cosmos.gov.v1beta1.MsgDeposit\x1a&.cosmos.gov.v1beta1.MsgDepositResponseB*Z(github.com/cosmos/cosmos-sdk/x/gov/typesb\x06proto3'
)


_MSGSUBMITPROPOSAL = DESCRIPTOR.message_types_by_name['MsgSubmitProposal']
_MSGSUBMITPROPOSALRESPONSE = DESCRIPTOR.message_types_by_name['MsgSubmitProposalResponse']
_MSGVOTE = DESCRIPTOR.message_types_by_name['MsgVote']
_MSGVOTERESPONSE = DESCRIPTOR.message_types_by_name['MsgVoteResponse']
_MSGVOTEWEIGHTED = DESCRIPTOR.message_types_by_name['MsgVoteWeighted']
_MSGVOTEWEIGHTEDRESPONSE = DESCRIPTOR.message_types_by_name['MsgVoteWeightedResponse']
_MSGDEPOSIT = DESCRIPTOR.message_types_by_name['MsgDeposit']
_MSGDEPOSITRESPONSE = DESCRIPTOR.message_types_by_name['MsgDepositResponse']
MsgSubmitProposal = _reflection.GeneratedProtocolMessageType(
    'MsgSubmitProposal',
    (_message.Message,),
    {
        'DESCRIPTOR': _MSGSUBMITPROPOSAL,
        '__module__': 'cosmos.gov.v1beta1.tx_pb2'
        # @@protoc_insertion_point(class_scope:cosmos.gov.v1beta1.MsgSubmitProposal)
    },
)
_sym_db.RegisterMessage(MsgSubmitProposal)

MsgSubmitProposalResponse = _reflection.GeneratedProtocolMessageType(
    'MsgSubmitProposalResponse',
    (_message.Message,),
    {
        'DESCRIPTOR': _MSGSUBMITPROPOSALRESPONSE,
        '__module__': 'cosmos.gov.v1beta1.tx_pb2'
        # @@protoc_insertion_point(class_scope:cosmos.gov.v1beta1.MsgSubmitProposalResponse)
    },
)
_sym_db.RegisterMessage(MsgSubmitProposalResponse)

MsgVote = _reflection.GeneratedProtocolMessageType(
    'MsgVote',
    (_message.Message,),
    {
        'DESCRIPTOR': _MSGVOTE,
        '__module__': 'cosmos.gov.v1beta1.tx_pb2'
        # @@protoc_insertion_point(class_scope:cosmos.gov.v1beta1.MsgVote)
    },
)
_sym_db.RegisterMessage(MsgVote)

MsgVoteResponse = _reflection.GeneratedProtocolMessageType(
    'MsgVoteResponse',
    (_message.Message,),
    {
        'DESCRIPTOR': _MSGVOTERESPONSE,
        '__module__': 'cosmos.gov.v1beta1.tx_pb2'
        # @@protoc_insertion_point(class_scope:cosmos.gov.v1beta1.MsgVoteResponse)
    },
)
_sym_db.RegisterMessage(MsgVoteResponse)

MsgVoteWeighted = _reflection.GeneratedProtocolMessageType(
    'MsgVoteWeighted',
    (_message.Message,),
    {
        'DESCRIPTOR': _MSGVOTEWEIGHTED,
        '__module__': 'cosmos.gov.v1beta1.tx_pb2'
        # @@protoc_insertion_point(class_scope:cosmos.gov.v1beta1.MsgVoteWeighted)
    },
)
_sym_db.RegisterMessage(MsgVoteWeighted)

MsgVoteWeightedResponse = _reflection.GeneratedProtocolMessageType(
    'MsgVoteWeightedResponse',
    (_message.Message,),
    {
        'DESCRIPTOR': _MSGVOTEWEIGHTEDRESPONSE,
        '__module__': 'cosmos.gov.v1beta1.tx_pb2'
        # @@protoc_insertion_point(class_scope:cosmos.gov.v1beta1.MsgVoteWeightedResponse)
    },
)
_sym_db.RegisterMessage(MsgVoteWeightedResponse)

MsgDeposit = _reflection.GeneratedProtocolMessageType(
    'MsgDeposit',
    (_message.Message,),
    {
        'DESCRIPTOR': _MSGDEPOSIT,
        '__module__': 'cosmos.gov.v1beta1.tx_pb2'
        # @@protoc_insertion_point(class_scope:cosmos.gov.v1beta1.MsgDeposit)
    },
)
_sym_db.RegisterMessage(MsgDeposit)

MsgDepositResponse = _reflection.GeneratedProtocolMessageType(
    'MsgDepositResponse',
    (_message.Message,),
    {
        'DESCRIPTOR': _MSGDEPOSITRESPONSE,
        '__module__': 'cosmos.gov.v1beta1.tx_pb2'
        # @@protoc_insertion_point(class_scope:cosmos.gov.v1beta1.MsgDepositResponse)
    },
)
_sym_db.RegisterMessage(MsgDepositResponse)

_MSG = DESCRIPTOR.services_by_name['Msg']
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z(github.com/cosmos/cosmos-sdk/x/gov/types'
    _MSGSUBMITPROPOSAL.fields_by_name['content']._options = None
    _MSGSUBMITPROPOSAL.fields_by_name['content']._serialized_options = b'\312\264-\007Content'
    _MSGSUBMITPROPOSAL.fields_by_name['initial_deposit']._options = None
    _MSGSUBMITPROPOSAL.fields_by_name[
        'initial_deposit'
    ]._serialized_options = (
        b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\362\336\037\026yaml:\"initial_deposit\"'
    )
    _MSGSUBMITPROPOSAL._options = None
    _MSGSUBMITPROPOSAL._serialized_options = b'\350\240\037\000\230\240\037\000\200\334 \000\210\240\037\000'
    _MSGSUBMITPROPOSALRESPONSE.fields_by_name['proposal_id']._options = None
    _MSGSUBMITPROPOSALRESPONSE.fields_by_name[
        'proposal_id'
    ]._serialized_options = b'\352\336\037\013proposal_id\362\336\037\022yaml:\"proposal_id\"'
    _MSGVOTE.fields_by_name['proposal_id']._options = None
    _MSGVOTE.fields_by_name[
        'proposal_id'
    ]._serialized_options = b'\352\336\037\013proposal_id\362\336\037\022yaml:\"proposal_id\"'
    _MSGVOTE._options = None
    _MSGVOTE._serialized_options = b'\350\240\037\000\230\240\037\000\200\334 \000\210\240\037\000'
    _MSGVOTEWEIGHTED.fields_by_name['proposal_id']._options = None
    _MSGVOTEWEIGHTED.fields_by_name['proposal_id']._serialized_options = b'\362\336\037\022yaml:\"proposal_id\"'
    _MSGVOTEWEIGHTED.fields_by_name['options']._options = None
    _MSGVOTEWEIGHTED.fields_by_name['options']._serialized_options = b'\310\336\037\000'
    _MSGVOTEWEIGHTED._options = None
    _MSGVOTEWEIGHTED._serialized_options = b'\350\240\037\000\230\240\037\000\200\334 \000\210\240\037\000'
    _MSGDEPOSIT.fields_by_name['proposal_id']._options = None
    _MSGDEPOSIT.fields_by_name[
        'proposal_id'
    ]._serialized_options = b'\352\336\037\013proposal_id\362\336\037\022yaml:\"proposal_id\"'
    _MSGDEPOSIT.fields_by_name['amount']._options = None
    _MSGDEPOSIT.fields_by_name[
        'amount'
    ]._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
    _MSGDEPOSIT._options = None
    _MSGDEPOSIT._serialized_options = b'\350\240\037\000\230\240\037\000\200\334 \000\210\240\037\000'
    _MSGSUBMITPROPOSAL._serialized_start = 190
    _MSGSUBMITPROPOSAL._serialized_end = 425
    _MSGSUBMITPROPOSALRESPONSE._serialized_start = 427
    _MSGSUBMITPROPOSALRESPONSE._serialized_end = 514
    _MSGVOTE._serialized_start = 517
    _MSGVOTE._serialized_end = 667
    _MSGVOTERESPONSE._serialized_start = 669
    _MSGVOTERESPONSE._serialized_end = 686
    _MSGVOTEWEIGHTED._serialized_start = 689
    _MSGVOTEWEIGHTED._serialized_end = 847
    _MSGVOTEWEIGHTEDRESPONSE._serialized_start = 849
    _MSGVOTEWEIGHTEDRESPONSE._serialized_end = 874
    _MSGDEPOSIT._serialized_start = 877
    _MSGDEPOSIT._serialized_end = 1079
    _MSGDEPOSITRESPONSE._serialized_start = 1081
    _MSGDEPOSITRESPONSE._serialized_end = 1101
    _MSG._serialized_start = 1104
    _MSG._serialized_end = 1468
# @@protoc_insertion_point(module_scope)
