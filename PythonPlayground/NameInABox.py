from tkinter import *
#READ BELOW!!!!
#***********************************************
#in python3 its tkinter with a small t
#in python2 it's a large T as in Tkinter
#***********************************************

def show_entry_fields():     
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
    # python 3.4 likes parentheses used in print statements
    print ("Go fuck yourself")   
  

master = Tk()
Label(master, text="First Name").grid(row=0)
#Label(master, text="Last Name").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Exit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Display', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )

