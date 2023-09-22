"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import nibiru.sudo.v1.state_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class QuerySudoersRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___QuerySudoersRequest = QuerySudoersRequest

@typing_extensions.final
class QuerySudoersResponse(google.protobuf.message.Message):
    """QuerySudoersResponse indicates the successful execution of MsgEditSudeors."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUDOERS_FIELD_NUMBER: builtins.int
    @property
    def sudoers(self) -> nibiru.sudo.v1.state_pb2.Sudoers: ...
    def __init__(
        self,
        *,
        sudoers: nibiru.sudo.v1.state_pb2.Sudoers | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["sudoers", b"sudoers"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["sudoers", b"sudoers"]) -> None: ...

global___QuerySudoersResponse = QuerySudoersResponse
