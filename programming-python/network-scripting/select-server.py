"""
Use the select module to manually multiplex among a set of sockets: 
	- main sockets which accept new client connections
	- input sockets connected to accepted clients
"""

import sys
import time
from select import select
from socket import socket, AF_INET, SOCK_STREAM


def now(): return time.ctime(time.time())


host = ""
port = 50007
if len(sys.argv) == 3:
    host, port = sys.argv[1:]
num_port_socks = 2

# main sockets for accepting new client requests
mainsocks, readsocks, writesocks = [], [], []
for x in range(num_port_socks):
    portsock = socket(AF_INET, SOCK_STREAM)  # make TCP/IP socket
    portsock.bind((host, port))
    portsock.listen(5)

    mainsocks.append(portsock)
    readsocks.append(portsock)
    port += 1


# event loop: listen and multiplex until server process killed
print(" select server loop starting")
while True:
    readables, writeables, exceptions, = select(readsocks, writesocks, [])
    for sockobj in readables:
        if sockobj in mainsocks:  # ready input sockets
            # port socket: accept new client
            newsock, address = sockobj.accept()
            print("Connect:", address, id(newsock))
            readsocks.append(newsock)
        else:
            # client socket: read next line
            data = sockobj.recv(1024)
            print('\tgot', data, 'on', id(sockobj))
            if not data:
                sockobj.close()
                readsocks.remove(sockobj)
            else:
                # this may block, select for writesocks
                reply = "Echo=>%s at %s" % (data, now())
                sockobj.send(reply.encode())
                	