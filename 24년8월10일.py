##from tkinter import *
##
##win = Tk()
##canvas = Canvas(win, width = 200, height = 100, bg = "white")
##canvas.pack()
##
##canvas.create_oval(10,10,60,60, fill = "blue")
##canvas.create_rectangle(100, 10, 160, 60, fill = "yellow", outline = "red")
##
##win.mainloop()
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##from tkinter import *
##
##win = Tk()
##canvas = Canvas(win, width = 200, height = 100, bg = "white")
##canvas.pack()
##
##canvas.create_polygon(100,10,30,90,160,90, fill = "red")
##win.mainloop()
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##from tkinter import *
##
##win = Tk()
##canvas = Canvas(win, width = 200, height = 200, bg = "white")
##canvas.pack()
##
##x1,y1 = 0, 0
##x2,y2 = 0,200
##
##for i in range(9) :
##    x1 += 20
##    x2 = x1
##    canvas.create_line(x1,y1,x2,y2)
##
##
##x3,y3 = 0,0
##x4,y4 = 200,0
##
##for i in range(9) :
##    y3 += 20
##    y4 = y3
##    canvas.create_line(x3,y3,x4,y4)

##canvas.create_oval(40, 40, 160, 160, fill = "blue", outline = "black")
##canvas.create_oval(60,60,140,100, fill = "blue", outline = "black")
    
##canvas.create_rectangle(20,20,160,100, fill = "yellow", outline = "black")
##canvas.create_rectangle(60,20,120,180, fill = "yellow", outline = "black")

##canvas.create_polygon(100,20,20,180,180,180, fill = "red")
##canvas.create_polygon(40,180,160,180,40,20,fill = "red")
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##from tkinter import *
##from random import *
##
##def draw_shape(event) :
##    color = ["black", "white", "blue", "red", "green", "yellow"]
##    x1,y1 = event.x, event.y
##    x2,y2 = x1 + randint(10, 70), y1 + randint(10, 70)
##    canvas.create_rectangle(x1,y1,x2,y2, fill = color[randint(0, 5)])
##
##win = Tk()
##canvas = Canvas(win, width = 300, height = 300, bg = "white")
##canvas.pack()
##canvas.bind("<Double-Button-1>", draw_shape)
##
##win.mainloop()
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##from tkinter import *
##from random import *
##
##def draw_shape(event) :
##    x1,y1 = event.x-25,event.y
##    x2,y2 = x1+ randint(50, 50), y1 + randint(50,50)
##    canvas.create_oval(x1,y1,x2,y2, fill = "yellow", outline = "black")    
##
##
##win = Tk()
##canvas = Canvas(win, width = 300, height = 300, bg = "white")
##canvas.pack()
##
##canvas.bind("<Double-Button-1>", draw_shape)
##win.mainloop()
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##from tkinter import *
##from random import *
##
##def draw_shape(event) :
##    x1,y1 = event.x-25,event.y
##    x2,y2 = event.x,event.y+25
##    x3,y3 = event.x+50,event.y+25
##    canvas.create_rectangle(x1,y1,x2,y2,x3,y3,fill = "green")
##
##win = Tk()
##canvas = Canvas(win, width = 300, height = 300, bg = "white")
##canvas.pack()
##
##canvas.bind("<Double-Button-1>", draw_shape)
##win.mainloop()
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
from tkinter import *
win = Tk()
canvas = Canvas(win, width = 500, height = 500, bg = "white")

btn_black = Button(win, text = "black", bg = "black", fg = "white", width = 8)
btn_blue = Button(win, text = "blue", bg = "blue", fg = "white", width = 8)
btn_green = Button(win, text = "green", bg = "green", fg = "white", width = 8)
btn_white = Button(win, text = "white", bg = "white", fg = "black", width = 8)
btn_red = Button(win, text = "red", bg = "red", fg = "white", width = 8)
btn_yellow = Button(win, text = "yellow", bg = "yellow", fg = "black", width = 8)

btn_canvas = Button(win, text = "canvas\ncolor", bg  = "white", width = 8)
btn_pen = Button(win, text = "pen\ncolor", bg  = "white", width = 8)
btn_fill = Button(win, text = "fill\ncolor", bg  = "white", width = 8)

btn_plus = Button(win, text = "+", bg = "white",width = 8)
btn_minus = Button(win, text = "-", bg = "white",width = 8)
btn_clear = Button(win, text = "clear", bg = "white",width = 8)

btn_oval = Button(win,text = "○", bg = "white",width = 8)
btn_rect = Button(win,text = "□", bg = "white",width = 8)
btn_poly= Button(win,text = "△", bg = "white",width = 8)

canvas.grid(row = 0, column = 0, columnspan = 5)
btn_canvas.grid(row=1,column = 0)
btn_black.grid(row=1,column = 1)
btn_blue.grid(row=1,column = 2)
btn_green.grid(row=1,column = 3)
btn_plus.grid(row=1,column = 4)
btn_pen.grid(row=2,column = 0)
btn_white.grid(row=2,column = 1)
btn_red.grid(row=2,column = 2)
btn_yellow.grid(row=2,column = 3)
btn_minus.grid(row=2,column = 4)
btn_fill.grid(row=3,column = 0)
btn_oval.grid(row=3,column = 1)
btn_rect.grid(row=3,column = 2)
btn_poly.grid(row=3,column = 3)
btn_clear.grid(row=3,column = 4)



