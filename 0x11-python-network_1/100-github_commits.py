#!/usr/bin/python3
"""list 10 commits of the repository rails by the user rails"""
import requests
import sys


if __name__ == "__main__":
    user = sys.argv[2]
    repo = sys.argv[1]
    url = "http://api.github.com/repos/{}/{}/commits".format(user, repo)

    resp = requests.get(url, params={'per_page': 10})
    json = resp.json()
    for commit in json:
        print("{}: {}".format(commit.get("sha"),
                              commit.get("commit").get("author").get("name")))
