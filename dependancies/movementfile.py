from tkinter import *
import random as rdm
import time
import keyboard

def moveup(canvas,oval):
    if canvas.coords(oval)[1] > 0:
        canvas.move(oval, 0, -5)
    else:
        print("Out of Bounds")
def moveright(canvas,oval):
    if canvas.coords(oval)[2] < 768:
        canvas.move(oval, 5, 0)
    else:
        print("Out of Bounds")
def movedown(canvas,oval):
    if canvas.coords(oval)[3] < 576:
        canvas.move(oval, 0, 5)
    else:
        print("Out of Bounds")
def moveleft(canvas,oval):
    if canvas.coords(oval)[0] > 0:
        canvas.move(oval, -5, 0)
    else:
        print("Out of Bounds")
def movediagonalleftup(canvas,oval):
    if canvas.coords(oval)[0] > 0 and canvas.coords(oval)[1] > 0:
        canvas.move(oval, -5, -5)
    else:
        print("Out of Bounds")
def movediagonalrightdown(canvas,oval):
    if canvas.coords(oval)[2] < 768 and canvas.coords(oval)[3] < 576:
        canvas.move(oval, 5, 5)
    else:
        print("Out of Bounds")
def movediagonalleftdown(canvas,oval):
    if canvas.coords(oval)[0] > 0 and canvas.coords(oval)[3] < 576:
        canvas.move(oval, -5, 5)
    else:
        print("Out of Bounds")
def movediagonalrightup(canvas,oval):
    if canvas.coords(oval)[2] < 768 and canvas.coords(oval)[1] > 0:
        canvas.move(oval, 5, -5)
    else:
        print("Out of Bounds")
