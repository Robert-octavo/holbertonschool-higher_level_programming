#!/usr/bin/python3
"""
The Holberton School staff evaluates candidates applying for a
back-end position with multiple technical challenges, like this one:
repository_url:	"https://api.github.com/repos/{owner}/{repo}"
https://api.github.com/repos/rails/rails/
commits_url	"https://api.github.com/repos/rails/rails/commits{/sha}"
"""
import requests
import requests.auth
import sys


if __name__ == "__main__":
    repo, owner = sys.argv[1], sys.argv[2]
    result = requests.get("https://api.github.com/repos/{}/{}/commits".
                          format(owner, repo))
    # if result.status_code >= 400:
    #    print('None')
    try:
        commits = result.json()
        for i in range(0, 10):
            code = commits[i].get("sha")
            name = commits[i].get("commit").get("author").get("name")
            print("{}: {}".format(code, name))
    except:
        pass
