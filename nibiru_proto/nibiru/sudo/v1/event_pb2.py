# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nibiru/sudo/v1/event.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from nibiru_proto.nibiru.sudo.v1 import state_pb2 as nibiru_dot_sudo_dot_v1_dot_state__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1anibiru/sudo/v1/event.proto\x12\x0enibiru.sudo.v1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1anibiru/sudo/v1/state.proto\"e\n\x12\x45ventUpdateSudoers\x12\x37\n\x07sudoers\x18\x01 \x01(\x0b\x32\x17.nibiru.sudo.v1.SudoersB\x04\xc8\xde\x1f\x00R\x07sudoers\x12\x16\n\x06\x61\x63tion\x18\x02 \x01(\tR\x06\x61\x63tionB,Z*github.com/NibiruChain/nibiru/x/sudo/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nibiru.sudo.v1.event_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z*github.com/NibiruChain/nibiru/x/sudo/types'
  _EVENTUPDATESUDOERS.fields_by_name['sudoers']._options = None
  _EVENTUPDATESUDOERS.fields_by_name['sudoers']._serialized_options = b'\310\336\037\000'
  _EVENTUPDATESUDOERS._serialized_start=126
  _EVENTUPDATESUDOERS._serialized_end=227
# @@protoc_insertion_point(module_scope)
