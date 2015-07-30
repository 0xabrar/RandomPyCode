import os, time, sys
from socket import *
from multiprocessing import Process
host = ''
port = 50007



def now():
	return time.ctime(time.time())

def handle_client(connection):
	print("child: ", os.getpid())
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
		print("Server connected by", address, end=" ")
		print("at", now())
		Process(target=handle_client, args=(connection,)).start()

if __name__ == "__main__":
	print("Parent: ", os.getpid())
	sockobj = socket(AF_INET, SOCK_STREAM)
	sockobj.bind((host, port))
	sockobj.listen(5)
	dispatcher()