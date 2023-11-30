#!/usr/bin/python3
import sys


def main():
    add_num = len(sys.argv)

    if add_num > 0:
        total = 0
        for i in range(1, add_num):
            total += int(sys.argv[i])

        print(total)


if __name__ == "__main__":
    main()
