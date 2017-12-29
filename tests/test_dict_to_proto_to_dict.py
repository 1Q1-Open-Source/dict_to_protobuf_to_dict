import copy
import pytest
from dict_to_protobuf_to_dict import dict_to_protobuf, protobuf_to_dict
from tests.sample_pb2 import MainMessage
from hypothesis import given, strategies

def _are_fields_in_proto_msg(message, fields=[]):
    name_map = {}
    for field, _ in message.ListFields():
        name_map[field.name] = None
    for field in fields:
        if field not in name_map:
            return False
    return True


@pytest.fixture
def setup_data():
    data_dct = {
        "a_str": "Neeraj Koul",
        "int_to_lst_ints_map": {1: {"lst_ints": [0, 1]}, 2: {"lst_ints": [2, 3]}, 3: {"lst_ints": [4, 5]}},
        "an_enum": "second",
        "an_int": 2,
        "lst_ints": [0, 1, 2],
        "str_to_message_map": {
            "where_from" : {"a_str": "Kashmir", "a_long": 1, "lst_longs": [1, 2, 3]}
        },
        "str_to_int_map": {"some_str": 1}
    }

    yield data_dct, data_dct.keys()

    # This would be your tearDown:
    data_dct = None


def test_all_populated(setup_data):
    data_dct, _ = setup_data
    msg = MainMessage()
    dict_to_protobuf(data_dct, msg)
    assert _are_fields_in_proto_msg(msg, data_dct.keys())
    dct = protobuf_to_dict(msg)
    assert dct == data_dct


def test_basic_scalar_manipulation(setup_data):
    data_dct, _ = setup_data
    data_dct.pop("a_str")
    data_dct.pop("an_int")
    msg = MainMessage()
    dict_to_protobuf(data_dct, msg)
    assert not _are_fields_in_proto_msg(msg, ["a_str", "an_int"])
    dct = protobuf_to_dict(msg)
    assert dct["a_str"] == ""
    assert dct["an_int"] == 0


def test_list_manipulation(setup_data):
    data_dct, _ = setup_data
    data_dct["lst_ints"] = []
    msg = MainMessage()
    dict_to_protobuf(data_dct, msg)
    assert not _are_fields_in_proto_msg(msg, ["lst_ints"])
    assert _are_fields_in_proto_msg(msg, ["a_str"])
    dct = protobuf_to_dict(msg)
    assert dct["lst_ints"] == []


def test_enum_manipulation(setup_data):
    data_dct, _ = setup_data
    data_dct["an_enum"] = "first"
    msg = MainMessage()
    dict_to_protobuf(data_dct, msg)
    assert not _are_fields_in_proto_msg(msg, ["an_enum"])
    dct = protobuf_to_dict(msg)
    assert dct["an_enum"] == "first"
    data_dct["an_enum"] = "second"
    msg = MainMessage()
    dict_to_protobuf(data_dct, msg)
    assert _are_fields_in_proto_msg(msg, ["an_enum"])


def test_map_manipulation(setup_data):
    data_dct, _ = setup_data
    data_dct["int_to_lst_ints_map"][1] = {}
    data_dct["int_to_lst_ints_map"].pop(2)
    data_dct["str_to_message_map"]["where_from"].pop("a_long")
    msg = MainMessage()
    dict_to_protobuf(data_dct, msg)
    assert 1 in getattr(msg, "int_to_lst_ints_map").keys()
    assert 2 not in getattr(msg, "int_to_lst_ints_map").keys()
    dct = protobuf_to_dict(msg)
    assert dct["int_to_lst_ints_map"][1] == {"lst_ints": []}
    assert dct["int_to_lst_ints_map"][3] == data_dct["int_to_lst_ints_map"][3]
    check_dct = {"a_str": "Kashmir", "lst_longs": [1, 2, 3], "a_long": 0}
    assert dct["str_to_message_map"]["where_from"] == check_dct


def test_serialising_data_which_is_not_part_of_schema(setup_data):
    data_dct, _ = setup_data
    data_dct_copy = copy.deepcopy(data_dct)
    data_dct["new_int"] = 11
    msg = MainMessage()
    dict_to_protobuf(data_dct, msg)
    assert not _are_fields_in_proto_msg(msg, ["new_int"])
    dct = protobuf_to_dict(msg)
    assert dct == data_dct_copy

