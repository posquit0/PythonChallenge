#!/usr/bin/env python
# encoding: utf-8
import StringIO
import requests
import zipfile
import re

ZIP_URL = "http://www.pythonchallenge.com/pc/def/channel.zip"
NEXT_REGEX = r"nothing is (\d+)"
BASE_FILENAME = "%s.txt"
START = 90052


def main():
    data = requests.get(ZIP_URL).content
    data = StringIO.StringIO(data)
    file = zipfile.ZipFile(data)
    next = START
    message = str()

    while True:
        filename = BASE_FILENAME % next
        message += file.getinfo(filename).comment
        data = file.read(filename)
        found = re.findall(NEXT_REGEX, data)
        if found:
            next = found[0]
        else:
            print data
            print message
            break

if __name__ == '__main__':
    main()
