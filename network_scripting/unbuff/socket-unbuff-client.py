import time
from socket import *

sockobj = socket()
sockobj.connect(("localhost", 60000))
file = sockobj.makefile("w",  buffering=1)

print("sending data1")
file.write("spam\n")
time.sleep(5)
#file.flush()

print("sending data2")
print("eggs", file=file)
time.sleep(5)
file.flush()

print("sending data3")
sockobj.send(b"ham\n")
time.sleep(5)