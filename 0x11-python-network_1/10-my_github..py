#!/usr/bin/python3
"""
Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to
display your id
"""
import requests
import requests.auth
import sys


if __name__ == "__main__":
    try:
        auth = requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2])
        result = requests.get("https://api.github.com/user", auth=auth)
        yourId = result.json().get("id")
        print(yourId)
    except:
        print("None")