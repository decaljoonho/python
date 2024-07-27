##from tkinter import *
##win = Tk()
##canvas = Canvas(win, bg = "white", width = 500, height = 500)
##canvas.create_line(250,100, 250, 400 , fill = "red", width = 3)
##canvas.pack()
##win.mainloop()
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##from tkinter import *
##win = Tk()
##canvas = Canvas(win, bg = "white", width = 500, height = 100)
##canvas.pack()
##x1, y1 = 0,0
##x2, y2= 500,0
##
##for i in range(3) :
##    y1 += 30
##    y2 = y1
##
##    canvas.create_line(x1, y1,x2,y2, fill = "red", width = 3)
##
##win.mainloop()
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##from tkinter import *
##win = Tk()
##canvas = Canvas(win, bg = "white", width = 500, height = 100)
##canvas.pack()
##x1, y1 = 0,0
##x2, y2= 0,100
##
##for i in range(10) :
##    x1 += 45
##    x2 = x1
##
##    canvas.create_line(x1, y1,x2,y2, fill = "red", width = 3)
##
##win.mainloop()
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##from tkinter import *
##win = Tk()
##canvas = Canvas(win, bg = "white", width = 500, height = 500)
##canvas.pack()
##x1, y1 = 10,10
##x2, y2= 10,460
##
##for i in range(10) :
##    canvas.create_line(x1, y1,x2,y2, fill = "red", width = 3)
##    x1 += 50
##    x2 = x1
##
##x3 , y3 = 10, 10
##x4, y4 = 460, 10
##
##for i in range(10) :
##    canvas.create_line(x3,y3,x4,y4, fill = "blue", width = 3)
##    y3 += 50
##    y4 = y3
##
##
##win.mainloop()
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##from tkinter import *
##
##def paint(event) :
##    x1, y1 = event.x, event.y
##    x2 , y2 = x1 + 5, y1 + 5
##    canvas.create_line(x1, y1, x2, y2, width = 3)
##
##win = Tk()
##canvas = Canvas(win , bg = "white", width = 500, height = 200)
##canvas.pack()
##win .bind("<B1-Motion>", paint)
##
##win.mainloop()
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##from tkinter import *
##pen_color = "black"
##
##def paint(event) :
##    global pen_color
##    x1, y1 = event.x, event.y
##    x2, y2 = x1 + 5, y1 + 5
##    canvas.create_line(x1, y1, x2, y2, width = 3, fill = pen_color)
##
##
##def change_color() :
##    global pen_color
##    pen_color = "red"
##
##win = Tk()
##canvas = Canvas(win, bg = "white", width = 500, height = 200)
##btn = Button(win, text = "red", command = change_color)
##
##canvas.pack()
##btn.pack()
##
##win.bind("<B1-Motion>", paint)
##win.mainloop()
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
from tkinter import *
win = Tk()
pen_color = "black"
def paint(event) :
    global pen_color
    x1, y1 = event.x, event.y
    x2, y2 = x1 + 5, y1 + 5
    canvas.create_line(x1, y1, x2, y2, width = 3, fill = pen_color)

def change_color(color) :
    global pen_color
    pen_color = color

def clear() :
    canvas.delete("all")

canvas = Canvas(win, bg = "white", width = 500, height = 500)
btn_white = Button(win, text = "white", width  = 6, bg = "white",command = lambda : change_color("white"))
btn_black = Button(win, text = "black", width  = 6, bg = "black", fg = "white",command = lambda : change_color("black"))
btn_blue = Button(win, text = "blue", width  = 6, bg = "blue", fg = "white",command = lambda : change_color("blue"))
btn_green = Button(win, text = "green", width  = 6, bg = "green", fg = "white",command = lambda : change_color("green"))
btn_yellow = Button(win, text = "yellow", width  = 6, bg = "yellow",command = lambda : change_color("yellow"))
btn_red = Button(win, text = "red", width  = 6, bg = "red", fg = "white",command = lambda : change_color("red"))
btn_plus = Button(win, text = "+", width  = 6, bg = "white")
btn_minus = Button(win, text = "-", width  = 6, bg = "white")
btn_clear = Button(win, text = "clear", width  = 6, bg = "white")

canvas.grid(row = 0, column =0, columnspan = 9)
btn_white.grid(row = 1, column = 0)
btn_black.grid(row = 1, column = 1)
btn_blue.grid(row = 1, column = 2)
btn_green.grid(row = 1, column = 3)
btn_yellow.grid(row = 1, column = 4)
btn_red.grid(row = 1, column = 5)
btn_plus.grid(row = 1, column = 6)
btn_minus.grid(row = 1, column = 7)
btn_clear.grid(row = 1, column = 8)

win.bind("<B1-Motion>", paint)
win.mainloop()


