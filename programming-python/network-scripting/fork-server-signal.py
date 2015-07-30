import os, time, sys, time, signal
from socket import *
host = ""
port = 50007

# create socket object and listen, setting signal handler
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((host, port))
sockobj.listen(5)
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

def now():
	return time.ctime(time.time())

# client handled in child process
def handle_client(connection):
	time.sleep(5)
	while True:
		data = connection.recv(1024)
		if not data: break
		reply = "Echo=>%s at %s" % (data, now())
		connection.send(reply.encode())
	connection.close()
	os._exit(0)

def dispatcher():
	while True:
		connection, address = sockobj.accept()
		print("Server connected by", address, end=" ")
		print("at", now())
		child_pid = os.fork()
		if child_pid == 0:
			handle_client(connection)

dispatcher()