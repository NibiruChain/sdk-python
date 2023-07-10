import time

import pysdk
import tests
from pysdk import Msg, event_specs, websocket
from pysdk.exceptions import QueryError, SimulationError


def get_validator_operator_address(sdk_val: pysdk.Sdk):
    """
    Return the first validator and delegator
    """
    validator = sdk_val.query.staking.validators()["validators"][0]
    return validator["operator_address"]


def delegate(sdk_val: pysdk.Sdk):
    return sdk_val.tx.execute_msgs(
        [
            Msg.staking.delegate(
                delegator_address=sdk_val.address,
                validator_address=get_validator_operator_address(sdk_val),
                amount=1,
            ),
        ],
    )


def undelegate(sdk_val: pysdk.Sdk):
    return sdk_val.tx.execute_msgs(
        [
            Msg.staking.undelegate(
                delegator_address=sdk_val.address,
                validator_address=get_validator_operator_address(sdk_val),
                amount=1,
            ),
        ],
    )


def test_query_vpool(sdk_val: pysdk.Sdk):
    query_resp = sdk_val.query.staking.pool()
    assert query_resp["pool"]["bonded_tokens"] >= 0
    assert query_resp["pool"]["not_bonded_tokens"] >= 0


def test_query_delegation(sdk_val: pysdk.Sdk):
    tests.broadcast_tx_must_succeed(delegate(sdk_val))
    query_resp = sdk_val.query.staking.delegation(
        sdk_val.address, get_validator_operator_address(sdk_val)
    )
    tests.dict_keys_must_match(
        query_resp["delegation_response"],
        [
            "delegation",
            "balance",
        ],
    )


def test_query_delegations(sdk_val: pysdk.Sdk):
    tests.broadcast_tx_must_succeed(delegate(sdk_val))
    query_resp = sdk_val.query.staking.delegations(sdk_val.address)
    tests.dict_keys_must_match(
        query_resp["delegation_responses"][0],
        [
            "delegation",
            "balance",
        ],
    )


def test_query_delegations_to(sdk_val: pysdk.Sdk):
    tests.broadcast_tx_must_succeed(delegate(sdk_val))
    query_resp = sdk_val.query.staking.delegations_to(
        get_validator_operator_address(sdk_val)
    )
    tests.dict_keys_must_match(
        query_resp["delegation_responses"][0],
        [
            "delegation",
            "balance",
        ],
    )


def test_historical_info(sdk_val: pysdk.Sdk):
    try:
        hist_info = sdk_val.query.staking.historical_info(1)
        if hist_info["hist"]["valset"]:
            tests.dict_keys_must_match(
                hist_info["hist"]["valset"][0],
                [
                    "operator_address",
                    "consensus_pubkey",
                    "jailed",
                    "status",
                    "tokens",
                    "delegator_shares",
                    "description",
                    "unbonding_height",
                    "unbonding_time",
                    "commission",
                    "min_self_delegation",
                    "unbonding_on_hold_ref_count",
                    "unbonding_ids",
                ],
            )
    except QueryError:
        pass


def test_params(sdk_val: pysdk.Sdk):
    query_resp = sdk_val.query.staking.params()
    tests.dict_keys_must_match(
        query_resp["params"],
        [
            "unbonding_time",
            "max_entries",
            "max_validators",
            "historical_entries",
            "bond_denom",
            "min_commission_rate",
        ],
    )


def test_redelegations(sdk_val: pysdk.Sdk):
    query_resp = sdk_val.query.staking.redelegations(
        sdk_val.address, get_validator_operator_address(sdk_val)
    )
    tests.dict_keys_must_match(query_resp, ["redelegation_responses", "pagination"])


