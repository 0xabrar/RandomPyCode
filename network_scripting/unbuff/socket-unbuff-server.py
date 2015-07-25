# read 3 messages over a raw socket
import time
from socket import *

sockobj = socket()
sockobj.bind(("", 60000))
sockobj.listen(5)

print("accepting...")
conn, id = sockobj.accept()

for x in range(3):
	print("receiving...")
	msg = conn.recv(1024)	# blocks until data received
	print(msg)	# gets all print lines at once unless flushed


