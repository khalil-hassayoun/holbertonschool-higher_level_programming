#!/usr/bin/python3
def new_in_list(list, idx, element):
    if (idx >= len(list) or idx < 0):
        return (list)
    newlist = list[:]
    newlist[idx] = element
    return (newlist)
