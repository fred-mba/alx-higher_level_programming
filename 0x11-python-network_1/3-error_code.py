#!/usr/bin/python3
"""
This module takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8)
"""

from urllib import request
from urllib import error
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    try:
        with request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)

    except error.HTTPError as err:
        print(f"Error code: {err.code}")
