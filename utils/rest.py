# -*- coding: utf-8 -*-
"""
The code in this file helps us out with working with json endpoints and making REST requests.

The code in this file is based on `RestUser` from `locust-plugins`:
https://github.com/SvenskaSpel/locust-plugins/blob/master/locust_plugins/users/rest.py

Copyright 2019 Svenska Spel AB
From: https://github.com/SvenskaSpel/locust-plugins/blob/master/LICENSE
"""


def get_json_headers() -> dict[str, str]:
    """
    Returns default headers needed for JSON requests that expect to send and receive json.
    :return: dict of headers to include with json requests
    """
    return {"Content-Type": "application/json", "Accept": "application/json"}
