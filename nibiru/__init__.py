import sys

try:
    if sys.version_info >= (3, 8):
        from importlib.metadata import version

        __version__ = version(__package__ or __name__)
    else:
        import pkg_resources

        __version__ = pkg_resources.get_distribution(__package__ or __name__).version
except Exception:
    pass

import google.protobuf.message

ProtobufMessage = google.protobuf.message.Message

import nibiru.exceptions  # noqa
import nibiru.pytypes  # noqa
from nibiru.grpc_client import GrpcClient  # noqa
from nibiru.msg import Msg  # noqa
from nibiru.network import Network  # noqa
from nibiru.pytypes import Coin, Direction, PoolAsset, Side, TxConfig, TxType  # noqa
from nibiru.sdk import Sdk  # noqa
from nibiru.transaction import Transaction  # noqa
from nibiru.wallet import Address, PrivateKey, PublicKey  # noqa
