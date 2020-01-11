import tkinter as tk
from random import randrange as rnd, choice
import time
from math import *

root = tk.Tk()
root.geometry('600x500')
canv = tk.Canvas(root, bg='white')
canv.pack(fill='both', expand=2)
colors=['red','yellow','blue','green','orange']
l = tk.Label(root, anchor='sw', bg='black', width=20,fg='white')
l.pack()
l['text']='0'
i=0
def new_ball():
    global x,y,r,t
    canv.delete('all')
    x = rnd(100,500)
    y = rnd(100,250)
    r = rnd(30,50)
    t=canv.create_oval(x-r,y-r,x+r,y+r, fill=choice(colors), width=0)
    root.after(2000,new_ball)

def score():
    global i
    i+=1
    l['text']=str(i)

def click(event):
    a = sqrt(((x-event.x)**2) + ((y-event.y)**2))
    if a <= r:
        canv.itemconfig(t, fill='green',outline='red',width=5)
        canv.delete(t)
        score()
    else:
        print('faill')

new_ball()
canv.bind('<Button-3>', click)
tk.mainloop()