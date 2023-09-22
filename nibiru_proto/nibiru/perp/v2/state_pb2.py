# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nibiru/perp/v2/state.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1anibiru/perp/v2/state.proto\x12\x0enibiru.perp.v2\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x1egoogle/protobuf/duration.proto\"\xf5\x08\n\x06Market\x12M\n\x04pair\x18\x01 \x01(\tB9\xc8\xde\x1f\x00\xda\xde\x1f\x31github.com/NibiruChain/nibiru/x/common/asset.PairR\x04pair\x12\x18\n\x07\x65nabled\x18\x02 \x01(\x08R\x07\x65nabled\x12h\n\x18maintenance_margin_ratio\x18\x03 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\x16maintenanceMarginRatio\x12Q\n\x0cmax_leverage\x18\x04 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\x0bmaxLeverage\x12{\n\"latest_cumulative_premium_fraction\x18\x05 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\x1flatestCumulativePremiumFraction\x12\\\n\x12\x65xchange_fee_ratio\x18\x06 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\x10\x65xchangeFeeRatio\x12g\n\x18\x65\x63osystem_fund_fee_ratio\x18\x07 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\x15\x65\x63osystemFundFeeRatio\x12\x62\n\x15liquidation_fee_ratio\x18\x08 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\x13liquidationFeeRatio\x12j\n\x19partial_liquidation_ratio\x18\t \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\x17partialLiquidationRatio\x12\x31\n\x15\x66unding_rate_epoch_id\x18\n \x01(\tR\x12\x66undingRateEpochId\x12U\n\x14twap_lookback_window\x18\x0b \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01R\x12twapLookbackWindow\x12I\n\x10prepaid_bad_debt\x18\x0c \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00R\x0eprepaidBadDebt\x12\\\n\x10max_funding_rate\x18\r \x01(\tB2\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x98\xdf\x1f\x01R\x0emaxFundingRate\"\xc6\x04\n\x03\x41MM\x12M\n\x04pair\x18\x01 \x01(\tB9\xc8\xde\x1f\x00\xda\xde\x1f\x31github.com/NibiruChain/nibiru/x/common/asset.PairR\x04pair\x12Q\n\x0c\x62\x61se_reserve\x18\x02 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\x0b\x62\x61seReserve\x12S\n\rquote_reserve\x18\x03 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\x0cquoteReserve\x12M\n\nsqrt_depth\x18\x04 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\tsqrtDepth\x12Y\n\x10price_multiplier\x18\x05 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\x0fpriceMultiplier\x12M\n\ntotal_long\x18\x06 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\ttotalLong\x12O\n\x0btotal_short\x18\x07 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\ntotalShort\"\x99\x04\n\x08Position\x12%\n\x0etrader_address\x18\x01 \x01(\tR\rtraderAddress\x12M\n\x04pair\x18\x02 \x01(\tB9\xc8\xde\x1f\x00\xda\xde\x1f\x31github.com/NibiruChain/nibiru/x/common/asset.PairR\x04pair\x12\x42\n\x04size\x18\x03 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\x04size\x12\x46\n\x06margin\x18\x04 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\x06margin\x12S\n\ropen_notional\x18\x05 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\x0copenNotional\x12{\n\"latest_cumulative_premium_fraction\x18\x06 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\x1flatestCumulativePremiumFraction\x12\x39\n\x19last_updated_block_number\x18\x07 \x01(\x03R\x16lastUpdatedBlockNumber\"a\n\x0fReserveSnapshot\x12+\n\x03\x61mm\x18\x01 \x01(\x0b\x32\x13.nibiru.perp.v2.AMMB\x04\xc8\xde\x1f\x00R\x03\x61mm\x12!\n\x0ctimestamp_ms\x18\x02 \x01(\x03R\x0btimestampMs*;\n\tDirection\x12\x19\n\x15\x44IRECTION_UNSPECIFIED\x10\x00\x12\x08\n\x04LONG\x10\x01\x12\t\n\x05SHORT\x10\x02*g\n\x0eTwapCalcOption\x12 \n\x1cTWAP_CALC_OPTION_UNSPECIFIED\x10\x00\x12\x08\n\x04SPOT\x10\x01\x12\x14\n\x10QUOTE_ASSET_SWAP\x10\x02\x12\x13\n\x0f\x42\x41SE_ASSET_SWAP\x10\x03\x42/Z-github.com/NibiruChain/nibiru/x/perp/v2/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nibiru.perp.v2.state_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z-github.com/NibiruChain/nibiru/x/perp/v2/types'
  _MARKET.fields_by_name['pair']._options = None
  _MARKET.fields_by_name['pair']._serialized_options = b'\310\336\037\000\332\336\0371github.com/NibiruChain/nibiru/x/common/asset.Pair'
  _MARKET.fields_by_name['maintenance_margin_ratio']._options = None
  _MARKET.fields_by_name['maintenance_margin_ratio']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _MARKET.fields_by_name['max_leverage']._options = None
  _MARKET.fields_by_name['max_leverage']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _MARKET.fields_by_name['latest_cumulative_premium_fraction']._options = None
  _MARKET.fields_by_name['latest_cumulative_premium_fraction']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _MARKET.fields_by_name['exchange_fee_ratio']._options = None
  _MARKET.fields_by_name['exchange_fee_ratio']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _MARKET.fields_by_name['ecosystem_fund_fee_ratio']._options = None
  _MARKET.fields_by_name['ecosystem_fund_fee_ratio']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _MARKET.fields_by_name['liquidation_fee_ratio']._options = None
  _MARKET.fields_by_name['liquidation_fee_ratio']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _MARKET.fields_by_name['partial_liquidation_ratio']._options = None
  _MARKET.fields_by_name['partial_liquidation_ratio']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _MARKET.fields_by_name['twap_lookback_window']._options = None
  _MARKET.fields_by_name['twap_lookback_window']._serialized_options = b'\310\336\037\000\230\337\037\001'
  _MARKET.fields_by_name['prepaid_bad_debt']._options = None
  _MARKET.fields_by_name['prepaid_bad_debt']._serialized_options = b'\310\336\037\000'
  _MARKET.fields_by_name['max_funding_rate']._options = None
  _MARKET.fields_by_name['max_funding_rate']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\230\337\037\001'
  _AMM.fields_by_name['pair']._options = None
  _AMM.fields_by_name['pair']._serialized_options = b'\310\336\037\000\332\336\0371github.com/NibiruChain/nibiru/x/common/asset.Pair'
  _AMM.fields_by_name['base_reserve']._options = None
  _AMM.fields_by_name['base_reserve']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _AMM.fields_by_name['quote_reserve']._options = None
  _AMM.fields_by_name['quote_reserve']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _AMM.fields_by_name['sqrt_depth']._options = None
  _AMM.fields_by_name['sqrt_depth']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _AMM.fields_by_name['price_multiplier']._options = None
  _AMM.fields_by_name['price_multiplier']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _AMM.fields_by_name['total_long']._options = None
  _AMM.fields_by_name['total_long']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _AMM.fields_by_name['total_short']._options = None
  _AMM.fields_by_name['total_short']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _POSITION.fields_by_name['pair']._options = None
  _POSITION.fields_by_name['pair']._serialized_options = b'\310\336\037\000\332\336\0371github.com/NibiruChain/nibiru/x/common/asset.Pair'
  _POSITION.fields_by_name['size']._options = None
  _POSITION.fields_by_name['size']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _POSITION.fields_by_name['margin']._options = None
  _POSITION.fields_by_name['margin']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _POSITION.fields_by_name['open_notional']._options = None
  _POSITION.fields_by_name['open_notional']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _POSITION.fields_by_name['latest_cumulative_premium_fraction']._options = None
  _POSITION.fields_by_name['latest_cumulative_premium_fraction']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _RESERVESNAPSHOT.fields_by_name['amm']._options = None
  _RESERVESNAPSHOT.fields_by_name['amm']._serialized_options = b'\310\336\037\000'
  _DIRECTION._serialized_start=2527
  _DIRECTION._serialized_end=2586
  _TWAPCALCOPTION._serialized_start=2588
  _TWAPCALCOPTION._serialized_end=2691
  _MARKET._serialized_start=160
  _MARKET._serialized_end=1301
  _AMM._serialized_start=1304
  _AMM._serialized_end=1886
  _POSITION._serialized_start=1889
  _POSITION._serialized_end=2426
  _RESERVESNAPSHOT._serialized_start=2428
  _RESERVESNAPSHOT._serialized_end=2525
# @@protoc_insertion_point(module_scope)
