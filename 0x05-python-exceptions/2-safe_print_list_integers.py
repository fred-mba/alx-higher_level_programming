#!/usr/bin/python3
def safe_print_list_integers(my_list=[], y=0):
    n = 0
    for i in range(y):
        try:
            print('{:d}'.format(my_list[i]), end="")
            n += 1
        except (ValueError, TypeError):
            i += 1
            continue
    print("")
    return (n)