def test_unbonding_delegation(sdk_val: pysdk.Sdk):
    tests.broadcast_tx_must_succeed(delegate(sdk_val))
    try:
        undelegate(sdk_val)
        query_resp = sdk_val.query.staking.unbonding_delegation(
            sdk_val.address, get_validator_operator_address(sdk_val)
        )
        if query_resp.get("unbonding_responses"):
            tests.dict_keys_must_match(
                query_resp["unbond"],
                ["delegator_address", "validator_address", "entries"],
            )
            assert len(query_resp["unbond"]["entries"]) > 0

    except BaseException as err:
        tests.raises(
            ok_errs=["too many unbonding", "Error on UnbondingDelegation"], err=err
        )


def test_unbonding_delegations(sdk_val: pysdk.Sdk):
    tests.broadcast_tx_must_succeed(delegate(sdk_val))
    try:
        undelegate(sdk_val)
    except SimulationError as ex:
        assert "too many unbonding" in ex.args[0]

    query_resp = sdk_val.query.staking.unbonding_delegations(sdk_val.address)

    tests.dict_keys_must_match(query_resp, ["unbonding_responses", "pagination"])
    if query_resp.get("unbonding_responses"):
        tests.dict_keys_must_match(
            query_resp["unbonding_responses"][0],
            ["delegator_address", "validator_address", "entries"],
        )
        assert len(query_resp["unbonding_responses"][0]["entries"]) > 0


def test_unbonding_delegations_from(sdk_val: pysdk.Sdk):
    tests.broadcast_tx_must_succeed(delegate(sdk_val))
    try:
        undelegate(sdk_val)
    except SimulationError as ex:
        assert "too many unbonding" in ex.args[0]

    query_resp = sdk_val.query.staking.unbonding_delegations_from(
        get_validator_operator_address(sdk_val)
    )

    tests.dict_keys_must_match(query_resp, ["unbonding_responses", "pagination"])
    if query_resp.get("unbonding_responses"):
        tests.dict_keys_must_match(
            query_resp["unbonding_responses"][0],
            ["delegator_address", "validator_address", "entries"],
        )
        assert len(query_resp["unbonding_responses"][0]["entries"]) > 0


def test_validators(sdk_val: pysdk.Sdk):
    query_resp = sdk_val.query.staking.validators()
    tests.dict_keys_must_match(query_resp, ["validators", "pagination"])
    assert query_resp["pagination"]["total"] > 0
    assert len(query_resp["validators"]) > 0
    tests.dict_keys_must_match(
        query_resp["validators"][0],
        [
            "operator_address",
            "consensus_pubkey",
            "jailed",
            "status",
            "tokens",
            "delegator_shares",
            "description",
            "unbonding_height",
            "unbonding_time",
            "commission",
            "min_self_delegation",
            "unbonding_on_hold_ref_count",
            "unbonding_ids",
        ],
    )


def test_validator(sdk_val: pysdk.Sdk):
    validator = sdk_val.query.staking.validators()["validators"][0]
    query_resp = sdk_val.query.staking.validator(validator["operator_address"])

    tests.dict_keys_must_match(
        query_resp["validator"],
        [
            "operator_address",
            "consensus_pubkey",
            "jailed",
            "status",
            "tokens",
            "delegator_shares",
            "description",
            "unbonding_height",
            "unbonding_time",
            "commission",
            "min_self_delegation",
            "unbonding_on_hold_ref_count",
            "unbonding_ids",
        ],
    )


def test_staking_events(sdk_val: pysdk.Sdk, network: pysdk.Network):
    """
    Check staking events are properly filtered
    """
    expected_events_tx = [event_specs.EventType.Delegate]
    expected_events = expected_events_tx

    ws = websocket.NibiruWebsocket(
        network,
        expected_events,
    )
    ws.start()
    time.sleep(1)

    delegate(sdk_val)
    time.sleep(5)
    success: bool = False
    ws.queue.put(None)
    while True:
        if ws.captured_event_types_map.get("delegate"):
            success = True  # Event Captured! Success
        event: event_specs.EventCaptured = ws.queue.get()
        time.sleep(1)
        if event is None:
            break
        elif event.event_type == "delegate":
            success = True  # Event Captured! Success
    assert success, "Message delegate captured"
