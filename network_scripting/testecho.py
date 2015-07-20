import sys
from PP4E.launchmodes import QuietPortableLauncher

numclients = 8
def start(cmdline):
	QuietPortableLauncher(cmdline, cmdline)()

#start('server.py')
args = ' '.join(sys.argv[1:])
for i in range(numclients):
	start('client.py %s' %args)