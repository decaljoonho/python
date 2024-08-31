##from tkinter import *
##from court import *
##from Ball import *
##
##width, height = 745,374
##
##
##win = Tk()
##win.title("Tennis Game")
##win.geometry("745x374+150+150")
##win.resizable(False,False)
##court = Court(win, 745,374,"court.png")
##
##x1,y1 = width/2, height/2
##x2,y2 = x1+30, y1+30
##
##ball = Ball(court,x1,y1,x2,y2)
##
##def play_game() :
##    if ball.x1 <= 5 :
##        winner = "green"
##
##    if ball.x1 + ball.width >= court.width - 5 :
##        winner = "red"
##    ball.move_ball()
##    win.after(50,play_game)
##
##
##
##def score() :
##    global green_score,red_score,winner
##
##    if winner == "red" :
##        red_score += 1
##        winner = ""
##
##    elif winner == "green" :
##        green_score += 1
##        winner = ""
##    court.draw_score(red_score,green_score)
##
##def restart(event) :
##    score()
##    red_racket.start_position()
##    green_racket.start_position()
##    ball.start_ball()
##
##
##
##
##
##play_game()
##win.mainloop()

from tkinter import *
from court import *                       # 사용자 정의 court 모듈 불러오기
from Ball import *                        # 사용자 정의 ball 모듈 불러오기
from racket import *                      # 사용자 정의 racket 모듈 불러오기

# 점수 매기는 함수
def score() :
    global green_score, red_score, winner
    if winner == "red" :
        red_score += 1
    elif winner == "green" :
        green_score += 1
    winner = ''
    # 점수 그리기 함수 호출하기
    court.draw_score(red_score, green_score)   
        
# 스페이스 바 눌렀을 때 호출될 함수
def replay(event) :
    score()
    red_racket.start_position()
    green_racket.start_position()
    ball.start_ball()

# 게임 진행 함수
def play_game() :
    global winner

    # 배트와 공의 충돌 감지하기
    red_racket.dectect_collision(ball)
    green_racket.dectect_collision(ball)

    # 공이 왼쪽 벽에 충돌했을 경우 승자 판단하기
    if ball.x1 <= 5 :
        winner = "green"
        ball.stop_ball()
    # 공이 오른쪽 벽에 충돌했을 경우 승자 판단하기
    if ball.x1 + ball.width >= court.width - 5 :
        winner = "red"
        ball.stop_ball()

    # ball 객체 움직이는 함수 호출하기
    ball.move_ball()

    # 1초에 50번 play_game()를 함수 호출하기
    win.after(50, play_game)


# 빨간 라켓 점수 초기화하기
red_score = 0        
# 초록 라켓 점수 초기화하기           
green_score = 0    
# 승리자 초기화하기
winner = ''                                                        
# 윈도 창과 캔버스의 가로, 세로 길이 초기화하기
width, height = 745, 374

win = Tk()
win.title("Tennis Game")
win.geometry("745x374+150+150")
win.resizable(False, False)

# Court 클래스 생성하기
court = Court(win, width, height, "court.png")
# 공의 좌표를 캔버스의 중앙으로 저장하기
x1, y1 = width / 2, height / 2
x2, y2 = x1 + 30, y1 + 30

# Ball 클래스 생성하기
ball = Ball(court, x1, y1, x2, y2)

# Racket 클래스 생성하기 - 빨간색
red_racket = Racket(court, 60, 180, "red_racket.png")
# Racket 클래스 생성하기 - 초록색
green_racket = Racket(court, 680, 180, "green_racket.png")            

# 캔버스에 점수 표시하기
court.draw_score(red_score, green_score)

# 게임 진행 함수 호출하기
play_game()

# 키보드 이벤트 처리하기
win.bind("<w>", red_racket.move_up)
win.bind("<s>", red_racket.move_down)
win.bind("<Up>", green_racket.move_up)
win.bind("<Down>", green_racket.move_down)
win.bind("<space>", replay)

win.mainloop()    

