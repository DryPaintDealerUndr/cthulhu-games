from tkinter import *
import redlight
import time
name = input("ENTER FULL NAME: ")
Id = int(input("Enter telephone number number :"))
def Continue():
    print("Starting test now")
    redlight.main()
    root.destroy()
root = Tk()
gibby = Label(root, text="-+-+-+-+- Q1. Is Taiwan a country-+-+-+-+-")
social = Button(root, text="       Yes        ", command=Continue)
social2 = Button(root, text="       No         ", command=Continue)
gibby.pack()
social.pack()
social2.pack()

root.mainloop()
