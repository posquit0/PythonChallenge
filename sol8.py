#!/usr/bin/env python
# encoding: utf-8
import bz2

USER_ID = ''
USER_ID += 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02'
USER_ID += '\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
USER_PW = ''
USER_PW += 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$'
USER_PW += ' \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'


def main():
    user_id = bz2.decompress(USER_ID)
    user_pw = bz2.decompress(USER_PW)
    print user_id
    print user_pw

if __name__ == '__main__':
    main()
