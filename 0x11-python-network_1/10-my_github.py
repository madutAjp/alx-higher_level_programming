#!/usr/bin/python3
"""A  script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id
"""
import requests
from sys import argv

if __name__ == '__main__':
    username = argv[1]
    token = argv[2]
    url = "https://api.github.com/user"
    headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json",
            }
    response = requests.get(url, header=headers)
    if response.status_code == 200:
        print(response.json()["id"])
    else:
        print(None)
