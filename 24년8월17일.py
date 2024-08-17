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
##canvas.create_polygon(100,10,30,90,160,90, fill = "red")
##win.mainloop()
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
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
##
##
##canvas.create_oval(40, 40, 160, 160, fill = "blue", outline = "black")
##canvas.create_oval(60,60,140,100, fill = "blue", outline = "black")
##    
##canvas.create_rectangle(20,20,160,100, fill = "yellow", outline = "black")
##canvas.create_rectangle(60,20,120,180, fill = "yellow", outline = "black")
##
##canvas.create_polygon(100,20,20,180,180,180, fill = "red")
##canvas.create_polygon(40,180,160,180,40,20,fill = "red")
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
from tkinter import *
win = Tk()
pen_color = "black"
pen_size = 2
shape_size = 10
my_tool = "pen"
fill_color = "white"


def paint(event) :
    global pen_size, pen_color
    x1,y1 = event.x,event.y
    x2,y2 = event.x + pen_size, event.y + pen_size
    canvas.create_line(x1,y1,x2,y2, width = pen_size, fill = pen_color)




def draw_shape(event) :
    global shape_size, my_tool
    x1,y1 = event.x,event.y
    x2,y2 = event.x + shape_size, event.y + shape_size

    if my_tool == "oval" :
        canvas.create_oval(x1-(shape_size/2),y1,x2-(shape_size/2),y2,fill = fill_color)
    elif my_tool == "rect" :
        canvas.create_rectangle(x1,y1,x2,y2, fill = fill_color)

    elif my_tool == "poly" :
        canvas.create_polygon(x1,y1,x2,y2,(x1-(shape_size)), y2,fill = fill_color,outline = "black")



def change_size(btn) :
    global pen_size,shape_size,my_tool
    if my_tool == "pen" :
        if btn == "plus" :
            pen_size += 1
        elif btn == "minus" and pen_size > 2:
            pen_size -= 1

    else :
        if btn == "plus" :
            shape_size += 10

        elif btn == "minus" :
            shape_size -= 10 and shape_size > 10
    
        
def change_color(color) :
    global pen_color, fill_color,my_tool
    if my_tool == "pen" :
        pen_color = color
    elif my_tool == "canvas" :
        canvas['bg'] = color
    else :
        fill_color = color
        
def clear_canvas() :
    canvas.delete("all")

def change_tool(tool) :
    global my_tool
    my_tool = tool

canvas = Canvas(win, width = 500, height = 500, bg = "white")

btn_black = Button(win, text = "black", bg = "black", fg = "white", width = 8,command = lambda : change_color("black"))
btn_blue = Button(win, text = "blue", bg = "blue", fg = "white", width = 8,command = lambda : change_color("blue"))
btn_green = Button(win, text = "green", bg = "green", fg = "white", width = 8,command = lambda : change_color("green"))
btn_white = Button(win, text = "white", bg = "white", fg = "black", width = 8,command = lambda : change_color("white"))
btn_red = Button(win, text = "red", bg = "red", fg = "white", width = 8,command = lambda : change_color("red"))
btn_yellow = Button(win, text = "yellow", bg = "yellow", fg = "black", width = 8,command = lambda : change_color("yellow"))

btn_canvas = Button(win, text = "canvas\ncolor", bg  = "white", width = 8,command = lambda : change_tool("canvas"))
btn_pen = Button(win, text = "pen\ncolor", bg  = "white", width = 8,command = lambda : change_tool("pen"))
btn_fill = Button(win, text = "fill\ncolor", bg  = "white", width = 8,command = lambda : change_tool("shape"))

btn_plus = Button(win, text = "+", bg = "white",width = 8,command = lambda : change_size("plus"))
btn_minus = Button(win, text = "-", bg = "white",width = 8,command = lambda : change_size("minus"))
btn_clear = Button(win, text = "clear", bg = "white",width = 8,command = clear_canvas)

btn_oval = Button(win,text = "○", bg = "white",width = 8,command = lambda : change_tool("oval"))
btn_rect = Button(win,text = "□", bg = "white",width = 8,command = lambda : change_tool("rect"))
btn_poly= Button(win,text = "△", bg = "white",width = 8,command = lambda : change_tool("poly"))

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

win.bind("<B1-Motion>",paint)
win.bind("<Double-Button-1>",draw_shape)
win.mainloop()
