# -*- coding: utf-8 -*-
import requests

from cryptography.hazmat.primitives.serialization.pkcs12 import (
    load_key_and_certificates,
)
from cryptography.hazmat.primitives.serialization import (
    Encoding,
    PrivateFormat,
    NoEncryption,
)
from cryptography.hazmat.backends import default_backend
from requests_toolbelt.adapters.x509 import X509Adapter

from asn1crypto import x509
from PyKCS11 import *

from OpenSSL import crypto


def card_to_pem(cert_der):
    cert12 = crypto.load_certificate(crypto.FILETYPE_ASN1, cert_der,)
    subject = cert12.get_subject()
    # print(subject)

    cert13 = crypto.dump_certificate(crypto.FILETYPE_PEM, cert12)
    cert13_str = cert13.decode("utf-8")
    return cert13_str


def get_cac():
    pkcs11 = PyKCS11Lib()
    lib_path = "/usr/local/lib/pkcs11/opensc-pkcs11.so"
    pkcs11.load(lib_path)

    # get 1st slot
    slot = pkcs11.getSlotList(tokenPresent=True)[0]

    session = pkcs11.openSession(slot, CKF_SERIAL_SESSION | CKF_RW_SESSION)
    pin = os.getenv("PIN")
    print(pin)
    session.login(pin)

    cert_label = "Certificate for PIV Authentication"
    # private_key_label = "PIV AUTH key"
    results = []
    certs = session.findObjects([(CKA_CLASS, CKO_CERTIFICATE)])
    pub_key = session.findObjects([(CKA_CLASS, CKO_PUBLIC_KEY)])
    priv_key = session.findObjects([(CKA_CLASS, CKO_PRIVATE_KEY)])

    for c in certs:
        print("CERT")
        print(c)

    for k in pub_key:
        print("PUB KEY")
        print(k)

    for k in priv_key:
        print("PRIV KEY")
        print(k)
    # label = session.findObjects([(CKA_LABEL, CKA_CLASS)])
    # print("label")
    # print(label)
    # f = open("./tmp/my2.pem", "wb")
    # for cert in certs:
    # 	print("\n\n&&&&&&&&")
    # 	print(cert)

    # 	cka_label, cka_value, cka_id = session.getAttributeValue(cert, [CKA_LABEL, CKA_VALUE, CKA_ID])
    # 	print("value...")
    # 	print(cka_value)
    # 	cert_der = bytes(cka_value)

    # 	cert12 = crypto.load_certificate(
    # 		crypto.FILETYPE_ASN1,
    # 		cert_der,
    # 	)
    # 	subject = cert12.get_subject()
    # 	# print(subject)

    # 	cert13 = crypto.dump_certificate(
    # 		crypto.FILETYPE_PEM,
    # 		cert12
    # 	)
    # 	# cert13_str = cert13.decode("utf-8")
    # 	# print(cert13_str)

    # 	f.write(cert13)

    # for key in pub_key:
    # 	print("\n\n+++++++++++++")
    # 	print(key)

    # 	cka_label, cka_value, cka_id = session.getAttributeValue(key, [CKA_LABEL, CKA_VALUE, CKA_ID])
    # 	cert_der = bytes(cka_value)

    # 	cert12 = crypto.load_publickey(
    # 		crypto.FILETYPE_ASN1,
    # 		cert_der,
    # 	)
    # 	# subject = cert12.get_subject()
    # 	# print(subject)

    # 	cert13 = crypto.dump_publickey(
    # 		crypto.FILETYPE_PEM,
    # 		cert12
    # 	)
    # 	# cert13_str = cert13.decode("utf-8")
    # 	f.write(cert13)

    # # for key in priv_key:
    # # 	print("\n\n@@@@@@@@@@")
    # # 	print(key)

    # # 	cka_label, cka_value, cka_id = session.getAttributeValue(key, [CKA_LABEL, CKA_VALUE, CKA_ID])
    # # 	if CKA_VALUE:
    # # 		cert_der = bytes(cka_value)

    # # 		cert12 = crypto.load_publickey(
    # # 			crypto.FILETYPE_ASN1,
    # # 			cert_der,
    # # 		)
    # # 		# subject = cert12.get_subject()
    # # 		# print(subject)

    # # 		cert13 = crypto.dump_publickey(
    # # 			crypto.FILETYPE_PEM,
    # # 			cert12
    # # 		)
    # # 		cert13_str = cert13.decode("utf-8")
    # # 		f.write(cert13_str)

    # f.close()
    # return 'asdf'


backend = default_backend()
cert12 = get_cac()
print("abc 123")
print(cert12)


# with open('test_cert.p12', 'rb') as pkcs12_file:
# 	pkcs12_data = pkcs12_file.read()

# pkcs12_password_bytes = "test".encode('utf8')

# pycaP12 = load_key_and_certificates(pkcs12_data, pkcs12_password_bytes, backend)


# cert_bytes = pycaP12[1].public_bytes(Encoding.DER)
# pk_bytes = pycaP12[0].private_bytes(Encoding.DER, PrivateFormat.PKCS8, NoEncryption())

# adapter = X509Adapter(max_retries=3, cert_bytes=cert_bytes, pk_bytes=pk_bytes, encoding=Encoding.DER)
# session = requests.Session()
# session.mount('https://', adapter)

# r = session.get('https://api.experimental.move.mil/prime/v1/move-task-orders', verify=False)
