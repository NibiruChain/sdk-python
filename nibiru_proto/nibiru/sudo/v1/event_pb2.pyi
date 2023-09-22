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
class EventUpdateSudoers(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUDOERS_FIELD_NUMBER: builtins.int
    ACTION_FIELD_NUMBER: builtins.int
    @property
    def sudoers(self) -> nibiru.sudo.v1.state_pb2.Sudoers: ...
    action: builtins.str
    """Action is the type of update that occured to the "sudoers" """
    def __init__(
        self,
        *,
        sudoers: nibiru.sudo.v1.state_pb2.Sudoers | None = ...,
        action: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["sudoers", b"sudoers"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["action", b"action", "sudoers", b"sudoers"]) -> None: ...

global___EventUpdateSudoers = EventUpdateSudoers
