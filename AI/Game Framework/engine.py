import tkinter as tk
from tkinter import *

class Game():
    def __init__(self, word):
        self.window = Tk()
        self.window.title("hi")


my = Game("hello")
lol_img = PhotoImage(file="./lol.png")

lol = Label(my.window, image = lol_img)
lol.place(x=0, y=0)



