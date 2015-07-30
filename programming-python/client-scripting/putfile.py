#!/usr/local/bin/python
"""
Store an arbitrary file by ftp in binary mode. Uses anonymous
ftp unless you in a user=(name, pswd) tuple of arguments.
"""

import ftplib

def putfile(file, site, dir, user=(), *, verbose=True):
	"""
	store a file by ftp to a site/directory
	"""
	if verbose: print("Uploading ", file)
	local = open(file, "rb")
	remote = ftplib.FTP(site)
	remote.login(user)
	remote.cwd(dir)
	remote.storbinary('STOR ' + file, local, 1024)
	remote.quit()
	local.close()
	if verbose: print("Upload done.")

if __name__ == "__main__":
	site = "ftp.rmi.net"
	dir = "."
	import sys, getpass
	pswd = getpass.getpass(site + "pswd?")	#filename on command line
	putfile(sys.argv[1], site, dir, user=("lutz", pswd))
