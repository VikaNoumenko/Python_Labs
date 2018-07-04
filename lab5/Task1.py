from tkinter import *
import time
import _thread


xCoor = 5
yCoor = 5
widthE = 75
heightE = 75

def Move(xCoor,yCoor,ellipse,widthE,heightE):
    while xCoor < 200:
        xCoor = xCoor + 5
        yCoor = yCoor + 5
        c.delete(ellipse)
        ellipse = c.create_oval(xCoor, yCoor, widthE, heightE)
        time.sleep(1)


c = Canvas(width=100, height=350, bg='grey80')
c.pack()
ellipse = c.create_oval(xCoor, yCoor, widthE, heightE)

_thread.start_new_thread(Move,(xCoor,yCoor,ellipse,widthE,heightE))
mainloop()



#
# def defColor():
#     c.itemconfig('all', fill = 'grey80')
#
# def changeColor():
#     while 1:
#         c.itemconfig(redOval, fill='red')
#         time.sleep(1)
#         defColor()
#         c.itemconfig(yellowOval, fill='yellow')
#         time.sleep(1)
#         defColor()
#         c.itemconfig(greenOval, fill='green')
#         time.sleep(1)
#         defColor()
#
# c = Canvas(width = 100, height = 350, bg = 'grey80')
# c.pack()
# redOval = c.create_oval(25,25,75,75)
# yellowOval = c.create_oval(25,85,75,135)
# greenOval = c.create_oval(25,145,75,195)
#
# _thread.start_new_thread(changeColor,())
#
# mainloop()
