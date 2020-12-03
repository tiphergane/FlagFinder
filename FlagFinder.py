#!/usr/bin/env python3
# coding: utf-8
from pwn import *
import sys
import re


prog = sys.argv[0]


def Exploit():
    regex = sys.argv[2]
    file = sys.argv[1]
    info("Opening file: %s\n" % file)
    s = read(file)
    info("Searching for pattern: %s\n" % regex)
    c = re.findall(regex, str(s))
    if not str(c):
        info("Too Bad my friend !!!")
    else:
        for a in c:
            success("Yeah !!!! flag found: %s\n" % a)
            warn("flag is now copied in flag.txt")
            write("flag.txt", a)


def failExploit():
    error("An error occured")


if len(sys.argv) != 3:
    warn('Usage: python %s file "pattern"' % prog)
    sys.exit()

try:
    Exploit()
except:
    failExploit()
finally:
    info("Goodbye Professor !")
    sys.exit()
