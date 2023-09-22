"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import cosmos.base.query.v1beta1.pagination_pb2
import cosmos.base.tendermint.v1beta1.types_pb2
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys
import tendermint.p2p.types_pb2
import tendermint.types.block_pb2
import tendermint.types.types_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class GetValidatorSetByHeightRequest(google.protobuf.message.Message):
    """GetValidatorSetByHeightRequest is the request type for the Query/GetValidatorSetByHeight RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEIGHT_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    height: builtins.int
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest:
        """pagination defines an pagination for the request."""
    def __init__(
        self,
        *,
        height: builtins.int = ...,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["height", b"height", "pagination", b"pagination"]) -> None: ...

global___GetValidatorSetByHeightRequest = GetValidatorSetByHeightRequest

@typing_extensions.final
class GetValidatorSetByHeightResponse(google.protobuf.message.Message):
    """GetValidatorSetByHeightResponse is the response type for the Query/GetValidatorSetByHeight RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BLOCK_HEIGHT_FIELD_NUMBER: builtins.int
    VALIDATORS_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    block_height: builtins.int
    @property
    def validators(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Validator]: ...
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse:
        """pagination defines an pagination for the response."""
    def __init__(
        self,
        *,
        block_height: builtins.int = ...,
        validators: collections.abc.Iterable[global___Validator] | None = ...,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageResponse | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["block_height", b"block_height", "pagination", b"pagination", "validators", b"validators"]) -> None: ...

global___GetValidatorSetByHeightResponse = GetValidatorSetByHeightResponse

@typing_extensions.final
class GetLatestValidatorSetRequest(google.protobuf.message.Message):
    """GetLatestValidatorSetRequest is the request type for the Query/GetValidatorSetByHeight RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAGINATION_FIELD_NUMBER: builtins.int
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest:
        """pagination defines an pagination for the request."""
    def __init__(
        self,
        *,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["pagination", b"pagination"]) -> None: ...

global___GetLatestValidatorSetRequest = GetLatestValidatorSetRequest

@typing_extensions.final
class GetLatestValidatorSetResponse(google.protobuf.message.Message):
    """GetLatestValidatorSetResponse is the response type for the Query/GetValidatorSetByHeight RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BLOCK_HEIGHT_FIELD_NUMBER: builtins.int
    VALIDATORS_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    block_height: builtins.int
    @property
    def validators(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Validator]: ...
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse:
        """pagination defines an pagination for the response."""
    def __init__(
        self,
        *,
        block_height: builtins.int = ...,
        validators: collections.abc.Iterable[global___Validator] | None = ...,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageResponse | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["block_height", b"block_height", "pagination", b"pagination", "validators", b"validators"]) -> None: ...

global___GetLatestValidatorSetResponse = GetLatestValidatorSetResponse

@typing_extensions.final
class Validator(google.protobuf.message.Message):
    """Validator is the type for the validator-set."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESS_FIELD_NUMBER: builtins.int
    PUB_KEY_FIELD_NUMBER: builtins.int
    VOTING_POWER_FIELD_NUMBER: builtins.int
    PROPOSER_PRIORITY_FIELD_NUMBER: builtins.int
    address: builtins.str
    @property
    def pub_key(self) -> google.protobuf.any_pb2.Any: ...
    voting_power: builtins.int
    proposer_priority: builtins.int
    def __init__(
        self,
        *,
        address: builtins.str = ...,
        pub_key: google.protobuf.any_pb2.Any | None = ...,
        voting_power: builtins.int = ...,
        proposer_priority: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pub_key", b"pub_key"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["address", b"address", "proposer_priority", b"proposer_priority", "pub_key", b"pub_key", "voting_power", b"voting_power"]) -> None: ...

global___Validator = Validator

@typing_extensions.final
class GetBlockByHeightRequest(google.protobuf.message.Message):
    """GetBlockByHeightRequest is the request type for the Query/GetBlockByHeight RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEIGHT_FIELD_NUMBER: builtins.int
    height: builtins.int
    def __init__(
        self,
        *,
        height: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["height", b"height"]) -> None: ...

global___GetBlockByHeightRequest = GetBlockByHeightRequest

