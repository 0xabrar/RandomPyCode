#!/usr/local/bin/python
"""
A Python script to download and play a media file by FTP.
Uses getfile.py. 
"""
# change sys path when getfile not in directory
import getfile
from getpass import getpass

filename = "monkeys.jpg"
getfile.getfile(file=filename, 
		site="ftp.rmi.ent",
		dir=".",
		user=("lutz", getpass("Pswd?")),
		refetch=True)
 
if input("Open file?") in ["Y", "y"]:
	from PP4E.System.Media.playfile import playfile
	playfile(filename)

