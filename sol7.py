#!/usr/bin/env python
# encoding: utf-8
from PIL import Image
import StringIO
import requests
import re

IMG_URL = "http://www.pythonchallenge.com/pc/def/oxygen.png"
MSG_LINE = 50
MESSAGE_REGEX = r"(\d+)"


def main():
    data = requests.get(IMG_URL).content
    data = StringIO.StringIO(data)
    img = Image.open(data)
    w, h = img.size

    filtered = [img.getpixel((x, MSG_LINE)) for x in range(0, w, 7)]
    message = "".join(chr(r) for (r, g, b, _) in filtered if r == g == b)
    print message
    message = "".join(
        chr(ch) for ch in map(int, re.findall(MESSAGE_REGEX, message))
    )
    print message

if __name__ == '__main__':
    main()
