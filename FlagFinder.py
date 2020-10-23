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
    if str(c):
        info("Yeah !!!! flag founded: %s\n" % c)
    else:
        warn("Too bad my friend")

def ArgMissing():
    warn("Missing arguments, please use %s target \"Flag pattern\"" % sys.argv[0])

try:
    Exploit()
except:
    ArgMissing()
finally:
    sys.exit()
