#!/usr/bin/python3
"""that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header
You must use the packages requests and sys"""
import requests
import sys


email = {'email': sys.argv[2]}
r = requests.post(sys.argv[1], data=email)
print(r.text)
