"""
#################################################
used to test the socket_stream_redirect.py modes
#################################################
"""

import sys
import os
import multiprocessing
from socket_stream_redirect import *

#################################################
# redirected client output
#################################################


def server1():
    pid = os.getpid()
    conn = init_listener_socket()  # block until client connects
    sock_file = conn.makefile("r")
    for x in range(3):
        data = sock_file.readline().rstrip()  # block until data ready
        print("server %s got [%s]" % (pid, data))


def client1():
    pid = os.getpid()
    redirect_out()
    for x in range(3):
        print("client %s: %s" % (pid, x))
        sys.stdout.flush()


#################################################
# redirected client input
#################################################

def server2():
	