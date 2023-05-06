import pyshorteners
from tkinter import *

win =Tk()
win.geometry("500x400")
win.configure(bg="light gray")

def short():
    url=entry1.get()
    s = pyshorteners.Shortener().tinyurl.short(url)
    entry2.insert(END,s)

Label(win,text="ENTER YOUR URL LINK",font="impack 17 bold",bg="light gray",fg="black",bd=5).pack(fill="x",pady=10)

entry1= Entry(win ,font="15",bd=5,width=40,fg="black",bg="light gray")
entry1.pack(pady=20)

Button(win ,text="CLICK ME",font="impack 12 bold",bg="dark gray",fg="black",width="15",bd=5,command=short).pack(pady=20)

Label(win,text="SHORTED URL",font="impack 17 bold",bg="light gray",fg="black",bd=3).pack(fill="x",pady=20)
entry2=Entry(win,font=15,bd=5,width=40,fg="black",bg="light gray")
entry2.pack(pady=20)
mainloop()

