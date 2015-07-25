"""
######################################################################
a reusable form class
######################################################################
"""

from tkinter import *
entry_size = 40

class Form: 

	def __init__(self, labels, parent=None):
		label_size = max(len(x) for x in labels) + 2
		box = Frame(parent)
		box.pack(expand=YES, fill=X)
		rows = Frame(box, bd=2, relief=GROOVE)
		rows.pack(side=TOP, expand=YES, fill=X)	
		self.content = {}

		for label in labels:
			row = Frame(box)
			row.pack(fill=X)
			Label(row, text=label, width=label_size).pack(side=LEFT)
			entry = Entry(row, width=entry_size)
			entry.pack(side=RIGHT, expand=YES, fill=X)
			self.content[label] = entry
		Button(box, text="Cancel", command=self.on_cancel).pack(side=RIGHT)
		Button(box, text="Submit", command=self.on_submit).pack(side=RIGHT)
		box.master.bind("<Return>", (lambda event: self.on_submit()))

	# ovveride method
	def on_submit(self):
		for key in self.content:
			print(key, "\t=>\t", self.content[key].get())

	def on_cancel(self):
		Tk().quit()

class DynamicForm(Form):

	def __init__(self, labels=None):
		labels = input("Enter field names: ")
		Form.__init__(self, labels)

	def on_submit(self):
		print("Field values...")
		Form.on_submit(self)
		self.on_cancel()

if __name__ == "__main__":
	import sys
	if len(sys.argv) == 1:
		Form(["Name", "Age", "Job"])
	else:
		DynamicForm()	# input forms, go away after submit
	mainloop()
