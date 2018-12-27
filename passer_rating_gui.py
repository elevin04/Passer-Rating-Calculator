from tkinter import Tk, Label, Entry, Button, W, E
from calc_pass_rating import calc_passer_rating as cpr
from tkinter.messagebox import showinfo
from tkinter import PhotoImage
import pygame


def get_passer_rating():
    co = float(comp.get())
    t = float(td.get())
    yd = float(yds.get())
    inter = float(int.get())
    at = float(att.get())
    a = cpr.a(co, at)
    b = cpr.b(yd, at)
    c = cpr.c(t, at)
    d = cpr.d(inter, at)
    pygame.mixer.init()
    pygame.mixer.music.load('ding.mp3')
    pygame.mixer.music.play()
    showinfo('Passer Rating', round(cpr.passer_rating(a, b, c, d), 1))


root = Tk()
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='football.png'))
root.title('Passer Rating Calculator')
Label(root, text="Completions").grid(row=0)
Label(root, text="Touchdowns Passes").grid(row=1)
Label(root, text="Passing Yards").grid(row=2)
Label(root, text="Interceptions").grid(row=3)
Label(root, text="Passing Attempts").grid(row=4)

comp = Entry(root)
td = Entry(root)
yds = Entry(root)
int = Entry(root)
att = Entry(root)

comp.grid(row=0, column=1)
td.grid(row=1, column=1)
yds.grid(row=2, column=1)
int.grid(row=3, column=1)
att.grid(row=4, column=1)

Button(root, text='Quit', command=root.quit).grid(
    row=5, column=0, sticky=W, pady=4)

Button(root, text='Calculate', command=get_passer_rating).grid(
    row=5, column=1, sticky=E, pady=4)
root.mainloop()
