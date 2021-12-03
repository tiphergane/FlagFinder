#!/usr/bin/env python3
# coding: utf-8

import pwn
import argparse
import re
import requests


def Exploit(fichier, pattern):
    regex = pattern
    file = fichier
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


def Online(url, pattern):
    regex = pattern
    file = url
    pwn.info("Opening file: {fichier}\n".format(fichier=file))
    r = requests.session()
    s = r.get(file)
    s = s.content
    pwn.info("Search for pattern: {flag}\n".format(flag=regex))
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Rechercher un flag dans un fichier", prog="FlagFinder.py"
    )
    parser.add_argument(
        "-f",
        "--file",
        dest="fichier",
        help="Fichier à vérifier",
        # required=True,
    )
    parser.add_argument(
        "-u",
        "--url",
        dest="fichier",
        help="Lien vers le fichier",
    )
    parser.add_argument(
        "-o",
        "--online",
        help="Déclare si nous passons en mode en ligne",
        dest="isOnline",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "-r",
        "--regex",
        dest="pattern",
        help="Pattern à chercher, par défaut FLAG{.*?}",
        default="FLAG{.*?}",
    )
    args = parser.parse_args()
    fichier = args.fichier
    pattern = args.pattern
    if args.isOnline:
        Online(fichier, pattern)

    else:
        Exploit(fichier, pattern)
