# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/bank/v1beta1/authz.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1f\x63osmos/bank/v1beta1/authz.proto\x12\x13\x63osmos.bank.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"\x88\x01\n\x11SendAuthorization\x12`\n\x0bspend_limit\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins:\x11\xd2\xb4-\rAuthorizationB+Z)github.com/cosmos/cosmos-sdk/x/bank/typesb\x06proto3'
)


_SENDAUTHORIZATION = DESCRIPTOR.message_types_by_name['SendAuthorization']
SendAuthorization = _reflection.GeneratedProtocolMessageType(
    'SendAuthorization',
    (_message.Message,),
    {
        'DESCRIPTOR': _SENDAUTHORIZATION,
        '__module__': 'cosmos.bank.v1beta1.authz_pb2'
        # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.SendAuthorization)
    },
)
_sym_db.RegisterMessage(SendAuthorization)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z)github.com/cosmos/cosmos-sdk/x/bank/types'
    _SENDAUTHORIZATION.fields_by_name['spend_limit']._options = None
    _SENDAUTHORIZATION.fields_by_name[
        'spend_limit'
    ]._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
    _SENDAUTHORIZATION._options = None
    _SENDAUTHORIZATION._serialized_options = b'\322\264-\rAuthorization'
    _SENDAUTHORIZATION._serialized_start = 138
    _SENDAUTHORIZATION._serialized_end = 274
# @@protoc_insertion_point(module_scope)
