from asn1crypto import x509
from PyKCS11 import *

import requests



# 	tokenLabel := v.GetString(TokenLabelFlag)
# 	certLabel := v.GetString(CertLabelFlag)
# 	keyLabel := v.GetString(KeyLabelFlag)

# cert label: Certificate for PIV Authentication
# key label: PIV AUTH key

# https://github.com/paultag/go-pksigner/blob/master/pkcs11.go
# https://github.com/paultag/go-piv/blob/master/certificate.go
# TLSCertificate -> LoadCertificate -> GetCertificateTemplate -> 
# go run ./cmd/prime-api-client --cac --hostname api.experimental.move.mil --port 443 fetch-mtos | jq


pkcs11 = PyKCS11Lib()
lib_path = "/usr/local/lib/pkcs11/opensc-pkcs11.so"
pkcs11.load(lib_path)

# get 1st slot
slot = pkcs11.getSlotList(tokenPresent=True)[0]

session = pkcs11.openSession(slot, CKF_SERIAL_SESSION | CKF_RW_SESSION)
pin = os.getenv('PIN')
print (pin)
session.login(pin)

print("sessionInfo")
print(session.getSessionInfo())

cert_label = "Certificate for PIV Authentication"
# private_key_label = "PIV AUTH key"
results = []
certs = session.findObjects([(CKA_CLASS, CKO_CERTIFICATE)])
# print("certs")
# print (certs)

# label = session.findObjects([(CKA_LABEL, CKA_CLASS)])
# print("label")
# print(label)

for cert in certs:
	print("&&&&&&&&")
	print(cert)

	cka_label, cka_value, cka_id = session.getAttributeValue(cert, [CKA_LABEL, CKA_VALUE, CKA_ID])
	if cka_label == "Certificate for PIV Authentication":
		print (cka_label)
		cert_der = bytes(cka_value)
		cert_x509 = x509.Certificate.load(cert_der)


print (cert_x509)

# The PKCS#11 API is an abstract API to perform operations on cryptographic objects such as private keys, without requiring access to the objects themselves. That is, it provides a logical separation of the keys from the operations. The PKCS #11 API is mainly used to access objects in smart cards and Hardware or Software Security Modules (HSMs). That is because in these modules the cryptographic keys are isolated in hardware or software and are not made available to the applications using them.

# PKCS#11 API is an OASIS standard and it is supported by various hardware and software vendors. Usually, hardware vendors provide a PKCS#11 module to access their devices. A prominent example is the OpenSC PKCS #11 module which provides access to a variety of smart cards. Other libraries like NSS or GnuTLS already take advantage of PKCS #11 to access cryptographic objects.

# OpenSSL engines
# OpenSSL implements various cipher, digest, and signing features and it can consume and produce keys. However plenty of people think that these features should be implemented in separate hardware, like USB tokens, smart cards or hardware security modules. Therefore OpenSSL has an abstraction layer called "engine" which can delegate some of these features to different piece of software or hardware.

# engine_pkcs11 tries to fit the PKCS#11 API within the engine API of OpenSSL. That is, it provides a gateway between PKCS#11 modules and the OpenSSL engine API. One has to register the engine with OpenSSL and one has to provide the path to the PKCS#11 module which should be gatewayed to. This can be done by editing the OpenSSL configuration file, by engine specific controls, or by using the p11-kit proxy module.

# The p11-kit proxy module provides access to any configured PKCS #11 module in the system. See the p11-kit web pages for more information.

# PKCS #11 module configuration
# Copying the engine shared object to the proper location
# OpenSSL has a location where engine shared objects can be placed and they will be automatically loaded when requested. It is recommended to copy the engine_pkcs11 to that location as "libpkcs11.so" to ease usage. This is handle by 'make install' of engine_pkcs11.

# Using the engine from the command line
# In systems with p11-kit-proxy engine_pkcs11 has access to all the configured PKCS #11 modules and requires no further OpenSSL configuration. In systems without p11-kit-proxy you need to configure OpenSSL to know about the engine and to use OpenSC PKCS#11 module by the engine_pkcs11. For that you add something like the following into your global OpenSSL configuration file (often in /etc/ssl/openssl.cnf). This line must be placed at the top, before any sections are defined:

		# return cert_x509
	# 	results.append(cert)
	# print(len(results))


# for r in certs:
#     attr = session.getAttributeValue(r, [CKA_LABEL, CKA_CLASS])
#     print(attr)

# # print(result)

# for r in certs:




from requests import Session

from m2requests import M2HttpsAdapter

request = Session()
request.mount("https://", M2HttpsAdapter())
# PKCS#11 URI; REF: https://tools.ietf.org/html/rfc7512
request.cert=("pkcs11:type=cert;...", "pkcs11:type=private;...")
request.get("https://...")