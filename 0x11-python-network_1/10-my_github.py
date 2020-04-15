#!/usr/bin/python3
"""script that takes your Github credentials (username and password)
and uses the Github API to display your id"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/user"
    headers = {"X-Github-Username": argv[1],
            "Authorization": "token " + argv[2]}
    try:
        r = requests.get(url, headers=headers)
        print(r.json()["id"])
    except:
        print(None)
