#***************************************************
#!/usr/bin/python
try:
    from Tkinter import *
except ImportError:
    from tkinter import *
#READ BELOW!!!!!
#***********************************************
#in python3 its tkinter with a small t
#in python2 it's a large T as in Tkinter
#***********************************************

def show_entry_fields():
   print("The number is: %s" % (num.get()))
#print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
#print num
# create a root window
root = Tk()
root.title("PLease enter a number")
root.geometry("300x200")
#create a frame in the window to hold other widgets
Label(root, text="Number").grid(row=8)
num = Entry(root)

num.grid(row=8, column=2)
app = Frame(root)
app.grid()


lbl = Label(app, text = "Java is KING")
lbl.grid()

Button(root, text='Exit', command=root.quit).grid(row=16, column=2, sticky=W, pady=4)
Button(root, text='Display', command=show_entry_fields).grid(row=15, column=2, sticky=W, pady=4)

#bttn1 = Button(app, text = "Die")
#bttn1.grid()


root.mainloop()

