import sys

try:
    from tkinter import *
    import random as rdm
    import time
    #import portmantreq
    from PIL import ImageTk,Image
    import threading
    result="All dependancies installed"
except:
    result="Please install the Python dependancies in requirements.txt"
print(result)
