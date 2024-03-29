#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request
to the URL and displays the value of the variable
X-Request-Id in the response header
"""
import requests
import sys


if __name__ == "__main__":
    try:
        result = requests.get(sys.argv[1])
        print(result.headers['X-Request-Id'])
    except:
        print('None')
