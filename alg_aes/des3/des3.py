#!/usr/bin/env python
# coding:utf-8

import binascii
import base64
import pyDes
import time
from getrandom import *


# Key has to be 24bit long
key = T_key
# here is the data you want to encrypt
data = get_random_16bytes()

def encrypt(key, data,mode):
    iv = "0000000000000000"
    iv = binascii.unhexlify(iv)
    key = binascii.unhexlify(key)
    data = binascii.unhexlify(data)
    if mode == 'cbc':
        k = pyDes.triple_des(key, pyDes.CBC, iv, pad=None, padmode=pyDes.PAD_NORMAL)
    elif mode == 'ecb':
        k = pyDes.triple_des(key, pyDes.ECB, pad=None, padmode=pyDes.PAD_NORMAL)
    else:
        raise Exception("wrong mode")
    d = k.encrypt(data)
    return binascii.hexlify(d)

def hex_to_str(s):
    return ''.join([chr(i) for i in [int(b, 16) for b in s.split(' ')]])

def decrypt(key, data,mode):
    data = binascii.unhexlify(data)
    iv = "0000000000000000"
    iv = binascii.unhexlify(iv)
    key = binascii.unhexlify(key)
    if mode == 'cbc':
        k = pyDes.triple_des(key, pyDes.CBC, iv, pad=None, padmode=pyDes.PAD_NORMAL)
    elif mode == 'ecb':
        k = pyDes.triple_des(key, pyDes.ECB, iv, pad=None, padmode=pyDes.PAD_NORMAL)
    else:
        raise Exception("wrong mode")
    d = k.decrypt(data)
    return binascii.hexlify(d)

from tools import test_alg

def role(sign, alg, mode,):
    ans = test_alg.alg_all_test(sign, alg, mode, encrypt, decrypt)
    return ans

