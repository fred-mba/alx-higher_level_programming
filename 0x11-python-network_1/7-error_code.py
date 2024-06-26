#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the body of the
response.
If the HTTP status code is greater than or equal to 400, print:
Error code: followed by the value of the HTTP status code
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = requests.get(argv[1])
    if url.status_code >= 400:
        print("Error code: {}".format(url.status_code))
    else:
        print(url.text)
