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

    deadlmao=ImageTk.PhotoImage(file="./debt-screen.png")
    
    i=0
    x = 720/2
    y = 960/2
    color = "red"
    canvas.create_oval(x, y, x + 40, y + 40, fill=color)
    oval=bkgrd
    rand=rdm.randint(440,540)
    rand2=rdm.randint(200,260)
    rando=rand
    rando2=rand2
    playing = True
    while playing == True:
        if i%rando == 0:
            rand=rdm.randint(440,540)
            rand2=rdm.randint(200,260)
            rando=rand
            rando2=rand2
        #print(rando,"and",rando2) -- debug
        canvas.update()
        if keyboard.is_pressed('d') and not keyboard.is_pressed('s') and not RedLightOn==True:
            if i%12 == 0:
                moveleft(canvas,oval)
        elif keyboard.is_pressed('d') and RedLightOn==True:
            print("dead")
            canvas.itemconfig(oval, image = greenlight)
            canvas.coords(oval)[0]=0
            playing = False
        if i >= rando2:
            RedLightOn=True
            i=i+1
            if i == rando:
                i=0
        elif i < rando2:
            RedLightOn=False
            i=i+1
        if RedLightOn==True:
            canvas.itemconfig(lights, image = redlight)
        elif RedLightOn==False:
            canvas.itemconfig(lights, image = greenlight)
        print(i)
        # print(rando,"and",rando2) -- debug


    ws.mainloop()
if __name__ == "__main__":
    main()
