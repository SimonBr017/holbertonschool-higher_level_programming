#!/usr/bin/python3
"""takes in a URL and an email,
sends a POST request to the passed
URL with the email as a parameter,
and displays the body of the response"""

import urllib.request
import sys
import urllib.parse


if __name__ == '__main__':
    data = urllib.parse.urlencode({"email": sys.argv[2]})
    data = data.encode('ascii')
    url = sys.argv[1]

    with urllib.request.urlopen(url, data) as response:
        html = response.read()
        print(html.decode('utf-8'))
