from tkinter import *
from court import *
from Ball import *

width, height = 745,374


win = Tk()
win.title("Tennis Game")
win.geometry("745x374+150+150")
win.resizable(False,False)
court = Court(win, 745,374,"court.png")

x1,y1 = width/2, height/2
x2,y2 = x1+30, y1+30

ball = Ball(court,x1,y1,x2,y2)

def play_game() :
    if ball.x1 <= 5 :
        winner = "green"

    if ball.x1 + ball.width >= court.width - 5 :
        winner = "red"
    ball.move_ball()
    win.after(50,play_game)



def score() :
    global green_score,red_score,winner

    if winner == "red" :
        red_score += 1
        winner = ""

    elif winner == "green" :
        green_score += 1
        winner = ""
    court.draw_score(red_score,green_score)

def restart(event) :
    score()
    red_racket.start_position()
    green_racket.start_position()
    ball.start_ball()





play_game()
win.mainloop()

    

