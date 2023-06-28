#!/usr/bin/python3
import sys


def main():
    args = sys.argv[1:]
    length = len(args)

    if length == 0:
        print('{} arguments.'.format(length))
    elif length == 1:
        print('{} argument:'.format(length))
    else:
        print('{} arguments:'.format(length))

    for i, arg in enumerate(args):
        print('{}: {}'.format(i + 1, arg))


if __name__ == "__main__":
    main()
