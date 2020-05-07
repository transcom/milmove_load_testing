#!/usr/bin/env python

#   Copyright (C) 2015 Roman Pasechnik
#
# This file is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA.

from PyKCS11 import *
import os
import sys

pin = os.getenv('PIN')
print (pin)

# the key_id has to be the same for both objects
key_id = (0x22,)

pkcs11 = PyKCS11Lib()
# pkcs11.load()  # define environment variable PYKCS11LIB=YourPKCS11Lib
lib_path = "/usr/local/lib/pkcs11/opensc-pkcs11.so"
pkcs11.load(lib_path)

# get 1st slot
slot = pkcs11.getSlotList(tokenPresent=True)[0]

session = pkcs11.openSession(slot, CKF_SERIAL_SESSION | CKF_RW_SESSION)
session.login(pin)

pubTemplate = [
    (CKA_CLASS, CKO_PUBLIC_KEY),
    (CKA_TOKEN, CK_TRUE),
    (CKA_PRIVATE, CK_FALSE),
    (CKA_MODULUS_BITS, 0x0400),
    (CKA_PUBLIC_EXPONENT, (0x01, 0x00, 0x01)),
    (CKA_ENCRYPT, CK_TRUE),
    (CKA_VERIFY, CK_TRUE),
    (CKA_VERIFY_RECOVER, CK_TRUE),
    (CKA_WRAP, CK_TRUE),
    (CKA_LABEL, "My Public Key"),
    (CKA_ID, key_id),
]

privTemplate = [
    (CKA_CLASS, CKO_PRIVATE_KEY),
    (CKA_TOKEN, CK_TRUE),
    (CKA_PRIVATE, CK_TRUE),
    (CKA_DECRYPT, CK_TRUE),
    (CKA_SIGN, CK_TRUE),
    (CKA_SIGN_RECOVER, CK_TRUE),
    (CKA_UNWRAP, CK_TRUE),
    (CKA_ID, key_id),
]

(pubKey, privKey) = session.generateKeyPair(pubTemplate, privTemplate)

# logout
session.logout()
session.closeSession()