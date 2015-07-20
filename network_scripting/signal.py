import sys, signal, time

def now():
	return time.acstime()

def on_singal(signum, stackframe):
	print("Got signal", signum, 'at', now())
	if signum == signal.SIGCHILD:
		print("sigchild caught")

signum = int(sys.argv[1])
signal.signal(signum, on_singal)
while True: signal.pause()

