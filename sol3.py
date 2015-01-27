#!/usr/bin/env python
# encoding: utf-8
import requests
import re

PROBLEM_URL = "http://www.pythonchallenge.com/pc/def/equality.html"
COMMENT_REGEX = re.compile(r"<!--(.*?)-->", re.DOTALL)
BODYGUARD_REGEX = r"[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]"


def recognize(data):
    return "".join(re.findall(BODYGUARD_REGEX, data))


def main():
    r = requests.get(PROBLEM_URL)
    data = r.text
    comment = COMMENT_REGEX.findall(data)[0]
    comment = "".join(line for line in comment.split())
    print recognize(comment)

if __name__ == '__main__':
    main()
