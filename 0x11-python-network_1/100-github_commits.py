#!/usr/bin/python3
"""script that takes your Github credentials (username and password)
and uses the Github API to display your id"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) < 3:
        url = "https://api.github.com/repos/"+argv[2]+"/"+argv[1]+"/commits"
        r = requests.get(url)
        commits = r.json()
        for i in range(10):
            sha = commits[i]["sha"]
            name = commits[i]["commit"]["author"]["name"]
            print("{}: {}".format(sha, name))