@typing_extensions.final
class GetBlockByHeightResponse(google.protobuf.message.Message):
    """GetBlockByHeightResponse is the response type for the Query/GetBlockByHeight RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BLOCK_ID_FIELD_NUMBER: builtins.int
    BLOCK_FIELD_NUMBER: builtins.int
    SDK_BLOCK_FIELD_NUMBER: builtins.int
    @property
    def block_id(self) -> tendermint.types.types_pb2.BlockID: ...
    @property
    def block(self) -> tendermint.types.block_pb2.Block:
        """Deprecated: please use `sdk_block` instead"""
    @property
    def sdk_block(self) -> cosmos.base.tendermint.v1beta1.types_pb2.Block:
        """Since: cosmos-sdk 0.47"""
    def __init__(
        self,
        *,
        block_id: tendermint.types.types_pb2.BlockID | None = ...,
        block: tendermint.types.block_pb2.Block | None = ...,
        sdk_block: cosmos.base.tendermint.v1beta1.types_pb2.Block | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["block", b"block", "block_id", b"block_id", "sdk_block", b"sdk_block"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["block", b"block", "block_id", b"block_id", "sdk_block", b"sdk_block"]) -> None: ...

global___GetBlockByHeightResponse = GetBlockByHeightResponse

@typing_extensions.final
class GetLatestBlockRequest(google.protobuf.message.Message):
    """GetLatestBlockRequest is the request type for the Query/GetLatestBlock RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___GetLatestBlockRequest = GetLatestBlockRequest

@typing_extensions.final
class GetLatestBlockResponse(google.protobuf.message.Message):
    """GetLatestBlockResponse is the response type for the Query/GetLatestBlock RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BLOCK_ID_FIELD_NUMBER: builtins.int
    BLOCK_FIELD_NUMBER: builtins.int
    SDK_BLOCK_FIELD_NUMBER: builtins.int
    @property
    def block_id(self) -> tendermint.types.types_pb2.BlockID: ...
    @property
    def block(self) -> tendermint.types.block_pb2.Block:
        """Deprecated: please use `sdk_block` instead"""
    @property
    def sdk_block(self) -> cosmos.base.tendermint.v1beta1.types_pb2.Block:
        """Since: cosmos-sdk 0.47"""
    def __init__(
        self,
        *,
        block_id: tendermint.types.types_pb2.BlockID | None = ...,
        block: tendermint.types.block_pb2.Block | None = ...,
        sdk_block: cosmos.base.tendermint.v1beta1.types_pb2.Block | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["block", b"block", "block_id", b"block_id", "sdk_block", b"sdk_block"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["block", b"block", "block_id", b"block_id", "sdk_block", b"sdk_block"]) -> None: ...

global___GetLatestBlockResponse = GetLatestBlockResponse

@typing_extensions.final
class GetSyncingRequest(google.protobuf.message.Message):
    """GetSyncingRequest is the request type for the Query/GetSyncing RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___GetSyncingRequest = GetSyncingRequest

@typing_extensions.final
class GetSyncingResponse(google.protobuf.message.Message):
    """GetSyncingResponse is the response type for the Query/GetSyncing RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SYNCING_FIELD_NUMBER: builtins.int
    syncing: builtins.bool
    def __init__(
        self,
        *,
        syncing: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["syncing", b"syncing"]) -> None: ...

global___GetSyncingResponse = GetSyncingResponse

@typing_extensions.final
class GetNodeInfoRequest(google.protobuf.message.Message):
    """GetNodeInfoRequest is the request type for the Query/GetNodeInfo RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___GetNodeInfoRequest = GetNodeInfoRequest

@typing_extensions.final
class GetNodeInfoResponse(google.protobuf.message.Message):
    """GetNodeInfoResponse is the response type for the Query/GetNodeInfo RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEFAULT_NODE_INFO_FIELD_NUMBER: builtins.int
    APPLICATION_VERSION_FIELD_NUMBER: builtins.int
    @property
    def default_node_info(self) -> tendermint.p2p.types_pb2.DefaultNodeInfo: ...
    @property
    def application_version(self) -> global___VersionInfo: ...
    def __init__(
        self,
        *,
        default_node_info: tendermint.p2p.types_pb2.DefaultNodeInfo | None = ...,
        application_version: global___VersionInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["application_version", b"application_version", "default_node_info", b"default_node_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["application_version", b"application_version", "default_node_info", b"default_node_info"]) -> None: ...

global___GetNodeInfoResponse = GetNodeInfoResponse

@typing_extensions.final
class VersionInfo(google.protobuf.message.Message):
    """VersionInfo is the type for the GetNodeInfoResponse message."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    APP_NAME_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    GIT_COMMIT_FIELD_NUMBER: builtins.int
    BUILD_TAGS_FIELD_NUMBER: builtins.int
    GO_VERSION_FIELD_NUMBER: builtins.int
    BUILD_DEPS_FIELD_NUMBER: builtins.int
    COSMOS_SDK_VERSION_FIELD_NUMBER: builtins.int
    name: builtins.str
    app_name: builtins.str
    version: builtins.str
    git_commit: builtins.str
    build_tags: builtins.str
    go_version: builtins.str
    @property
    def build_deps(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Module]: ...
    cosmos_sdk_version: builtins.str
    """Since: cosmos-sdk 0.43"""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        app_name: builtins.str = ...,
        version: builtins.str = ...,
        git_commit: builtins.str = ...,
        build_tags: builtins.str = ...,
        go_version: builtins.str = ...,
        build_deps: collections.abc.Iterable[global___Module] | None = ...,
        cosmos_sdk_version: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["app_name", b"app_name", "build_deps", b"build_deps", "build_tags", b"build_tags", "cosmos_sdk_version", b"cosmos_sdk_version", "git_commit", b"git_commit", "go_version", b"go_version", "name", b"name", "version", b"version"]) -> None: ...

