#!/usr/bin/python3
"""This script fetches https://alx-intranet.hbtn.io/status"""
from os import error
from urllib.error import URLError
import urllib.request

url = "https://alx-intranet.hbtn.io/status"

if __name__ == "__main__":
    with urllib.request.urlopen(url) as response:
        html = response.read()
    print("Body response:")
    print("\t- type:", type(html))
    print("\t- content:", html)
    print("\t- utf8 content:", html.decode('utf-8'))
