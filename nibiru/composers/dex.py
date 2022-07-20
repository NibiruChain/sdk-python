from typing import List

from nibiru.common import PoolAsset
from nibiru.proto.cosmos.base.v1beta1 import coin_pb2 as coin_pb
from nibiru.proto.dex.v1 import pool_pb2 as pool_tx_pb
from nibiru.proto.dex.v1 import tx_pb2 as dex_tx_pb


class Dex:
    @staticmethod
    def create_pool(creator: str, swap_fee: str, exit_fee: str, assets: List[PoolAsset]):
        pool_assets = [pool_tx_pb.PoolAsset(token=a.token, weight=a.weight) for a in assets]

        return dex_tx_pb.MsgCreatePool(
            creator=creator,
            pool_params=pool_tx_pb.PoolParams(swapFee=swap_fee, exitFee=exit_fee),
            pool_assets=pool_assets,
        )

    @staticmethod
    def join_pool(sender: str, pool_id: int, tokens: List[coin_pb.Coin]):
        return dex_tx_pb.MsgJoinPool(
            sender=sender,
            pool_id=pool_id,
            tokens_in=tokens,
        )

    @staticmethod
    def exit_pool(sender: str, pool_id: int, pool_shares: coin_pb.Coin):
        return dex_tx_pb.MsgExitPool(
            sender=sender,
            pool_id=pool_id,
            pool_shares=pool_shares,
        )

    @staticmethod
    def swap_assets(sender: str, pool_id: int, token_in: coin_pb.Coin, token_out_denom):
        return dex_tx_pb.MsgSwapAssets(
            sender=sender,
            pool_id=pool_id,
            token_in=token_in,
            token_out_denom=token_out_denom,
        )
