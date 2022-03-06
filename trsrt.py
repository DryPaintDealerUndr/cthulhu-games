import pygame as pg
import random as rdm
import keyboard
from pygame import Color, Surface
from dependancies.screenshotter.screenshotter import *

WIDTH = 640
HEIGHT = 480
EMPTY = Color(0,0,0,0)

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Drawing app")
bg = pg.image.load("tringle-todo.png")
clock = pg.time.Clock()

#I create a transparant canvas
canvas = pg.Surface([640,480], pg.SRCALPHA, 32)

def main():
    is_running = True
    while is_running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    is_running = False
            elif event.type == pg.MOUSEMOTION:
                if pg.mouse.get_pressed()[0]:
                    #if mouse 1 is pressed, you draw a circle on the location of the cursor
                    location = (pg.mouse.get_pos())
                    pg.draw.circle(canvas, (0,0,0), location, 10)

            elif keyboard.is_pressed('c'):
                #clear canvas on mouse button 3 press
                canvas.fill(EMPTY)
            elif keyboard.is_pressed('p'):
                pg.image.save(screen, "screenshots/"+str(rdm.randint(1000,9000))+".png")

        #I blit the background first!
        screen.blit(bg,(0,0))

        #afterwards I overwrite it with a transparant canvas with the drawing I want
        screen.blit(canvas,(0,0))

        pg.display.update()
        clock.tick(60000)

if __name__ == "__main__":
    main()
