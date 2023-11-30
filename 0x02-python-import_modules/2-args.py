#!/usr/bin/python3
import sys


def print_arguments():
    arg_num = len(sys.argv) - 1

    if arg_num == 0:
        print("{} arguments.".format(arg_num))
    elif arg_num == 1:
        print("{} argument:".format(arg_num))
    else:
        print("{} arguments:".format(arg_num))

    if arg_num > 0:
        for i in range(1, len(sys.argv)):
            print(f"{i}: {sys.argv[i]}")


if __name__ == "__main__":
    print_arguments()
