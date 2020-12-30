# -*- coding: utf-8 -*-
from tasks.base import check_response
from types import SimpleNamespace


def test_check_response():
    """
    1. Check that something is logged
    2. Check the return value (dict, bool)
    """
    response_object = {
        "moveTaskOrderID": "1f2270c7-7166-40ae-981e-b200ebdf3054",
        "id": "1f2270c7-7166-40ae-981e-b200ebdf3054",
        "createdAt": "2019-08-24T14:15:22Z",
        "agents": [],
        "status_code": 200,
        "content": '{"field": "value"}',
    }
    # response_object = {
    #     "status_code": 200,
    #     "content": '{"field": "value"}'
    # }
    get_all_data = SimpleNamespace(**response_object)

    assert check_response(get_all_data) == ({"field": "value"}, True)
