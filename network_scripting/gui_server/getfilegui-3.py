"""
=====================================================
launch getfile client with a reusable GUI form class
os.chdir to target local dir if input
=====================================================
"""

# TODO: use threads, show download status and getfile prints

from forms import Form
from tkinter import Tk, mainloop
from tkinter.messagebox import showinfo
import getfile, os

class GetfileForm(Form):

	def __init__(self, one_shot=False):
		root = Tk()
		root.title("Getfile GUI")
		labels = ["Server Name", "Port Number", "File Name", "Local Dir?"]
		Form.__init__(self, labels, root)
		self.one_shot = one_shot

	def on_submit(self):
		Form.on_submit(self)
		localdir = self.content["Local Dir?"].get()
		portnum = self.content["Port Number"].get()
		filename = self.content["File Name"].get()
		servername = self.content["Server Name"].get() 
		if localdir:
			os.chdir(localdir)
		portnum = int(portnum)
		getfile.client(servername, portnum, filename)
		showinfo("getfilegui-3", "Download Complete")
		if self.one_shot: Tk().quit()

if __name__ == "__main__":
	GetfileForm()
	mainloop()