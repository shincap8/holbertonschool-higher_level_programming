#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status
You must use the package requests"""
import requests


if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    print("Body response:\n\t- type: {}\n\t- content: {}".
          format(type(r.text), r.text))
