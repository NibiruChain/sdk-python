# stablecoin_test.py

import pysdk
from tests import dict_keys_must_match


def test_query_params(sdk_val: pysdk.Sdk):
    res = sdk_val.query.stablecoin.params()
    dict_keys_must_match(res, ["params"])
    dict_keys_must_match(
        res["params"],
        [
            "coll_ratio",
            "fee_ratio",
            "ef_fee_ratio",
            "bonus_rate_recoll",
            "distr_epoch_identifier",
            "adjustment_step",
            "price_lower_bound",
            "price_upper_bound",
            "is_collateral_ratio_valid",
        ],
    )


def test_query_circulating_supplies(sdk_val: pysdk.Sdk):
    res = sdk_val.query.stablecoin.circulating_supplies()
    assert isinstance(res, dict)
