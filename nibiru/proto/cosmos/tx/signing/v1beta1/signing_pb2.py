# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/tx/signing/v1beta1/signing.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import enum_type_wrapper

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.crypto.multisig.v1beta1 import (
    multisig_pb2 as cosmos_dot_crypto_dot_multisig_dot_v1beta1_dot_multisig__pb2,
)
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\'cosmos/tx/signing/v1beta1/signing.proto\x12\x19\x63osmos.tx.signing.v1beta1\x1a-cosmos/crypto/multisig/v1beta1/multisig.proto\x1a\x19google/protobuf/any.proto\"Z\n\x14SignatureDescriptors\x12\x42\n\nsignatures\x18\x01 \x03(\x0b\x32..cosmos.tx.signing.v1beta1.SignatureDescriptor\"\xa4\x04\n\x13SignatureDescriptor\x12(\n\npublic_key\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x41\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x33.cosmos.tx.signing.v1beta1.SignatureDescriptor.Data\x12\x10\n\x08sequence\x18\x03 \x01(\x04\x1a\x8d\x03\n\x04\x44\x61ta\x12L\n\x06single\x18\x01 \x01(\x0b\x32:.cosmos.tx.signing.v1beta1.SignatureDescriptor.Data.SingleH\x00\x12J\n\x05multi\x18\x02 \x01(\x0b\x32\x39.cosmos.tx.signing.v1beta1.SignatureDescriptor.Data.MultiH\x00\x1aN\n\x06Single\x12\x31\n\x04mode\x18\x01 \x01(\x0e\x32#.cosmos.tx.signing.v1beta1.SignMode\x12\x11\n\tsignature\x18\x02 \x01(\x0c\x1a\x93\x01\n\x05Multi\x12\x41\n\x08\x62itarray\x18\x01 \x01(\x0b\x32/.cosmos.crypto.multisig.v1beta1.CompactBitArray\x12G\n\nsignatures\x18\x02 \x03(\x0b\x32\x33.cosmos.tx.signing.v1beta1.SignatureDescriptor.DataB\x05\n\x03sum*\x8b\x01\n\x08SignMode\x12\x19\n\x15SIGN_MODE_UNSPECIFIED\x10\x00\x12\x14\n\x10SIGN_MODE_DIRECT\x10\x01\x12\x15\n\x11SIGN_MODE_TEXTUAL\x10\x02\x12\x1f\n\x1bSIGN_MODE_LEGACY_AMINO_JSON\x10\x7f\x12\x16\n\x11SIGN_MODE_EIP_191\x10\xbf\x01\x42/Z-github.com/cosmos/cosmos-sdk/types/tx/signingb\x06proto3'
)

_SIGNMODE = DESCRIPTOR.enum_types_by_name['SignMode']
SignMode = enum_type_wrapper.EnumTypeWrapper(_SIGNMODE)
SIGN_MODE_UNSPECIFIED = 0
SIGN_MODE_DIRECT = 1
SIGN_MODE_TEXTUAL = 2
SIGN_MODE_LEGACY_AMINO_JSON = 127
SIGN_MODE_EIP_191 = 191


_SIGNATUREDESCRIPTORS = DESCRIPTOR.message_types_by_name['SignatureDescriptors']
_SIGNATUREDESCRIPTOR = DESCRIPTOR.message_types_by_name['SignatureDescriptor']
_SIGNATUREDESCRIPTOR_DATA = _SIGNATUREDESCRIPTOR.nested_types_by_name['Data']
_SIGNATUREDESCRIPTOR_DATA_SINGLE = _SIGNATUREDESCRIPTOR_DATA.nested_types_by_name['Single']
_SIGNATUREDESCRIPTOR_DATA_MULTI = _SIGNATUREDESCRIPTOR_DATA.nested_types_by_name['Multi']
SignatureDescriptors = _reflection.GeneratedProtocolMessageType(
    'SignatureDescriptors',
    (_message.Message,),
    {
        'DESCRIPTOR': _SIGNATUREDESCRIPTORS,
        '__module__': 'cosmos.tx.signing.v1beta1.signing_pb2'
        # @@protoc_insertion_point(class_scope:cosmos.tx.signing.v1beta1.SignatureDescriptors)
    },
)
_sym_db.RegisterMessage(SignatureDescriptors)

SignatureDescriptor = _reflection.GeneratedProtocolMessageType(
    'SignatureDescriptor',
    (_message.Message,),
    {
        'Data': _reflection.GeneratedProtocolMessageType(
            'Data',
            (_message.Message,),
            {
                'Single': _reflection.GeneratedProtocolMessageType(
                    'Single',
                    (_message.Message,),
                    {
                        'DESCRIPTOR': _SIGNATUREDESCRIPTOR_DATA_SINGLE,
                        '__module__': 'cosmos.tx.signing.v1beta1.signing_pb2'
                        # @@protoc_insertion_point(class_scope:cosmos.tx.signing.v1beta1.SignatureDescriptor.Data.Single)
                    },
                ),
                'Multi': _reflection.GeneratedProtocolMessageType(
                    'Multi',
                    (_message.Message,),
                    {
                        'DESCRIPTOR': _SIGNATUREDESCRIPTOR_DATA_MULTI,
                        '__module__': 'cosmos.tx.signing.v1beta1.signing_pb2'
                        # @@protoc_insertion_point(class_scope:cosmos.tx.signing.v1beta1.SignatureDescriptor.Data.Multi)
                    },
                ),
                'DESCRIPTOR': _SIGNATUREDESCRIPTOR_DATA,
                '__module__': 'cosmos.tx.signing.v1beta1.signing_pb2'
                # @@protoc_insertion_point(class_scope:cosmos.tx.signing.v1beta1.SignatureDescriptor.Data)
            },
        ),
        'DESCRIPTOR': _SIGNATUREDESCRIPTOR,
        '__module__': 'cosmos.tx.signing.v1beta1.signing_pb2'
        # @@protoc_insertion_point(class_scope:cosmos.tx.signing.v1beta1.SignatureDescriptor)
    },
)
_sym_db.RegisterMessage(SignatureDescriptor)
_sym_db.RegisterMessage(SignatureDescriptor.Data)
_sym_db.RegisterMessage(SignatureDescriptor.Data.Single)
_sym_db.RegisterMessage(SignatureDescriptor.Data.Multi)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z-github.com/cosmos/cosmos-sdk/types/tx/signing'
    _SIGNMODE._serialized_start = 788
    _SIGNMODE._serialized_end = 927
    _SIGNATUREDESCRIPTORS._serialized_start = 144
    _SIGNATUREDESCRIPTORS._serialized_end = 234
    _SIGNATUREDESCRIPTOR._serialized_start = 237
    _SIGNATUREDESCRIPTOR._serialized_end = 785
    _SIGNATUREDESCRIPTOR_DATA._serialized_start = 388
    _SIGNATUREDESCRIPTOR_DATA._serialized_end = 785
    _SIGNATUREDESCRIPTOR_DATA_SINGLE._serialized_start = 550
    _SIGNATUREDESCRIPTOR_DATA_SINGLE._serialized_end = 628
    _SIGNATUREDESCRIPTOR_DATA_MULTI._serialized_start = 631
    _SIGNATUREDESCRIPTOR_DATA_MULTI._serialized_end = 778
# @@protoc_insertion_point(module_scope)
