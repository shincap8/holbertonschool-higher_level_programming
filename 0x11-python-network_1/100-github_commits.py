#!/usr/bin/python3
"""script that takes your Github credentials (username and password)
and uses the Github API to display your id"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) < 3:
        exit()
    url = "https://api.github.com/repos/"+argv[2]+"/"+argv[1]+"/commits"
    commits = requests.get(url).json()
    for commit in commits[:10]:
        sha = commit["sha"]
        name = commit["commit"]["author"]["name"]
        print("{}: {}".format(sha, name))
