##from tkinter import *
##from Ball import *
##from court import *
##
##class Racket :
##
##    def __init__ (self, court, x, y, img, w = 53, h = 121) :
##        self.canvas = court.canvas
##
##        self.img = PhotoImage(file = img)
##        self.racket = self.canvas.create_image(x,y, img = self.img)
##
##        self.x = x
##        self.y = y
##
##        self.x_start = x
##        self.y_start = y
##
##
##        self.width = w
##        self.height = h
##        self.speed = 25
##
##    def start_position(self) :
##        self.x = self.x_start
##        self.y = self.y_start
##        self.canvas.coords(self.racket, self.x, self.y)
##
##    def move_up(self, event) :
##        self.y -= self.speed
##        self.canvas.coords(self.racket,self.x,self.y)
##
##    def move_down(self, event) :
##        self.y += self.speed
##        self.canvas.coords(self.racket,self.x,self.y)
##
##    def dectect_collision(self,ball) :
##
##        left, top = self.x, self.y
##        right, bottom = left + self.width , top + self.height
##
##        if ball.x2 > top and ball.y1 < bottom and ball.x2 > left and ball.x1 < right :
##            if left < ball.x2 and (ball.y2 > top or ball.y1 < bottom) :
##                ball.x1 -= randint(0, 10)
##                ball.x_dist *= -1
##
##            if right > ball.x1 and (bottom > ball.y1 or top < ball.y2) :
##                ball.x1 += randint(0, 10)
##

from tkinter import *
from Ball import *
from court import *

class Racket :

    def __init__ (self, court, x, y, img, w = 53, h = 121) :
        # court 객체의 캔버스 저장하기
        self.canvas = court.canvas
	
	# 라켓 이미지 생성하기
        self.img = PhotoImage(file = img)
        self.racket = self.canvas.create_image(x, y, image = self.img)

	# 라켓의 시작 좌표 초기화하기
        self.x = x
        self.y = y

	# 라켓의 시작 좌표 보관하기
        self.x_start = x
        self.y_start = y

        # 라켓의 가로, 세로 길이 초기화하기
        self.width = w
        self.height = h
        self.speed = 25



    # 라켓 위치 처음으로 초기화 메소드
    def start_position(self) :
        self.x = self.x_start
        self.y = self.y_start
        self.canvas.coords(self.racket, self.x, self.y)

    # 라켓 위로 이동 메소드
    def move_up(self, event) :      
        self.y -= self.speed
        self.canvas.coords(self.racket, self.x, self.y)

    # 라켓 아래로 이동 메소드
    def move_down(self, event) :
        self.y += self.speed
        self.canvas.coords(self.racket, self.x, self.y)

    # 충돌 감지 메소드
    def dectect_collision(self, ball) :

        # 라켓 변수 초기화하기 
        left, top = self.x, self.y
        right, bottom = left + self.width, top + self.height

        # 충돌 감지하기
        if ball.y2 > top and ball.y1 < bottom and ball.x2 > left and ball.x1 < right :
            # 라켓의 오른쪽에 충돌하면 랜덤 각도로 공을 쳐내기
            if left < ball.x2 and (ball.y2 > top or ball.y1 < bottom) :
                # 튀는 각도 랜덤
                ball.x1 -= randint(0, 10)
                # 공 왼쪽으로 이동
                ball.x_dist *= -1

            # 라켓의 왼쪽에 충돌하면 랜덤 각도로 공을 쳐내기
            if right > ball.x1 and (bottom > ball.y1 or top < ball.y2) :
                # 튀는 각도 랜덤
                ball.x1 += randint(0, 10)












