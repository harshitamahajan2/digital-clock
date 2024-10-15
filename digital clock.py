from tkinter import *
from time import strftime
root=Tk()

def clk():
    res=strftime('%d-%b-%Y %A %H:%M:%S %p')
    x.config(text=res)
    x.after(1000,clk)
    
x=Label(root,bg='black',fg='red', font='Arial 65 bold')
x.pack()

clk()

root.mainloop()
