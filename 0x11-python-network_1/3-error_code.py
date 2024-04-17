#!/usr/bin/python3
"""
This module takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8)
"""

from urllib import request, error
from sys import argv


if __name__ == "__main__":
    url = request.Request(argv[1])

    try:
        with request.urlopen(url) as response:
            body = response.read().decode('utf-8')  # Decode the response
            print(body)

    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
