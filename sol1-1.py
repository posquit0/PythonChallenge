#!/usr/bin/env python
# encoding: utf-8
from string import lowercase

CIPHER = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def caesar_decrypt(cipher, n):
    return "".join(
        ch.isalpha() and lowercase[(lowercase.index(ch) - n) % len(lowercase)] or ch 
        for ch in cipher
    )

def main():
    print caesar_decrypt(CIPHER, 24)

if __name__ == '__main__':
    main()