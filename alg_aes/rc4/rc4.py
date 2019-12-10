# -*-coding:utf-8-*-
# import base64
import binascii

def rc4_crypt(PlainBytes: bytes, KeyBytes: bytes) -> str:
    '''[summary]
    rc4 crypt
    Arguments:
        PlainBytes {[bytes]} -- [plain bytes]
        KeyBytes {[bytes]} -- [key bytes]

    Returns:
        [string] -- [hex string]
    '''

    keystreamList = []
    cipherList = []

    keyLen = len(KeyBytes)
    plainLen = len(PlainBytes)
    S = list(range(256))

    j = 0
    for i in range(256):
        j = (j + S[i] + KeyBytes[i % keyLen]) % 256
        S[i], S[j] = S[j], S[i]

    i = 0
    j = 0
    for m in range(plainLen):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        cipherList.append(k ^ PlainBytes[m])

    result_hexstr = ''.join(['%02x' % i for i in cipherList])
    return result_hexstr.upper()

def encrypt(mode,data,key):
    data = binascii.a2b_hex(data)
    key = binascii.a2b_hex(key.upper())
    res = rc4_crypt(PlainBytes=data, KeyBytes=key)
    return res

def decrypt(mode,data,key):
    data = binascii.a2b_hex(data)
    key = binascii.a2b_hex(key.upper())
    res = rc4_crypt(PlainBytes=data, KeyBytes=key)
    return res

from tools import test_alg

def role(sign, alg, mode,):
    ans = test_alg.alg_all_test(sign, alg, mode, encrypt, decrypt)
    return ans


if __name__ == "__main__":
    pass

