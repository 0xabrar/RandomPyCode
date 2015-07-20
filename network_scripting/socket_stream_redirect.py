"""
######################################################################
Tools for connecting standard streams of non-GUI programs to
sockets that a GUI program can use to interact with non-GUI programs.
######################################################################
"""

import sys
from socket import *
port = 50008 		# pass in different port if multiple dialogs on machine
host = "localhost"  # pass in different host to connect to remote listeners


def init_listener_socket(port=port):
    """
    init connected sockets for callers that listen in server mode 
    """
    sockobj = socket(AF_INET, SOCK_STREAM)
    sockobj.bind(("", port))
    sockobj.listen(5)

    conn, addr = sockobj.accept()
    return conn


def redirect_out(port=port, host=host):
    """
    connect caller's standard output stream to a socket for GUI to listen
    start caller after listener started, else connect fails before accept
    """
    sockobj = socket(AF_INET, SOCK_STREAM)
    sockobj.bind((host, port))
    sock_file = sockobj.makefile("w")  # make prints go to sock.send
    sys.stdout = sock_file
    return sockobj


def redirect_in(port=port, host=host):
    """
    connect caller's standard input stream to a socket for GUI to provide
    """
    sockobj = socket(AF_INET, SOCK_STREAM)
    sockobj.connect((host, port))
    sock_file = sockobj.makefile("r")
    sys.stdin = sock_file 	# make input come from sockobj.recv
    return sockobj


def redirect_both_as_client(port=port, host=host):
    """
    connect caller's standard input and output stream to same socket 
    in this mode, caller is client to a server: sends msgs, receives reply
    """
    sockobj = socket(AF_INET, SOCK_STREAM)
    sockobj.connect((host, port))

    # two file objects wrap around the same socket
    ifile = sockobj.makefile("r")
    ofile = sockobj.makefile("w")

    sys.stdin = ifile
    sys.stdout = ofile
    return sockobj


def redirect_both_as_sever(port=port, host=host):
    """
    connect caller's standard input stream and output stream to same socket
    in this mode, caller is server to a client: receives messages, send reply
    """
    sockobj = socket(AF_INET, SOCK_STREAM)
    sockobj.bind((host, port))
    sockobj.listen(5)

    conn, addr = sockobj.accept()
    ofile = sockobj.makefile("w")
    ifile = sockobj.makefile("r")

    sys.stdin = ifile
    sys.stdout = ofile
    return conn
