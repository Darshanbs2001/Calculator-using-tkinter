import tkinter
from  tkinter import *
root=tkinter.Tk()
root.geometry('270x400')
root.resizable(0,0)
root.title("claculator",)
global data
data=StringVar()
val=""
global a
a=0
global b
b=0
global count
count=0
global h
h=""
row0=Frame(root,bg="#ffffff")
row0.pack(expand=True,fill="both")
row1=Frame(root,bg="#ffffff")
row1.pack(expand=True,fill="both")
row2=Frame(root,bg="#ffffff")
row2.pack(expand=True,fill="both")
row3=Frame(root,bg="#ffffff")
row3.pack(expand=True,fill="both")
row4=Frame(root,bg="#ffffff")
row4.pack(expand=True,fill="both")
row5=Frame(root,bg="#ffffff")
row5.pack(fill="both")
Label(row5,text="This app was created by Darshan for the first time ").pack()
def btn1c():
    global val
    global a
    global h
    global b
    val = val + "1"
    if count==0:
        a=float(val)
    if count>0:
        h=h+"1"
        b=float(h)
    data.set(val)
def btn2c():
    global val
    global a
    global b
    global h
    val=val+"2"
    if count==0:

      a=float(val)
    if count>0:
        h = h + "2"
        b=float(h)
    data.set(val)
def btn3c():
    global val
    global a
    global b
    global h
    val = val + "3"
    if count == 0:
        a = float(val)
    if count > 0:
        h = h + "3"
        b = float(h)
    data.set(val)
def btn4c():
    global val
    global a
    global b
    global h
    val = val + "4"
    if count == 0:
        a =float(val)
    if count > 0:
        h = h + "4"
        b = float(h)
    data.set(val)
def btn5c():
    global val
    global a
    global b
    global h
    val = val + "5"
    if count == 0:
        a = float(val)
    if count > 0:
        h = h + "5"
        b = float(h)
    data.set(val)
def btn6c():
    global val
    global a
    global b
    global h
    val = val + "6"
    if count == 0:
        a = float(val)
    if count > 0:
        h = h + "6"
        b = float(h)
    data.set(val)
def btn7c():
    global val
    global a
    global b
    global h
    val = val + "7"
    if count == 0:
        a = float(val)
    if count > 0:
        h = h + "7"
        b = float(h)
    data.set(val)
def btn8c():
    global val
    global a
    global b
    global h
    val = val + "8"
    if count == 0:
        a = float(val)
    if count > 0:
        h = h + "8"
        b = float(h)
    data.set(val)
def btn9c():
    global val
    global a
    global b
    global h
    val = val + "9"
    if count == 0:
        a = float(val)
    if count > 0:
        h = h + "9"
        b = float(h)
    data.set(val)
def btn0c():
    global val
    global a
    global b
    global h
    val = val + "0"
    if count == 0:
        a = float(val)
        print(a)
    if count > 0:
        h = h + "0"
        b = float(h)
    data.set(val)
l=Label(row0,textvariable=data,
    text="hi",font=("arial",22),anchor="se")
l.pack(expand=True,fill="both",anchor="se",side=BOTTOM)
def clear():
    global a
    global b
    global val
    global count
    val=""
    a=0
    b=0
    count =0
    data.set(val)
def btnpc():
    global val
    global a
    global b
    global count
    count = count + 1
    global operator
    operator="+"
    val=val + "+"
    data.set(val)
def btnsc():
    global val
    global a
    global b
    global count
    count = count + 1
    global operator
    operator = "-"
    val = val + "-"
    data.set(val)
def btnmc():
    global val
    global a
    global b
    global count
    count = count + 1
    global operator
    operator = "*"
    val = val + "*"
    data.set(val)
def btndc():
    global val
    global a
    global b
    global count
    count = count + 1
    global operator
    operator = "/"
    val = val + "/"
    data.set(val)
def btnd():
    global val
    global a
    global b
    global h
    val = val + "."
    if count == 0:
        a = float(val)
    if count > 0:
        h = h + "."
        b = float(h)
    data.set(val)
def btnec():
   global val
   global a
   global b
   global c
   global count
   global h
   c=0
   if operator=="+":
     c = a + b
     a=c
     h=""
     b=0
     val = str(c)
     data.set(val)
   if operator=="-":
     c = a - b
     h=""
     a=c
     b=0
     val = str(c)
     data.set(val)
   if operator=="*":
     h=""
     c = a * b
     a=c
     b=0
     val = str(c)
     data.set(val)
   if operator=="/" :
     if b != 0:
      c = float(a / b)
      h=""
      a=c
      b=0
      val = str(c)
      data.set(val)
     else:
       c=str(c)
       c="illegal operations"
       data.set(c)
       c=0
   



btn1=Button(row1,text="1",font=("arial",22),command=btn1c,border=0)
btn1.pack(side=LEFT,expand=True,fill="both",)
btn2=Button(row1,text="2",font=("arial",22),command=btn2c,border=0)
btn2.pack(side=LEFT,expand=True,fill="both")
btn3=Button(row1,text="3",font=("arial",22),command=btn3c,border=0)
btn3.pack(side=LEFT,expand=True,fill="both")
btn4=Button(row1,text="+",font=("arial",22),command=btnpc,border=0)
btn4.pack(side=LEFT,expand=True,fill="both")
btn5=Button(row2,text="4",font=("arial",22),command=btn4c,border=0)
btn5.pack(side=LEFT,expand=True,fill="both")
btn6=Button(row2,text="5",font=("arial",22),command=btn5c,border=0)
btn6.pack(side=LEFT,expand=True,fill="both")
btn7=Button(row2,text="6",font=("arial",22),command=btn6c,border=0)
btn7.pack(side=LEFT,expand=True,fill="both")
btn8=Button(row2,text="-",font=("arial",22),command=btnsc,border=0,)
btn8.pack(side=LEFT,expand=True,fill="both")
btn9=Button(row3,text="7",font=("arial",22),command=btn7c,border=0)
btn9.pack(side=LEFT,expand=True,fill="both")
btn0=Button(row3,text="8",font=("arial",22),command=btn8c,border=0)
btn0.pack(side=LEFT,expand=True,fill="both")
btn10=Button(row3,text="9",font=("arial",22),command=btn9c,border=0)
btn10.pack(side=LEFT,expand=True,fill="both")
btn11=Button(row3,text="*",font=("arial",22),command=btnmc,border=0)
btn11.pack(side=LEFT,expand=True,fill="both")
btn12=Button(row4,text="C",font=("arial",22),command=clear,border=0)
btn12.pack(side=LEFT,expand=True,fill="both")
btn13=Button(row4,text="0",font=("arial",22),command=btn0c,border=0)
btn13.pack(side=LEFT,expand=True,fill="both")
btn14=Button(row4,text="=",font=("arial",22),command=btnec,border=0,)
btn14.pack(side=LEFT,expand=True,fill="both")
btn15=Button(row4,text="/",font=("arial",22),command=btndc,border=0,)
btn15.pack(side=LEFT,expand=True,fill="both")
btn16=Button(row4,text="(.)",font=("arial",22),command=btnd,border=0,)
btn16.pack(side=LEFT,expand=True,fill="both")
root.mainloop()

