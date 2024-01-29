#https://docs.python.org/3/library/tkinter.html#module-tkinter

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

from math import *
def evaluate(event):
    res.configure(text = "Answer: " + str(eval(entry.get())))
w = Tk()
Label(w, text="Your Expression:").pack()
entry = Entry(w)
entry.bind("<Return>", evaluate)
entry.pack()
res = Label(w)
res.pack()
w.mainloop()
