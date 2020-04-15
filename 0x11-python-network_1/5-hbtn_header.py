#!/usr/bin/python3
"""that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header
You must use the packages requests and sys"""
import requests
import sys


r = requests.get(sys.argv[1])
print(r.headers["X-Request-Id"])
