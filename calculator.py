from tkinter import *


class Person():
	def __init__(self, name):
		self.name = name

	def changeName(self, name):
		self.name = name

	def printName(self):
		print(self.name)

root = Tk()
root.title("Tkinter Calculator")
root.minsize(150,100)
#Draw display
display = Entry(root)
display.grid(row=0, column=0, columnspan=4)

#draw buttons
btn_7 = Button(root, text="7").grid(row=1,column=0)
btn_8 = Button(root, text="8").grid(row=1, column=1)
btn_9 = Button(root, text="9").grid(row=1, column=2)
btn_mult = Button(root, text="X").grid(row=1, column=3)
btn_4 = Button(root, text="4").grid(row=2, column=0)
btn_5 = Button(root, text="5").grid(row=2, column=1)
btn_6 = Button(root, text="6").grid(row=2, column=2)
btn_sub = Button(root, text="-").grid(row=2, column=3)
btn_1 = Button(root, text="1").grid(row=3, column=0)
btn_2 = Button(root, text="2").grid(row=3, column=1)
btn_3 = Button(root, text="3").grid(row=3, column=2)
btn_add = Button(root, text="+").grid(row=3, column=3)
btn_0 = Button(root, text="0").grid(row=4, column=0)
btn_c = Button(root, text="C").grid(row=4, column=1)
btn_dot = Button(root, text=".").grid(row=4, column=2)
btn_equal = Button(root, text="=").grid(row=4, column=3)
root.mainloop()
