"""
spawn FTP get and put GUIs no matter what directory run from
"""

import os, sys
print("Running in, " os.getcwd())

# from PP4E.Launcher import findFirst
# mydir = os.path.split(findFirst(os.curdir, 'PyFtpGui.pyw'))[0]

from PP4E.Tools.find import findlist
mydir = os.path.dirname(findlist("PyFtpGUI.pyw", startdir=os.curdir)[0])

if sys.platform[:3] == "win":
	os.system("start %s\getfilegui.py" % mydir)
	os.system("start %s\putfilegui.py" % mydir)
else:
	os.system("python %s\getfilegui.py" % mydir)
	os.system("python %s\putfilegui.py" % mydir)