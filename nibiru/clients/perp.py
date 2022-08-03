from grpc import Channel

from nibiru.proto.perp.v1 import query_pb2 as perp_type
from nibiru.proto.perp.v1 import query_pb2_grpc as perp_query
from google.protobuf.json_format import MessageToDict
from nibiru.utils import from_sdk_dec, from_sdk_dec_24

from .util import deserialize


class Perp:
    """
    Perp allows to query the endpoints made available by the Nibiru Chain's PERP module.
    """

    def __init__(self, channel: Channel):
        self.api = perp_query.QueryStub(channel)

    def params(self):
        """
        Get the parameters of the perp module.

        Output sample:
            {
                "maintenanceMarginRatio": 0.0625,
                "feePoolFeeRatio": 0.001,
                "ecosystemFundFeeRatio": 0.001,
                "liquidationFeeRatio": 0.025,
                "partialLiquidationRatio": 0.25,
                "epochIdentifier": "30 min",
                "twapLookbackWindow": "900s"
            }

        Returns:
            dict: The current parameters for the perpetual module
        """
        proto_output: perp_type.QueryParamsResponse = self.api.Params(perp_type.QueryParamsRequest())
        output = MessageToDict(proto_output)["params"]

        sdk_dec_fields = [
            "maintenanceMarginRatio",
            "feePoolFeeRatio",
            "ecosystemFundFeeRatio",
            "liquidationFeeRatio",
            "partialLiquidationRatio",
        ]

        for field in sdk_dec_fields:
            output[field] = from_sdk_dec(output[field])

        return output

    def trader_position(self, token_pair: str, trader: str) -> dict:
        """
        Get the trader position. Returns information about position notional, margin ratio
        unrealized pnl, size of the position etc.

        Args:
            token_pair (str): The token pair
            trader (str): The trader address

        Sample output:
            {
                "position": {
                    "traderAddress": "nibi1zaavvzxez0elund",
                    "pair": {
                        "token0": "axlwbtc",
                        "token1": "unusd"
                    },
                    "size": 11.241446725317692,
                    "margin": 45999.99999999999,
                    "openNotional": 230000.0,
                    "lastUpdateCumulativePremiumFraction": "0",
                    "blockNumber": "278"
                },
                "positionNotional": 230000.0,
                "unrealizedPnl": 1.024e-20,
                "marginRatio": 0.2
            }

        Returns:
            dict: The output of the query
        """
        req = perp_type.QueryTraderPositionRequest(
            token_pair=token_pair,
            trader=trader,
        )

        proto_output: perp_type.QueryTraderPositionResponse = self.api.TraderPosition(req)
        output = MessageToDict(proto_output)

        position_sdk_dec_fields = [
            "size",
            "margin",
            "openNotional",
        ]

        sdk_dec_fields = [
            "positionNotional",
            "unrealizedPnl",
        ]
        for field in position_sdk_dec_fields:
            output["position"][field] = from_sdk_dec_24(output["position"][field])

        for field in sdk_dec_fields:
            output[field] = from_sdk_dec_24(output[field])

        output["marginRatio"] = from_sdk_dec(output["marginRatio"])

        return output
