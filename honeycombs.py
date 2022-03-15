import pygame as pg
import random as rdm
import keyboard
import sqlite3
from pygame import Color, Surface
connection = sqlite3.connect("local_database\SquidBaseSQL.db")
#from dependancies.screenshotter.screenshotter import *
cur = connection.cursor()
def compare():
    
def add_data(task):

    sql = """INSERT INTO SquidBaseSQL(Name,Screenshot_ID,Game_1,Game_2,Game_3,Game_4,Game_5,Game_6,Selected_Shape)
          VALUES(?,?,?,?,?,?,?,?,?)"""
    cur.execute(sql, task)
    connection.commit()
    return cur.lastrowid

def mod_data(task):

    sql = """UPDATE SquidBaseSQL(Screenshot_ID)
          VALUES(?)"""
    cur.execute(sql, task)
    connection.commit()
    return cur.lastrowid


def get_screen():
    i=0
    with connection:
        cur=crsr
        val=cur.execute("SELECT Screenshot_ID FROM SquidBaseSQL WHERE Name == Kim Yoon Tae")
        return(val)

WIDTH = 640
HEIGHT = 480
EMPTY = Color(0,0,0,0)

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("AlexARGBOY5")
bg = pg.image.load("tringle-todo.png")
clock = pg.time.Clock()

#I create a transparant canvas
canvas = pg.Surface([640,480], pg.SRCALPHA, 32)

#data = ("Kim Yoon Tae",0,"False",0,"False","False","False","False") #todo: turn into input prompt
#add_data(data)

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
                cur.execute('SELECT Screenshot_ID FROM SquidBaseSQL WHERE Name == "Kim Yoon Tae"')
                number=cur.fetchall()[0]
                pg.image.save(screen, "screenshots/"+str(number)+".png")
                cur.execute('UPDATE SquidBaseSQL SET Screenshot_ID = Screenshot_ID + 1 WHERE Name = "Kim Yoon Tae"')
                

        #I blit the background first!
        screen.blit(bg,(0,0))

        #afterwards I overwrite it with a transparant canvas with the drawing I want
        screen.blit(canvas,(0,0))

        pg.display.update()
        clock.tick(60000)

if __name__ == "__main__":
    main()
