#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) == 2 and sys.argv[1].isalpha() else ""
    res = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        file = res.json()
        cod , name = file.get("id") , file.get("name")
        print("[{}] {}".format(cod, name)) if file else print("No result")
    except:
        print('Not a valid JSON')
