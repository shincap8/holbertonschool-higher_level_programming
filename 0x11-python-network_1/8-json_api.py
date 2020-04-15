#!/usr/bin/python3
"""Python script that takes in a URL, sends a request
to the URL and displays the body of the response.
If the HTTP status code is greater than or equal to 400,
print: Error code: followed by the value of the HTTP status code"""
import requests
import sys


if __name__ == "__main__":
    letter = {'q': ""}
    if len(sys.argv) > 1:
        letter['q'] = sys.argv[1]
    r = requests.post("http://0.0.0.0:5000/search_user", data=letter)
    try:
        dict = r.json()
        if len(dict) != 0:
            print("[{}] {}".format(dict["id"], dict["name"]))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
