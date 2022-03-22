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

    #Background and Blank lights images
    background_image=ImageTk.PhotoImage(file="./IstandwithUkraine.png")
    background_image2=ImageTk.PhotoImage(file="./lights.png")

    canvas = Canvas(
        ws,
        height=720,
        width=960
        )

    canvas.pack()

    #Background and Blank lights creation
    bkgrd=canvas.create_image(0,0,image=background_image,anchor="nw")
    lights=canvas.create_image(0,0,image=background_image2,anchor="nw")

    #Countdown images
    three=ImageTk.PhotoImage(file="./Three.png")
    two=ImageTk.PhotoImage(file="./Two.png")
    one=ImageTk.PhotoImage(file="./One.png")

    #Lights images
    redlight=ImageTk.PhotoImage(file="./lights-red.png")
    greenlight=ImageTk.PhotoImage(file="./lights-green.png")

    #Death screen
    deadlmao=ImageTk.PhotoImage(file="./debt-screen.png")

    #Countdown creation
    countdown=canvas.create_image(960-133,0,image=three,anchor="ne")
    canvas.itemconfig(countdown, state='hidden')
    
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
            rand=rdm.randint(880,1080)
            rand2=rdm.randint(400,520)
            rando=rand
            rando2=rand2
        #print(rando,"and",rando2) -- debug
        canvas.update()
        if keyboard.is_pressed('d') and not keyboard.is_pressed('s') and not RedLightOn==True:
            if i%12 == 0:
                moveleft(canvas,oval)
        elif keyboard.is_pressed('d') and RedLightOn==True:
            print("dead")
            canvas.create_image(0,0,image=deadlmao,anchor="nw")
            playing = False
        if i >= rando2:
            RedLightOn=True
            i=i+1
            canvas.itemconfig(countdown, state='hidden')
            if i == rando:
                i=0
        elif i < rando2:
            RedLightOn=False
            i=i+1
            if i >= rando2-90 and not i ==rando2:
                canvas.itemconfig(countdown, state='normal')
                canvas.itemconfig(countdown, image = three)
                if i >= rando2-60 and not i >= rando2-30:
                    canvas.itemconfig(countdown, image = two)
                elif i >= rando2-30 and not i >= rando2:
                    canvas.itemconfig(countdown, image = one)
            else:
                canvas.itemconfig(countdown, state='hidden')
        if RedLightOn==True:
            canvas.itemconfig(lights, image = redlight)
        elif RedLightOn==False:
            canvas.itemconfig(lights, image = greenlight)
        print(i)
        # print(rando,"and",rando2) -- debug


    ws.mainloop()
if __name__ == "__main__":
    main()
