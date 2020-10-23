#!/usr/bin/env python3
#coding: utf-8
from pwn import *
import re

regex = sys.argv[2]
file = sys.argv[1]

def Exploit():
    info("Opening file: %s\n" % file)
    f = read(file)
    c = re.findall(regex,str(f))
    if not str(c):
        info("Too Bad my friend !!!")
    else:
        for a in c:
            info("Yeah !!!! flag founded: %s\n" % c)

def failExploit():
    warn("Failled to open file %s" % file)

try:
    Exploit()
except:
    failExploit()
finally:
    sys.exit()
