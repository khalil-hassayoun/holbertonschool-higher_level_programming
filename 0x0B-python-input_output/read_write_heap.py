#!/usr/bin/python3
"""
read_write_heap: reads from the heap of another running process
reports basics information about the memory space
and then finds and replaces a string inside of the heap
"""
import sys
import os


class Memmap:
    """ memmap: class to hold info about the memory space """
    def __init__(self, info):
        self.addresses = info[0]
        self.permissions = info[1]
        self.offset = info[2]
        self.inode = info[4]
        dash = self.addresses.find("-")
        self.start = self.addresses[:dash]
        self.end = self.addresses[dash + 1:]


def find_string(fd, info, string):
    """ finds a string inside of the memory file """
    with open("/proc/{:s}/mem".format(sys.argv[1]), 'rb') as f:
        f.seek(int(info.start, 16), 0)
        total = (int(info.end, 16) - int(info.start, 16))
        b = f.read(total)
        for x in range(total):
            if chr(b[x]) == string[0]:
                temp = b[x:x + len(string)]
                if temp.decode('UTF-8') == string:
                    return (x)
    return (-1)

if len(sys.argv) != 4:
    print("Usage: read_write_heap.py pid search_string replace_string")
    exit(1)

string = sys.argv[2]
replace = bytes(sys.argv[3] + '\x00', 'utf-8')
print(replace)

heap = "[heap]"
with open("/proc/{:s}/maps".format(sys.argv[1]), 'r') as f:
    print("[*] maps: /proc/{:s}/maps".format(sys.argv[1]))
    for line in f:
        if heap in line:
            info = Memmap(line.split())
            print("[*] Found {:s}:".format(heap))
            print("        pathname = {:s}".format(heap))
            print("        addresses: = {:s}".format(info.addresses))
            print("        permissions: = {:s}".format(info.permissions))
            print("        offset: = {:s}".format(info.offset))
            print("        inode = {:s}".format(info.inode))
            print("[*] Addr start [{:s}] | end [{:s}]"
                  .format(info.start, info.end))
    f.closed

found = find_string(sys.argv[1], info, string)

if found == -1:
    print("[*] {:s} not found!".format(string))
    exit()

print("[*] Found {:s} at {:d}".format(string, found))
with open("/proc/{:s}/mem".format(sys.argv[1]), 'wb') as f:
    f.seek(found + int(info.start, 16), 0)
    f.write(bytes(replace))
    print("[*] Replaced {:s} with {:s}".format(string, sys.argv[3]))
