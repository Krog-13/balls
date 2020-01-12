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


class one_ball:
    def __init__(self):
        self.r = 20
        self.x = 30
        self.y = 40
        self.dx, self.dy = (+1, +1)
        self.ball_1 = canv.create_oval(10,20,50,60, fill='green', activefill='red',outline='blue')


    def move(self):
        self.x += 2
        self.y += 2
    def show(self):
        canv.move(self.ball_1, self.x, self.y)
    def bank(self):
        print('Degrise')
        

def canv_clik(event):
    print('I can see that', event.x, event.y)

def tik_tok():
    for i in range(1):
        a.move()
        a.show()
    root.after(800, tik_tok)
def main():
    global balls,a
    canv.bind('<Button-1>', canv_clik)
    #balls = [one_ball() for i in range(2)]
    a = one_ball()
    tik_tok()
    tk.mainloop()

def score():
    global i
    i+=1
    l['text']=str(i)

def click(event):
    a = sqrt(((x-event.x)**2) + ((y-event.y)**2))
    canv.itemconfig(t, fill='green',outline='red',width=5)
    if a <= r:
        time.sleep(1)
        canv.delete(t)
        score()
    else:
        print('faill')

if __name__ == '__main__':
    main()

#canv.bind('<Button-3>', click)
#tk.mainloop()