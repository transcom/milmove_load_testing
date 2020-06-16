# -*- coding: utf-8 -*-
import os

STATIC_FILES = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "static")
LOCAL_MTLS_CERT = os.path.join(STATIC_FILES, "certs/devlocal-mtls.cer")
LOCAL_MTLS_KEY = os.path.join(STATIC_FILES, "certs/devlocal-mtls.key")

PRIME_CERT_KWARGS = {"cert": (LOCAL_MTLS_CERT, LOCAL_MTLS_KEY), "verify": False}
