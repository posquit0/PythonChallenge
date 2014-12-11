#!/usr/bin/env python
# encoding: utf-8
from string import (
    lowercase, maketrans
)

CIPHER = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def caesar_decrypt(cipher, n):
    intab = lowercase
    outtab = intab[len(intab) - n:] + intab[:len(intab) - n]
    trans = maketrans(intab, outtab)
    return cipher.translate(trans)

def main():
    print caesar_decrypt(CIPHER, 24)

if __name__ == '__main__':
    main()