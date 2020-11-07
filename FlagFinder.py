#!/usr/bin/env python3
# coding: utf-8
from pwn import *
import sys
import re

regex = sys.argv[2]
file = sys.argv[1]


def Exploit():
    info("Opening file: %s\n" % file)
    f = read(file)
    info("Searching for pattern: %s\n" % regex)
    c = re.findall(regex, str(f))
    if not str(c):
        info("Too Bad my friend !!!")
    else:
        for a in c:
            success("Yeah !!!! flag found: %s\n" % a)
            success("flag is now copied in flag.txt")
            f = open("flag.txt", "w")
            f.write(a)
            f.close()


def failExploit():
    warn("Failed to open file %s" % file)


try:
    Exploit()
except:
    failExploit()
finally:
    info("Goodbye Professor !")
    sys.exit()
