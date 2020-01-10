import tkinter
from tkinter import ttk

root = tkinter.Tk()
label = tkinter.Label(root, text="Hello World!")
label.pack()
tkinter.Button(root, text="Click me").pack()
ttk.Button(root, text="Click me").pack()
root.mainloop()