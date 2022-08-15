import logging

from .client import GrpcClient
from .common import TxConfig
from .network import Network
from .sdks.tx import TxClient
from .wallet import PrivateKey


class Sdk:
    """TODO docs

    Example:
    ```python
    sdk = (
        Sdk.authorize(val_mnemonic)
        .with_config(tx_config)
        .with_network(network, network_insecure)
    )
    ```
    """

    def __init__(self, _error_do_not_use_init_directly=None) -> None:
        """Unsupported, please use from_mnemonic to initialize."""
        if not _error_do_not_use_init_directly:
            raise TypeError("Please use PrivateKey.from_mnemonic() to construct me")
        self.priv_key: PrivateKey = None
        self.query = None
        self.tx = None
        self.network = None
        self.tx_config = TxConfig()

    @classmethod
    def authorize(cls, key: str = "") -> "Sdk":
        self = cls(_error_do_not_use_init_directly=True)
        if key == "":
            (mnemonic, pk) = PrivateKey.generate()
            logging.warning(
                "The mnemonic used for the newly generated key is: \n%s", mnemonic
            )
            logging.warning(
                "Please write down this key, it will NOT be recoverable otherwise"
            )
        if len(key.split(" ")) > 1:
            pk = PrivateKey.from_mnemonic(key)
        elif len(key) > 0:
            pk = PrivateKey.from_hex(key)

        self.with_priv_key(pk)

        return self

    def with_network(self, network: Network, insecure=False) -> "Sdk":
        self.network = network
        self.with_query_client(GrpcClient(self.network, insecure))
        return self

    def with_query_client(self, client: GrpcClient) -> "Sdk":
        self.query = client
        tx_client = TxClient(
            client=self.query,
            network=self.network,
            priv_key=self.priv_key,
            config=self.tx_config,
        )
        self.with_tx_client(tx_client)
        return self

    def with_tx_client(self, tx_client: TxClient) -> "Sdk":
        self.tx = tx_client
        return self

    def with_priv_key(self, priv_key: PrivateKey) -> "Sdk":
        self.priv_key = priv_key
        self.with_network(Network.local(), True)
        return self

    def with_config(self, config: TxConfig) -> "Sdk":
        self.tx_config = config
        tx_client = TxClient(
            client=self.query,
            network=self.network,
            priv_key=self.priv_key,
            config=self.tx_config,
        )
        self.with_tx_client(tx_client)
        return self

    @property
    def address(self) -> str:
        pub_key = self.priv_key.to_public_key()
        return pub_key.to_address().to_acc_bech32()
