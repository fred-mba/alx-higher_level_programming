#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays
the value of the variable X-Request-Id in the response header
"""
from urllib import response
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]

    respo = requests.get(url)
    feed = respo.headers.get('X-Request-Id')
    print(feed)
