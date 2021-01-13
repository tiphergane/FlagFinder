#!/usr/bin/env python3
# coding: utf-8
import pwn
import sys
import re


prog = sys.argv[0]


def Exploit():
    regex = sys.argv[2]
    file = sys.argv[1]
    pwn.info("Opening file: %s\n" % file)
    s = pwn.read(file)
    pwn.info("Searching for pattern: %s\n" % regex)
    c = re.findall(regex, str(s))
    if not str(c):
        pwn.info("Too Bad my friend !!!")
    else:
        for a in c:
            pwn.success("Yeah !!!! flag found: %s\n" % a)
            pwn.warn("flag is now copied in flag.txt")
            pwn.write("flag.txt", a)


def failExploit():
    pwn.error("An error occured")


if len(sys.argv) != 3:
    pwn.warn('Usage: python %s file "pattern"' % prog)
    sys.exit()

try:
    Exploit()
except IOError:
    pwn.error("Impossible d'ouvrir le fichier %s", sys.argv[1])
except:
    failExploit()
finally:
    pwn.info("Goodbye Professor !")
    sys.exit()
