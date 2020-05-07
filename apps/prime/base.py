# -*- coding: utf-8 -*-
import time

from locust import TaskSequence
from locust import task
from locust import events

from bravado.swagger_model import load_file
from bravado.client import SwaggerClient
from bravado.requests_client import RequestsClient

from bravado_core.formatter import SwaggerFormat
from bravado_core.exception import SwaggerMappingError
from bravado.exception import HTTPError

from asn1crypto import x509
from PyKCS11 import *


import requests

from cryptography.hazmat.primitives.serialization.pkcs12 import load_key_and_certificates
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, NoEncryption
from cryptography.hazmat.backends import default_backend
from requests_toolbelt.adapters.x509 import X509Adapter


from OpenSSL import crypto

def get_swagger_config():
    """
    Generate the config used in generating the swagger client from the spec
    """

    # MilMove uses custom formats for some fields. Without wanting to duplicate them here but
    # still wanting to not get warnings about them being undefined the UDFs are created here.
    # See https://bravado-core.readthedocs.io/en/stable/formats.html
    milmove_formats = []
    string_fmt_list = [
        "basequantity",
        "cents",
        "edipi",
        "millicents",
        "mime-type",
        "ssn",
        "telephone",
        "uri",
        "uuid",
        "x-email",
        "zip",
    ]
    for fmt in string_fmt_list:
        swagger_fmt = SwaggerFormat(
            format=fmt,
            to_wire=str,
            to_python=str,
            validate=lambda x: x,
            description="Converts [wire]string:string <=> python string",
        )
        milmove_formats.append(swagger_fmt)
        
    # local_cert = (
    #     "./config/tls/devlocal-mtls.cer",
    #     "./config/tls/devlocal-mtls.key",
    # )
    # self.requests_client = (ssl_verify=False, ssl_cert=self.local_cert)


    swagger_config = {
        # Validate our own requests to catch any problems with python type conversions
        "validate_requests": False,
        # Many of our payloads have invalid responses per the spec because of OpenAPI 2.0 issues
        "validate_responses": False,
        # "formats": milmove_formats
        # doesnt like definitions and responses toogether,
        "validate_swagger_spec": False,
        "use_models": False,
        # "ssl_verify": False, 
        # "ssl_cert": local_cert
    }
    return swagger_config

def swagger_request(callable_operation, *args, **kwargs):
    """
    Swagger client uses requests send() method instead of request(). This means we need to send off
    events to Locust on our own.
    """
    method = callable_operation.operation.http_method.upper()
    path_name = callable_operation.operation.path_name
    response_future = callable_operation(*args, **kwargs)
    try:
        start_time = time.time()
        response = response_future.response()
    except HTTPError as e:
        events.request_failure.fire(
            request_type=method,
            name=path_name,
            response_time=time.time() - start_time,
            exception=e,
        )
        print(e.response)
        return e.swagger_result
    except SwaggerMappingError as e:
        # Even though we don't return the result here we at least fire off the failure event
        events.request_failure.fire(
            request_type=method,
            name=path_name,
            response_time=time.time() - start_time,
            exception=e,
        )
        raise e
    else:
        metadata = response.metadata

        events.request_success.fire(
            request_type=method,
            name=path_name,
            response_time=metadata.elapsed_time,
            response_length=len(metadata.incoming_response.raw_bytes),
        )
        # this is equivalent to json.loads(metadata.incoming_response.text)
        return response.result

def card_cert(cert):
    # go code
    # https://github.com/paultag/go-pksigner/blob/master/pkcs11.go
    # https://github.com/paultag/go-piv/blob/master/certificate.go
    if cert:
        return cert
    else:
        
        pkcs11 = PyKCS11Lib()
        lib_path = "/usr/local/lib/pkcs11/opensc-pkcs11.so"
        pkcs11.load(lib_path)

        # get 1st slot
        slot = pkcs11.getSlotList(tokenPresent=True)[0]

        session = pkcs11.openSession(slot, CKF_SERIAL_SESSION | CKF_RW_SESSION)
        pin = os.getenv('PIN')
        print (pin)
        session.login(pin)

        cert_label = "Certificate for PIV Authentication"
        # private_key_label = "PIV AUTH key"
        results = []
        certs = session.findObjects([(CKA_CLASS, CKO_CERTIFICATE)])
        pub_key = session.findObjects([(CKA_CLASS, CKO_PUBLIC_KEY)])
        priv_key = session.findObjects([(CKA_CLASS, CKO_PRIVATE_KEY)])

        print("keys")
        print (pub_key)
        print (priv_key)

        # label = session.findObjects([(CKA_LABEL, CKA_CLASS)])
        # print("label")
        # print(label)

        for cert in certs:
            print("&&&&&&&&")
            # print(cert)

            cka_label, cka_value, cka_id = session.getAttributeValue(cert, [CKA_LABEL, CKA_VALUE, CKA_ID])
            cert_der = bytes(cka_value)
            # cert_x509 = x509.Certificate.load(cert_der)
            cert12 = crypto.load_certificate(
                crypto.FILETYPE_ASN1,
                cert_der,
            )
            subject = cert12.get_subject()
            print(subject)

            cert13 = crypto.dump_certificate(
                crypto.FILETYPE_PEM,
                cert12
            )


            f = open("./tmp/my.pem", "wb")
            f.write(cert13)
            f.close()

            print(cert13)            
            return cert13

            # return (results[0], results[1])
            # return results[1]

class BaseTaskSequence(TaskSequence):
    local_cert = (
        "./config/tls/devlocal-mtls.cer",
        "./config/tls/devlocal-mtls.key",
    )


