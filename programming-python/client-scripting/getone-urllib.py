#!/usr/local/bin/python
"""
A Python script to download a file by FTP by its URL strings; use
higher level urllib instead of ftplib to fetch file. 
"""

import os, getpass
from urllib.request import urlopen

filename = "monkeys.jpg"
password = getpass.getpass("Pswd?")

remoteaddr = 'ftp://lutz:%s@ftp.rmi.net/%s;type=i' % (password, filename)

remotefile = urlopen(remoteaddr)
localfile = open(filename, "wb")
localfile.write(remotefile.read())

localfile.close()
remotefile.close()


