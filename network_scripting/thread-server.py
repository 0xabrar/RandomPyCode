import time, _thread as thread
from socket import *
host = ""
port = 50007


def now():
	return time.ctime(time.time())

def handle_client(connection):
	time.sleep(5)
	while True:
		data = connection.recv(1024)
		if not data: break
		reply = "Echo=>%s at %s" % (data, now())
		connection.send(reply.encode())
	connection.close()

def dispatcher():
	while True:
		connection, address = sockobj.accept()
		print("Server connected by", address, end=" ")
		print("at", now())
		thread.start_new_thread(handle_client, (connection,))

if __name__ == "__main__":
	sockobj = socket(AF_INET, SOCK_STREAM)
	sockobj.bind((host, port))
	sockobj.listen(5)
	dispatcher()

