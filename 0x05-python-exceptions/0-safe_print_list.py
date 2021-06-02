#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list is None or my_list == [] or x == 0:
        print()
        return (0)
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
        print()
    except:
        print()
        return (i)

    return (i + 1)
