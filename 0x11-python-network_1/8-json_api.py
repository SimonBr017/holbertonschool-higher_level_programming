#!/usr/bin/python3
"""that takes in a letter
and sends a POST request to
http://0.0.0.0:5000/search_user
with the letter as a parameter."""

import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        parameter_value = sys.argv[1]
    else:
        parameter_value = ""

    url = "http://0.0.0.0:5000/search_user"
    resp = requests.post(url, data={'q': parameter_value})

    try:
        json = resp.json()
        if 'id' in json:
            print('[{}] {}'.format(json.get('id'), json.get('name')))
        else:
            print("No result")
    except Exception:
        print("Not a vald JSON")
