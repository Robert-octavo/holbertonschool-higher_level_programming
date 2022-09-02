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
    auth = requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2])
    result = requests.get("https://api.github.com/user", auth=auth)
    code, yourId = result.status_code, result.json().get("id")
    print('None') if code >= 400 else print(yourId)