global___VersionInfo = VersionInfo

@typing_extensions.final
class Module(google.protobuf.message.Message):
    """Module is the type for VersionInfo"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PATH_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    SUM_FIELD_NUMBER: builtins.int
    path: builtins.str
    """module path"""
    version: builtins.str
    """module version"""
    sum: builtins.str
    """checksum"""
    def __init__(
        self,
        *,
        path: builtins.str = ...,
        version: builtins.str = ...,
        sum: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["path", b"path", "sum", b"sum", "version", b"version"]) -> None: ...

global___Module = Module

@typing_extensions.final
class ABCIQueryRequest(google.protobuf.message.Message):
    """ABCIQueryRequest defines the request structure for the ABCIQuery gRPC query."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_FIELD_NUMBER: builtins.int
    PATH_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int
    PROVE_FIELD_NUMBER: builtins.int
    data: builtins.bytes
    path: builtins.str
    height: builtins.int
    prove: builtins.bool
    def __init__(
        self,
        *,
        data: builtins.bytes = ...,
        path: builtins.str = ...,
        height: builtins.int = ...,
        prove: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["data", b"data", "height", b"height", "path", b"path", "prove", b"prove"]) -> None: ...

global___ABCIQueryRequest = ABCIQueryRequest

@typing_extensions.final
class ABCIQueryResponse(google.protobuf.message.Message):
    """ABCIQueryResponse defines the response structure for the ABCIQuery gRPC query.

    Note: This type is a duplicate of the ResponseQuery proto type defined in
    Tendermint.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CODE_FIELD_NUMBER: builtins.int
    LOG_FIELD_NUMBER: builtins.int
    INFO_FIELD_NUMBER: builtins.int
    INDEX_FIELD_NUMBER: builtins.int
    KEY_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    PROOF_OPS_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int
    CODESPACE_FIELD_NUMBER: builtins.int
    code: builtins.int
    log: builtins.str
    """nondeterministic"""
    info: builtins.str
    """nondeterministic"""
    index: builtins.int
    key: builtins.bytes
    value: builtins.bytes
    @property
    def proof_ops(self) -> global___ProofOps: ...
    height: builtins.int
    codespace: builtins.str
    def __init__(
        self,
        *,
        code: builtins.int = ...,
        log: builtins.str = ...,
        info: builtins.str = ...,
        index: builtins.int = ...,
        key: builtins.bytes = ...,
        value: builtins.bytes = ...,
        proof_ops: global___ProofOps | None = ...,
        height: builtins.int = ...,
        codespace: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["proof_ops", b"proof_ops"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["code", b"code", "codespace", b"codespace", "height", b"height", "index", b"index", "info", b"info", "key", b"key", "log", b"log", "proof_ops", b"proof_ops", "value", b"value"]) -> None: ...

global___ABCIQueryResponse = ABCIQueryResponse

@typing_extensions.final
class ProofOp(google.protobuf.message.Message):
    """ProofOp defines an operation used for calculating Merkle root. The data could
    be arbitrary format, providing necessary data for example neighbouring node
    hash.

    Note: This type is a duplicate of the ProofOp proto type defined in Tendermint.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TYPE_FIELD_NUMBER: builtins.int
    KEY_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    type: builtins.str
    key: builtins.bytes
    data: builtins.bytes
    def __init__(
        self,
        *,
        type: builtins.str = ...,
        key: builtins.bytes = ...,
        data: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["data", b"data", "key", b"key", "type", b"type"]) -> None: ...

global___ProofOp = ProofOp

@typing_extensions.final
class ProofOps(google.protobuf.message.Message):
    """ProofOps is Merkle proof defined by the list of ProofOps.

    Note: This type is a duplicate of the ProofOps proto type defined in Tendermint.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPS_FIELD_NUMBER: builtins.int
    @property
    def ops(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ProofOp]: ...
    def __init__(
        self,
        *,
        ops: collections.abc.Iterable[global___ProofOp] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["ops", b"ops"]) -> None: ...

global___ProofOps = ProofOps
