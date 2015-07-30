#!/usr/local/bin/python
"""
Fetch and play the Monty Python theme song. 
Requires Internet access and an FTP account. Uses audio filters
on Unix and the .au player on Windows.
- Configure getfile.py as needed for platform.
"""

from getpass import getpass
from PP4E.Internet.Ftp.getfile import getfile
from PP4E.System.Media.playfile import playfile

file = "sousa.au"
site = "ftp.rmi.net"
dir = "."
user = ("lutz", getpass("Pswd?"))

getfile(file, site, dir, user)
playfile(file)

# import os
# os.system("getone.py sousa.au")



