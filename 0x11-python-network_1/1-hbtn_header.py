#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response."""
from urllib import request
import sys


with request.urlopen(sys.argv[1]) as res:
    headers = res.info()
    print(headers['X-Request-Id'])
