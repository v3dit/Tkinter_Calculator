from ast import operator
from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("500x400")
xyz = ""

equation = StringVar()
expression_field = Entry(top, textvariable=equation, fg='white', bg='black')
expression_field.grid(row="0",columnspan=6, ipadx=30)

b1 = Button(top, text=" 1 ", command=lambda: Cal("1"),
            activeforeground="red", activebackground="pink", height=1, width=7, fg='white', bg='black')
b2 = Button(top, text=" 2 ", command=lambda: Cal("2"),
            activeforeground="blue", activebackground="pink",  height=1, width=7, fg='white', bg='black')
b3 = Button(top, text=" 3 ", command=lambda: Cal("3"),
            activeforeground="green", activebackground="pink",  height=1, width=7, fg='white', bg='black')
b4 = Button(top, text=" 4 ", command=lambda: Cal("4"),
            activeforeground="yellow", activebackground="pink", height=1, width=7, fg='white', bg='black')
b5 = Button(top, text=" 5 ", command=lambda: Cal("5"),
            activeforeground="yellow", activebackground="pink", height=1, width=7, fg='white', bg='black')
b6 = Button(top, text=" 6 ", command=lambda: Cal("6"),
            activeforeground="yellow", activebackground="pink", height=1, width=7, fg='white', bg='black')
b7 = Button(top, text=" 7 ", command=lambda: Cal("7"),
            activeforeground="yellow", activebackground="pink", height=1, width=7, fg='white', bg='black')
b8 = Button(top, text=" 8 ", command=lambda: Cal("8"),
            activeforeground="yellow", activebackground="pink", height=1, width=7, fg='white', bg='black')
b9 = Button(top, text=" 9 ", command=lambda: Cal("9"),
            activeforeground="yellow", activebackground="pink", height=1, width=7, fg='white', bg='black')
b0 = Button(top, text=" 0 ", command=lambda: Cal("0"),
            activeforeground="yellow", activebackground="pink", height=1, width=7, fg='white', bg='black')

b1.grid(row=1, column=0, sticky=W)
b2.grid(row=1, column=2, sticky=W)
b3.grid(row=1, column=4, sticky=W)
b4.grid(row=2, column=0, sticky=W)
b5.grid(row=2, column=2, sticky=W)
b6.grid(row=2, column=4, sticky=W)
b7.grid(row=4, column=0, sticky=W)
b8.grid(row=4, column=2, sticky=W)
b9.grid(row=4, column=4, sticky=W)
b0.grid(row=6, column=2, sticky=W)

b10 = Button(top, text=" + ", command=lambda: Cal("+"),
             activeforeground="red", activebackground="pink", height=1, width=7, fg='white', bg='black')
b11 = Button(top, text=" - ", command=lambda: Cal("-"),
             activeforeground="red", activebackground="pink", height=1, width=7, fg='white', bg='black')
b12 = Button(top, text=" * ", command=lambda: Cal("*"),
             activeforeground="red", activebackground="pink", height=1, width=7, fg='white', bg='black')
b13 = Button(top, text=" / ", command=lambda: Cal("/"),
             activeforeground="red", activebackground="pink", height=1, width=7, fg='white', bg='black')
b14 = Button(top, text=" = ", command=lambda: ans(),
             activeforeground="red", activebackground="pink", height=1, width=7, fg='white', bg='black')
b15 = Button(top, text=" Clear ", command=lambda: clear(),
             activeforeground="red", activebackground="pink", height=1, width=7, fg='white', bg='black')

b10.grid(row=10, column=0, sticky=W)
b11.grid(row=10, column=2, sticky=W)
b12.grid(row=10, column=4, sticky=W)
b13.grid(row=12, column=0, sticky=W)
b14.grid(row=12, column=2, sticky=W)
b15.grid(row=12, column=4, sticky=W)

def Cal(n):
    global xyz
    xyz += n
    print(xyz)
    equation.set(xyz)

def ans():
    global xyz
    print(eval(xyz))
    equation.set(eval(xyz))
    xyz = ""

def clear():
    global xyz
    equation.set("")
    xyz = ""

def show_msg():
    messagebox.showinfo("Message", "Hey There! I hope you are doing well.")

mainloop()