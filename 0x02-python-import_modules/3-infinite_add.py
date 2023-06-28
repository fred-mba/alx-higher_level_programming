#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    numb_args = len(argv)
    sum_total = 0
    for i in range(1, numb_args):
        sum_total += int(argv[i])
    print("{:d}".format(sum_total))
