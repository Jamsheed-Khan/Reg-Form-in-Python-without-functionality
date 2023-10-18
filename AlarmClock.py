from tkinter import *
root = Tk()


root.geometry('400x300')


Label(root,text="Alarm Clock",font="ar 15 bold").grid(row=0,column=2)
Label(root,text="Set Time").grid(row=1,column=4)
SettimeValue = StringVar
SetTime = Entry(root,textvariable=SettimeValue).grid(row=1,column=5)


root.mainloop()
