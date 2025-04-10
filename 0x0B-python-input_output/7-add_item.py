#!/usr/bin/python3
"""Adds all arguments to a Python list, and then save them to a file"""
import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"


def main():
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        items = load_from_json_file(filename)
    else:
        items = []
    items.extend(sys.argv[1:])
    save_to_json_file(items, filename)


if __name__ == "__main__":
    main()
