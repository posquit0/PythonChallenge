#!/usr/bin/env python
# encoding: utf-8
import requests
import re

PROBLEM_URL = "http://www.pythonchallenge.com/pc/def/ocr.html"
COMMENT_REGEX = re.compile(r"<!--(.*?)-->", re.DOTALL)
ALPHABET_REGEX = r"[a-zA-Z]"

def recognize(data):
    return "".join(re.findall(ALPHABET_REGEX, data))

def main():
    r = requests.get(PROBLEM_URL)
    data = r.text
    comment = COMMENT_REGEX.findall(data)
    print recognize(comment[1])


if __name__ == '__main__':
    main()