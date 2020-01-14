import tkinter as tk
from random import randrange as rnd, choice
import time
from math import *

root = tk.Tk()
root.geometry('600x500')
canv = tk.Canvas(root, bg='white')
canv.pack(fill='both', expand=2)
colors=['red','yellow','blue','green','orange']
l = tk.Label(root, anchor='sw', bg='black', width=20,fg='white',text='Score')
l.pack()
l['text']='0'
his_name = tk.Entry(root, width=20)
his_name.pack()
his_name.insert(4, "Enter you name:")
name = tk.Label(root, width=40, bg='black', fg='white')
b = tk.Button(text='Go start')
b.pack()
name.pack()
i=0


class one_ball:
    def __init__(self):
        self.i = 0
        self.r = 20
        self.x = 25
        self.y = 45
        self.dx, self.dy = (+2, +2)
        self.ball_1 = canv.create_oval(10,20,50,60, fill='green', activefill='red',outline='blue')


    def move(self):
        self.x += self.dx
        self.y += self.dy
    def show(self):
        canv.move(self.ball_1, self.dx, self.dy)

    def bank(self,event):
        global i
        ae = sqrt(((self.x-event.x)**2) + ((self.y-event.y)**2))
        canv.itemconfig(self.ball_1, fill='green',outline='red',width=5)
        if ae <= self.r:
            canv.delete(self.ball_1)
            i+=1
            l['text']=str(i)

        else:
            print('miss')


def canv_clik(event):
    global i
    a.bank(event)
    #i+=1
    #l['text']=str(i)

def start(event):
    global a
    s = his_name.get()
    if len(s) > 15:
        s=s[15:]
        name['text']='Hello' + s
        a = one_ball()
        tik_tok()

def tik_tok():
    for i in range(1):
        a.move()
        a.show()
    root.after(50, tik_tok)

def main():
    global balls,a
    canv.bind('<Button-1>', canv_clik)
    b.bind('<Button-3>', start)
    #a = one_ball()
    #tik_tok()
    tk.mainloop()

def score():
    global i
    i+=1
    l['text']=str(i)

def click(event):
    a = sqrt(((x-event.x)**2) + ((y-event.y)**2))
    canv.itemconfig(t, fill='green',outline='red',width=5)
    if a <= r:
        a.bank()
    else:
        print('faill')

if __name__ == '__main__':
    main()



#canv.bind('<Button-3>', click)
#tk.mainloop()