from tkinter import *

root = Tk()
root.geometry('290x150')
root.resizable(0,0)
root.title("Sum of Two Numbers")

num1=IntVar()
num2=IntVar()
Sum=IntVar()

def Fun():
    add = num1.get() + num2.get()
    Sum.set(add)

def Clear():
    num1.set("")
    num2.set("")
    Sum.set("")

Clear()

Label(root,text="Enter First Number: ").place(x=15,y=5)
e1 = Entry(root,textvariable=num1)
e1.focus_set()
e1.place(x=145,y=5)
Label(root,text="Enter Second Number: ").place(x=15,y=40)
Entry(root,textvariable=num2).place(x=145,y=40)

Button(root,text="Sum",command=Fun).place(x=100,y=80)
Button(root,text="Clear",command=Clear).place(x=150,y=80)

Entry(root,textvariable=Sum,state="readonly").place(x=80,y=120)

root.mainloop()