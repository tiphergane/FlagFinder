#!/usr/bin/env python3
# coding: utf-8
import pwn
import sys
import re


prog = sys.argv[0]


def Exploit():
    regex = sys.argv[2]
    file = sys.argv[1]
    pwn.info("Opening file: {fichier}\n".format(fichier=file))
    s = pwn.read(file)
    pwn.info("Searching for pattern: {flag}\n".format(flag=regex))
    c = re.findall(regex, str(s))
    if not c:
        pwn.warn("No flag for you my friend, check your regex")
    else:
        for a in c:
            pwn.success("Yeah !!!! flag found: {result}\n".format(result=a))
            pwn.warn("flag is now copied in flag.txt")
            pwn.write("flag.txt", a)


def failExploit():
    pwn.error("An error occured")


if len(sys.argv) != 3:
    pwn.warn(
        "Usage: {program} {file} {regex}".format(
            program=sys.argv[0], file="cible", regex="flag{.*?}"
        )
    )
    sys.exit()

try:
    Exploit()
except IOError:
    pwn.error("Impossible d'ouvrir le fichier {file}".format(file=sys.argv[1]))
except KeyboardInterrupt:
    pwn.info("Canceled by user (CTRL-C)")
except:
    failExploit()
finally:
    pwn.info("Goodbye Professor !")
    sys.exit()
