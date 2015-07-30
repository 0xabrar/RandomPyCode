"""
######################################################################
implement client and server-side logic to transfer an arbitrary file
from server to client over a socket; use a simple control-info 
protocol rather than separate sockets for control and data (as in 
ftp), dispatches each client request to a handler thread, and loops
to transfer the entire file by blocks
######################################################################
"""

# TODO: use context manangers for all resource management

import sys, os, time, _thread  as thread
from socket import *

blitz = 1024
default_host = "localhost"
default_port = 50002

help_text = """
Usage...
server=> getfile.py -mode server 		[-port nnn] [-host hhh|localhost]
client=> getfile.py [-mode client] -file fff [-port nnn] [-host hhh|localhost]
"""

def now():
	return time.asctime()
{
	"cmd": ["python", "-u", "$file" ],
	"file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
	"selector": "source.python"
}

def parse_command_line():
	dict = {}	# in dictionary for easy lookup 
	args = sys.argv[1:]	
	# example: dict['-mode'] = 'server'
	while len(args) >= 2:
		dict[args[0]] = args[1]
		args = args[2:]
	return dict

def client(host, port, filename):
	sockobj = socket(AF_INET, SOCK_STREAM)
	sockobj.connect((host, port))
	sockobj.send((filename + "\n").encode())	# send remote name with dir: bytes

	dropdir = os.path.split(filename)[1]	# filename at end of dir path
	file = open(dropdir, "wb")	# create local file in cwd
	while True:
		data = sockobj.recv(blitz)
		if not data: break
		file.write(data)
	sockobj.close()
	file.close()
	print("Client got ", filename, "at", now())

def server_thread(client_sock):
	sockfile = client_sock.makefile("r")	# wrap sock in duplicate file obj
	filename = sockfile.readline()[:-1] # get filename up to end-line
	try:
		file = open(filename, "rb")
		while True:
			bytes = file.read(blitz)
			if not bytes: break
			sent = client_sock.send(bytes)
			assert send == len(bytes)
	except: 
		print("Error downloading file on server: ", filename)
	client_sock.close()	

def server(host, port):
	server_sock = socket(AF_INET, SOCK_STREAM)
	server_sock.bind((host, port))	# serve clients in threads
	server_sock.listen(5)
	while True:
		client_sock, client_addr = server_sock.accept()
		print("Server connected by", client_addr, "at", now())
		thread.start_new_thread(server_thread, (client_sock,))

def main(args):
	host = args.get('-host', default_host)
	port = int(args.get('-port', default_port))
	if args.get('-mode') == 'server':	
		if host == "locahost": host = "" # client is no mode flag
		server(host, port)	# else fails remotely
	elif args.get("-file"):
		client(host, port, args["-file"])
	else:
		print(help_text)

if __name__ == "__main__":
	args = parse_command_line()
	main(args)