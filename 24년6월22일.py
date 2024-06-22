##def average(n, tot) :
##    avg = tot / n
##    return avg
##
##def total() :
##    tot = 0
##    score = input("score : ").split()
##
##    for i in score :
##        tot += int(i)
##
##    avg = average(len(score), tot)
##
##    print("total socre : %d" % tot)
##
##    print("average score : %.2f" % avg)
##
##total()
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##def even(n) :
##    if n == 0 :
##        return n
##    if n%2 == 0 :
##        print(n, end = ' ')
##    even(n-1)
##
##even(10)
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##def total(n) :
##    if n == 1 :
##        return 1
##
##    else :
##       return n + total(n-1)
##
##n = int(input("수 : "))
##print(total(n))
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##from tkinter import *
##
##win = Tk()
##label1 = Label(win, text = "one")
##label2 = Label(win, text = "two")
##label3 = Label(win, text = "three")
##label1.pack()
##label2.pack()
##label3.pack()
##win.mainloop()
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##from tkinter import *
##
##win = Tk()
##lbl1 = Label(win, text = "orange", width = 20, height = 3,relief = "solid")
##lbl2 = Label(win, text = "banana", font = ("Elephant", 20), bg = "yellow")
##lbl3 = Label(win, text = "apple", fg = "red")
##lbl1.pack()
##lbl2.pack()
##lbl3.pack()
##win.mainloop()
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##from tkinter import *
##
##win = Tk()
##img = PhotoImage(file = 'pizza.png')
##lbl1 = Label(win, image = img)
##lbl2 = Label(win, text = "pizza", bg = "yellow", fg = "red")
##lbl1.pack()
##lbl2.pack()
##win.mainloop()
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##from tkinter import *
##
##win = Tk()
##btn = Button(win, text = "Button")
##btn.pack()
##win.mainloop()
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##from tkinter import *
##
##win = Tk()
##
##def click() :
##    if btn['text'] == "red" :
##        btn['text'] = "blue"
##        btn['bg'] = "blue"
##    else :
##        btn['text'] = "red"
##        btn['bg'] = "red"
##
##btn = Button(win, text = "red", fg = "white", bg = "red" , command = click)
##btn.pack()
##win.mainloop()
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##from tkinter import *
##win = Tk()
##
##def click() :
##    if btn['text'] == "hello" :
##        btn['text'] = "python"
##        btn['bg'] = "green"
##
##    else :
##        btn['text'] = "hello"
##        btn['bg'] = "orange"
##
##btn = Label(win, text = "hello", bg = "orange", fg = "white")
##btn2 = Button(win, text = "button", fg = "black", bg = "white" , command = click)
##btn.pack()
##btn2.pack()
##win.mainloop()
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##from tkinter import *
##win = Tk()
##
##def message(event) :
##    lbl['text'] = entry.get()
##
##entry = Entry(win)
##entry.bind("<Return>", message)
##entry.pack()
##lbl = Label(win, text = "")
##lbl.pack()
##win.mainloop()
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
from tkinter import *

win = Tk()
win.title("grid")
label1 = Label(win, width = 10, height = 5, bg = "red")
label2 = Label(win, width = 10, height = 5, bg = "orange")
label3 = Label(win, width = 10, height = 5, bg = "yellow")
label4 = Label(win, width = 10, height = 5, bg = "green")
label5 = Label(win, width = 10, height = 5, bg = "blue")
label6 = Label(win, width = 10, height = 5, bg = "purple")







label1.grid(row = 0, column = 0 )
label2.grid(row = 0, column = 1 )
label3.grid(row = 0, column = 2)
label4.grid(row = 1, column = 0 )
label5.grid(row = 1, column = 1 )
label6.grid(row = 1, column = 2 )





win.mainloop()
