"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.any_pb2
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
class BaseAccount(google.protobuf.message.Message):
    """BaseAccount defines a base account type. It contains all the necessary fields
    for basic account functionality. Any custom account type should extend this
    type for additional functionality (e.g. vesting).
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESS_FIELD_NUMBER: builtins.int
    PUB_KEY_FIELD_NUMBER: builtins.int
    ACCOUNT_NUMBER_FIELD_NUMBER: builtins.int
    SEQUENCE_FIELD_NUMBER: builtins.int
    address: builtins.str
    @property
    def pub_key(self) -> google.protobuf.any_pb2.Any: ...
    account_number: builtins.int
    sequence: builtins.int
    def __init__(
        self,
        *,
        address: builtins.str = ...,
        pub_key: google.protobuf.any_pb2.Any | None = ...,
        account_number: builtins.int = ...,
        sequence: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pub_key", b"pub_key"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["account_number", b"account_number", "address", b"address", "pub_key", b"pub_key", "sequence", b"sequence"]) -> None: ...

global___BaseAccount = BaseAccount

@typing_extensions.final
class ModuleAccount(google.protobuf.message.Message):
    """ModuleAccount defines an account for modules that holds coins on a pool."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BASE_ACCOUNT_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    PERMISSIONS_FIELD_NUMBER: builtins.int
    @property
    def base_account(self) -> global___BaseAccount: ...
    name: builtins.str
    @property
    def permissions(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        base_account: global___BaseAccount | None = ...,
        name: builtins.str = ...,
        permissions: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["base_account", b"base_account"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["base_account", b"base_account", "name", b"name", "permissions", b"permissions"]) -> None: ...

global___ModuleAccount = ModuleAccount

@typing_extensions.final
class ModuleCredential(google.protobuf.message.Message):
    """ModuleCredential represents a unclaimable pubkey for base accounts controlled by modules.

    Since: cosmos-sdk 0.47
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MODULE_NAME_FIELD_NUMBER: builtins.int
    DERIVATION_KEYS_FIELD_NUMBER: builtins.int
    module_name: builtins.str
    """module_name is the name of the module used for address derivation (passed into address.Module)."""
    @property
    def derivation_keys(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bytes]:
        """derivation_keys is for deriving a module account address (passed into address.Module)
        adding more keys creates sub-account addresses (passed into address.Derive)
        """
    def __init__(
        self,
        *,
        module_name: builtins.str = ...,
        derivation_keys: collections.abc.Iterable[builtins.bytes] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["derivation_keys", b"derivation_keys", "module_name", b"module_name"]) -> None: ...

global___ModuleCredential = ModuleCredential

@typing_extensions.final
class Params(google.protobuf.message.Message):
    """Params defines the parameters for the auth module."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MAX_MEMO_CHARACTERS_FIELD_NUMBER: builtins.int
    TX_SIG_LIMIT_FIELD_NUMBER: builtins.int
    TX_SIZE_COST_PER_BYTE_FIELD_NUMBER: builtins.int
    SIG_VERIFY_COST_ED25519_FIELD_NUMBER: builtins.int
    SIG_VERIFY_COST_SECP256K1_FIELD_NUMBER: builtins.int
    max_memo_characters: builtins.int
    tx_sig_limit: builtins.int
    tx_size_cost_per_byte: builtins.int
    sig_verify_cost_ed25519: builtins.int
    sig_verify_cost_secp256k1: builtins.int
    def __init__(
        self,
        *,
        max_memo_characters: builtins.int = ...,
        tx_sig_limit: builtins.int = ...,
        tx_size_cost_per_byte: builtins.int = ...,
        sig_verify_cost_ed25519: builtins.int = ...,
        sig_verify_cost_secp256k1: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["max_memo_characters", b"max_memo_characters", "sig_verify_cost_ed25519", b"sig_verify_cost_ed25519", "sig_verify_cost_secp256k1", b"sig_verify_cost_secp256k1", "tx_sig_limit", b"tx_sig_limit", "tx_size_cost_per_byte", b"tx_size_cost_per_byte"]) -> None: ...

global___Params = Params
