#!/usr/bin/python3
"""
This module fetches https://alx-intranet.hbtn.io/status url
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)

    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
