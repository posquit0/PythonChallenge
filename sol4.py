#!/usr/bin/env python
# encoding: utf-8
import requests
import re

PROBLEM_URL = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
DIVIDE_STAGE = r"Divide by"
NEXT_REGEX = r"nothing is (\d+)"
START = 12345

def main():
    next = START
    payload = dict()

    while True:
        payload['nothing'] = next
        r = requests.get(PROBLEM_URL, params=payload)
        data = re.findall(NEXT_REGEX, r.text)
        if data:
            next = data[0]
        else:
            if DIVIDE_STAGE in r.text:
                next = int(next) / 2
            else:
                print r.text
                break

if __name__ == '__main__':
    main()