"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Since: cosmos-sdk 0.46"""
import builtins
import collections.abc
import cosmos.group.v1.types_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class GenesisState(google.protobuf.message.Message):
    """GenesisState defines the group module's genesis state."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    GROUP_SEQ_FIELD_NUMBER: builtins.int
    GROUPS_FIELD_NUMBER: builtins.int
    GROUP_MEMBERS_FIELD_NUMBER: builtins.int
    GROUP_POLICY_SEQ_FIELD_NUMBER: builtins.int
    GROUP_POLICIES_FIELD_NUMBER: builtins.int
    PROPOSAL_SEQ_FIELD_NUMBER: builtins.int
    PROPOSALS_FIELD_NUMBER: builtins.int
    VOTES_FIELD_NUMBER: builtins.int
    group_seq: builtins.int
    """group_seq is the group table orm.Sequence,
    it is used to get the next group ID.
    """
    @property
    def groups(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.group.v1.types_pb2.GroupInfo]:
        """groups is the list of groups info."""
    @property
    def group_members(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.group.v1.types_pb2.GroupMember]:
        """group_members is the list of groups members."""
    group_policy_seq: builtins.int
    """group_policy_seq is the group policy table orm.Sequence,
    it is used to generate the next group policy account address.
    """
    @property
    def group_policies(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.group.v1.types_pb2.GroupPolicyInfo]:
        """group_policies is the list of group policies info."""
    proposal_seq: builtins.int
    """proposal_seq is the proposal table orm.Sequence,
    it is used to get the next proposal ID.
    """
    @property
    def proposals(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.group.v1.types_pb2.Proposal]:
        """proposals is the list of proposals."""
    @property
    def votes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.group.v1.types_pb2.Vote]:
        """votes is the list of votes."""
    def __init__(
        self,
        *,
        group_seq: builtins.int = ...,
        groups: collections.abc.Iterable[cosmos.group.v1.types_pb2.GroupInfo] | None = ...,
        group_members: collections.abc.Iterable[cosmos.group.v1.types_pb2.GroupMember] | None = ...,
        group_policy_seq: builtins.int = ...,
        group_policies: collections.abc.Iterable[cosmos.group.v1.types_pb2.GroupPolicyInfo] | None = ...,
        proposal_seq: builtins.int = ...,
        proposals: collections.abc.Iterable[cosmos.group.v1.types_pb2.Proposal] | None = ...,
        votes: collections.abc.Iterable[cosmos.group.v1.types_pb2.Vote] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["group_members", b"group_members", "group_policies", b"group_policies", "group_policy_seq", b"group_policy_seq", "group_seq", b"group_seq", "groups", b"groups", "proposal_seq", b"proposal_seq", "proposals", b"proposals", "votes", b"votes"]) -> None: ...

global___GenesisState = GenesisState
