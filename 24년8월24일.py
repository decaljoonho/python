##from tkinter import *
##win = Tk()
##x1, y1 = 10, 10
##x2,y2 = x1 + 30, y1 + 30
##x_dist, y_dist = 1,1
##
##canvas = Canvas(win,width = 500, height = 500, bg = "white")
##ball = canvas.create_oval(x1,y1,x2,y2, fill = "yellow")
##
##def flow() :
##    global x1,y1,x2,y2
##    x1 += x_dist
##    y1 += y_dist
##    x2,y2 = x1 + 30, y1 + 30
##    canvas.coords(ball,x1,y1,x2,y2)
##    win.after(10, flow)
##
##flow()
##
##canvas.pack()
##win.mainloop()

from tkinter import *

class Court :

    def __init__(self, window, width, height, img) :
        self.canvas = Canvas(window, width = width, height = height)
        self.img = PhotoImage(file = img)
        self.canvas.create_image(width/2, height/2, image = self.img)

        self.width = width
        self.height = height

        self.canvas.pack()
