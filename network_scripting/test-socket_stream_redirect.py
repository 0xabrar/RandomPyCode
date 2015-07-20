"""
#################################################
used to test the socket_stream_redirect.py modes
#################################################
"""

import sys
import os
import multiprocessing
from socket_stream_redirect import *

###########################################################
# redirected client output
###########################################################


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
        print("client %s: %s" % (pid, x))  # print to socket
        sys.stdout.flush()


###########################################################
# redirected client input
###########################################################

def server2():
    pid = os.getpid()
    conn = init_listener_socket()
    for x in range(3):
        conn.send(("server %s: %s\n" % (pid, x)).encode())


def client2():
    pid = os.getpid()
    redirect_in()
    for x in range(3):
        data = input()  # input from socket
        print("client %s got [%s]" % s(pid, data))

###########################################################
# redirect client input + output, client is socket client
###########################################################


def server3():
    pid = os.getpid()
    conn = init_listener_socket()
    sock_file = conn.makefile("r")  # recv print, send input()
    for x in range(3):
        data = sock_file.readline().rstrip()
        conn.send(("server %s got [%s]" % (pid, data)).encode())


def client3():
    pid = os.getpid()
    redirect_both_as_client()
    for x in range(3):
        print("client %s: %s" % (pid, x))
        data = input()  # input from socket , flushes
        # not redirected
        sys.stderr.write("client %s got [%s]\n" % (pid, data))


###########################################################
# redirect client input + output, client is socket server
###########################################################

def server4():
    pid = os.getpid()
    sockobj = socket(AF_INET, SOCK_STREAM)
    sockobj.connect((host, port))
    sock_file = sockobj.makefile("r")
    for x in range(3):
        sockobj.send(("server %s: %s\n" % (pid, x)).encode())
        data = sock_file.readline().rstrip()
        print("server %s got [%s]" % (pid, data))


def client4():
    pid = os.getpid()
    redirect_both_as_server()
    for x in range(3):
        data = input()  # input from socket, flushes
        # print to socket
        print("client %s got [%s]" % (pid, data))
        sys.stdout.flush()

###########################################################
# redirect client input + output, client as socket server, 
# server transfers first
###########################################################
    
def server5():
    pid = os.getpid()
    conn = init_listener_socket()   
    sock_file = conn.makefile("r")  # send input, recv print
    for x in range(3):
        conn.send(("server %s: %s\n" % (pid, x)).encode())
        data = sock_file.readline().rstrip()
        print("server %s for [%s]" % (pid, data))

def client5():
    pid = os.getpid()
    s = redirect_both_as_client() # socket client in mode
    for x in range(3):
        data = input()
        # print to socket
        print("client %s got [%s]" % (pid, data))
        sys.stdout.flush()


###########################################################
# test by number on command line
###########################################################

if __name__ == "__main__":
    server = eval("server" + sys.argv[1])
    client = eval("client" + sys.argv[1])
    multiprocessing.Process(target=server).start()
    client()



