# -*- coding: utf-8 -*-
from requests_toolbelt.adapters.ssl import SSLAdapter

import requests
import ssl

s = requests.Session()
s.mount("https://github.com/", SSLAdapter(ssl.PROTOCOL_TLSv1))

print("abc")
