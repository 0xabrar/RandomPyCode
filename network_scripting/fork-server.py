import os, time, sys
from socket import *
host = ''
port = 50007

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((host, port))
sockobj.listen(5)

def now():
	return time.ctime(time.time())

active_children = []
def reap_children():
	while active_children:
		pid, stat = os.waitpid(0, os.WNOHANG)
		if not pid: break
		active_children.remove(pid)

def handle_client(connection):
	time.sleep(5)
	while True:
		data = connection.recv(1024)
		if not data: break
		reply = "Echo=>%s at %s" %(data, now())
		connection.send(reply.encode())
	connection.close()	
	os._exit(0)

def dispatcher(): 
	while True:
		connection, address = sockobj.accept()
		print("Server connected by", address)
		print("at", now())
		reap_children()
		child_pid = os.fork()
		if child_pid == 0:
			handle_client(connection)
		else: 
			active_children.append(child_pid)

dispatcher()