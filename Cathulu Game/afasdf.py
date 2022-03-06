from tkinter import *
import random as rdm
import time
import keyboard
from dependancies.movementfile import *
from PIL import ImageGrab
from dependancies.screenshotter.screenshotter import *

ws = Tk()
ws.title('PythonGuides')
ws.geometry('768x576')
ws.config(bg='#345')

canvas = Canvas(
    ws,
    height=576,
    width=768,
    bg="#fff"
    )
   
canvas.pack()

x = 576/2
y = 768/2
color = "red"
oval=canvas.create_oval(x, y, x + 40, y + 40, fill=color)

while True:
    canvas.update()
    if keyboard.is_pressed('w') and not keyboard.is_pressed('s') and not keyboard.is_pressed('a') and not keyboard.is_pressed('d'):
        moveup(canvas,oval)
        time.sleep(.03)
    elif keyboard.is_pressed('s') and not keyboard.is_pressed('w') and not keyboard.is_pressed('a') and not keyboard.is_pressed('d'):
        movedown(canvas,oval)
        time.sleep(.03)
    elif keyboard.is_pressed('a') and not keyboard.is_pressed('s') and not keyboard.is_pressed('w') and not keyboard.is_pressed('d'):
        moveleft(canvas,oval)
        time.sleep(.03)
    elif keyboard.is_pressed('d') and not keyboard.is_pressed('s') and not keyboard.is_pressed('w') and not keyboard.is_pressed('a'):
        moveright(canvas,oval)
        time.sleep(.03)
    elif keyboard.is_pressed('w') and keyboard.is_pressed('a'):
        movediagonalleftup(canvas,oval)
        time.sleep(.03)
    elif keyboard.is_pressed('s') and keyboard.is_pressed('d'):
        movediagonalrightdown(canvas,oval)
        time.sleep(.03)
    elif keyboard.is_pressed('s') and keyboard.is_pressed('a'):
        movediagonalleftdown(canvas,oval)
        time.sleep(.03)
    elif keyboard.is_pressed('w') and keyboard.is_pressed('d'):
        movediagonalrightup(canvas,oval)
        time.sleep(.03)
    elif keyboard.is_pressed('p'):
        cap = CAP(ws)
        cap.capture("screenshots/"+str(rdm.randint(1000,9000))+".png")
    print(canvas.coords(oval))

root.mainloop()
keyboard.on_press_key("w", lambda _:moveup())
