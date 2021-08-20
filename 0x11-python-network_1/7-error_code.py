#!/usr/bin/python3
""" takes in a URL, sends a request
to the URL and displays the body of
the response (decoded in utf-8)."""

import requests
import sys


if __name__ == '__main__':

    resp = requests.get(sys.argv[1])
    if resp.status_code < 400:
        print(resp.text)
    else:
        print("Error code: {}".format(resp.status_code))
