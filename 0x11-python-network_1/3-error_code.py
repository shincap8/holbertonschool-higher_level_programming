#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)."""
from urllib import request, parse, error
from urllib.error import HTTPError
import sys


if __name__ == "__main__":
    req = request.Request(sys.argv[1])
    try:
        with request.urlopen(req) as res:
            body = res.read()
        print(body.decode("utf-8"))
    except HTTPError as er:
        print("Error code: {}".format(er.code))
