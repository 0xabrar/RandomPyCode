#!/usr/loca/bin/python
"""
################################################################
Download and play a media file by FTP, using ftplib.
Change filename and sitename accordingly. 
################################################################
"""

import os, sys
from getpass import getpass
from ftplib import FTP

nonpassive = False	# force active mode FTP for server?
filename = "monkeys.jpg"
dirname = "."
sitename = "ftp.rmi.net"
userinfo = ('lutz', getpass("Pswd?"))
if len(sys.argv) > 1: filename = sys.argv[1]

print("Connecting...")
connection = FTP(sitename)
connection.login(userinfo)
connection.cwd(dirname)
if nonpassive:
	connection.set_psv(False)

print("Downloading...")
localfile = open(filename, "wb")
connection.retrbinary("RETR" + filename, localfile.write, 1024)
connection.quit()
localfile.close()

if input("Open file?") in ["Y", "y"]:
	from PP4E.System.Media.playfile import playfile
	playfile(filename)