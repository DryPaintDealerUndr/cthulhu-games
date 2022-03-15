from tkinter import *
import random as rdm
import time
import keyboard
from dependancies.movementfileimg import *
from PIL import ImageTk,Image
import threading
#from dependancies.screenshotter.screenshotter import *

def main():
    RedLightOn=False
    ws = Tk()
    ws.title('PythonGuides')
    ws.geometry('960x720')
    ws.config(bg='#345')

    
    background_image=ImageTk.PhotoImage(file="./IstandwithUkraine.png")
    background_image2=ImageTk.PhotoImage(file="./lights.png")

    canvas = Canvas(
        ws,
        height=720,
        width=960
        )

    canvas.pack()

    bkgrd=canvas.create_image(0,0,image=background_image,anchor="nw")
    lights=canvas.create_image(0,0,image=background_image2,anchor="nw")

    redlight=ImageTk.PhotoImage(file="./lights-red.png")
    greenlight=ImageTk.PhotoImage(file="./lights-green.png")
    
    
    x = 720/2
    y = 960/2
    color = "red"
    canvas.create_oval(x, y, x + 40, y + 40, fill=color)
    oval=bkgrd
    
    def movement():
        while True:
            canvas.update()
            if keyboard.is_pressed('w') and not keyboard.is_pressed('s') and not keyboard.is_pressed('a') and not keyboard.is_pressed('d'):
                time.sleep(.03)
            elif keyboard.is_pressed('s') and not keyboard.is_pressed('w') and not keyboard.is_pressed('a') and not keyboard.is_pressed('d'):
                time.sleep(.03)
            elif keyboard.is_pressed('a') and not keyboard.is_pressed('s') and not keyboard.is_pressed('w') and not keyboard.is_pressed('d'):
                time.sleep(.03)
            elif keyboard.is_pressed('d') and not keyboard.is_pressed('s') and not keyboard.is_pressed('w') and not keyboard.is_pressed('a'):
                moveleft(canvas,oval)
                time.sleep(.03)
            elif keyboard.is_pressed('w') and keyboard.is_pressed('a'):
                time.sleep(.03)
            elif keyboard.is_pressed('s') and keyboard.is_pressed('d'):
                time.sleep(.03)
            elif keyboard.is_pressed('s') and keyboard.is_pressed('a'):
                time.sleep(.03)
            elif keyboard.is_pressed('w') and keyboard.is_pressed('d'):
                time.sleep(.03)
    def light():
        while True:
            if rdm.randint(1,3) == 2:
                RedLightOn=True
            else:
                RedLightOn=False
        
            if RedLightOn==False:
                canvas.itemconfig(lights, image = redlight)
                time.sleep(.1)
            else:
                canvas.itemconfig(lights, image = greenlight)
                time.sleep(.1)

    thread1 = threading.Thread(target=movement)
    thread1.start()
    
    thread2 = threading.Thread(target=light)
    thread2.start()

    ws.mainloop()
if __name__ == "__main__":
    main()
