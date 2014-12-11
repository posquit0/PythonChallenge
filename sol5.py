#!/usr/bin/env python
# encoding: utf-8
import urllib
import pickle

DATA_URL = "http://www.pythonchallenge.com/pc/def/banner.p"

def main():
    u = urllib.urlopen(DATA_URL)
    p = pickle.load(u)
    for data in p:
        print "".join(chr * cnt for (chr, cnt) in data)

if __name__ == '__main__':
    main()