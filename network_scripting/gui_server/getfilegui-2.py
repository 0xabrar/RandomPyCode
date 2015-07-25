"""
################################################################
same as other, but with grids and import+call, not command line
################################################################
"""

import getfile
from tkinter import *
from tkinter.messagebox import showinfo

def on_submit():
	getfile.client(content["Server"].get(),
		int(content["Port"].get()),
		content["File"].get())
	showinfo("getfilegui-2", "Download Complete")


box = Tk()
labels = ["Server", "Port", "File"]
row_num = 0
content = {}
for label in labels:
	Label(box, text=label).grid(column=0, row=row_num)
	entry = Entry(box)
	entry.grid(column=1, row=row_num, sticky=E+W)
	content[label] = entry
	row_num += 1

box.columnconfigure(0, weight=0) 	# makes expandable
box.columnconfigure(1, weight=1)
Button(text="Submit", command=on_submit).grid(row=row_num, column=0, columnspan=2)

box.title("GetFile GUI")
box.bind("<Return>", (lambda event: on_submit()))
mainloop()