from asn1crypto import x509
from PyKCS11 import *


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
		return cert_x509
	# 	results.append(cert)
	# print(len(results))


# for r in certs:
#     attr = session.getAttributeValue(r, [CKA_LABEL, CKA_CLASS])
#     print(attr)

# # print(result)

print("*********")