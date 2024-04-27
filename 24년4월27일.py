##a = 1
##while a <= 10 :
##    print(a, end = '  ')
##    a += 1
##--------------------------------------------------------------------------
##sum = 0
##i = 1
##while i <= 100 :
##    sum += i
##    i += 1
##print(sum)
##--------------------------------------------------------------------------
##i = 0
##while i < 10 :
##     i += 1
##     if i % 2 == 0 :
##      continue
##     print(i,end = '  ')
##--------------------------------------------------------------------------
##while True :
##    ans = input("Shall we close? (y/n) ")
##    if ans == 'y' :
##        print('The end')
##        break
##--------------------------------------------------------------------------
##a = 1
##while a <= 100 :
##     print(a, end = ' ')
##     a += 1
##--------------------------------------------------------------------------
##a = int(input())
##s = 1
##k = 0
##while s <= a :
##     k += s
##     s += 1
##print(k)
##--------------------------------------------------------------------------
##i = 0
##while i < 5 :
##        i += 1
##     a = int(input("input : "))
##     if a % 5 == 0 :
##         continue
##     print(f"output : {a}")
##--------------------------------------------------------------------------
##while True :
##    a = int(input())
##    if a == 0 :
##        break
##--------------------------------------------------------------------------
##cnt = 0
##n = int(input("정수 입력 : "))
##while n > 0 :
##    cnt += 1
##    n //= 10
##print("자릿수 : %d" % cnt)
##--------------------------------------------------------------------------
##import sys
##import pygame
##from pygame.locals import*
##
##pygame.init()
##screen = pygame.display.set_mode((400, 300))
##pygame.display.set_caption("Tick Tock Timer")
##CLOCK = pygame.time.Clock()
##sysfont = pygame.font.SysFont(None, 36)
##timer = 0
##while True :
##    for event in pygame.event.get():
##        if event.type == QUIT :
##            pygame.quit()
##            sys.exit()
##        timer += 1
##        screen.fill((255, 255, 255))
##        cnt_txt = sysfont.render("Timer : %d" % timer, True, (0, 0, 0))
##        screen.blit(cnt_txt, (140, 140))
##        pygame.display.update()
##        CLOCK.tick(1)
##--------------------------------------------------------------------------
##n = 1
##while n <= 10 :
##    if n % 3 == 0 :
##        print('X', end = '  ')
##    else :
##        print(n, end = '  ')
##    n += 1
##--------------------------------------------------------------------------
##n = 1
##while n <= 20 :
##    if n %10 == 3 or n % 10 == 6 or n % 10 == 9 :
##        print('X', end = '  ')
##    else :
##        print(n, end = '  ')
##    n += 1
##--------------------------------------------------------------------------
##a = int(input("몇 단 : "))
##i = 0
##while i < 9 :
##    i += 1
##    s = a * i
##    print(f"{a} * {i} = {s}")
##--------------------------------------------------------------------------
##from random import *
##com = randint(1, 100)
##while True :
##    user = int(input())
##    if user > com :
##        print("Down")
##    elif com > user :
##        print("Up")
##    elif com == user :
##        print("Correct!")
##        break
##--------------------------------------------------------------------------
import sys
import pygame
from random import *
from pygame.locals import*

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("pygame window")
CLOCK = pygame.time.Clock()
sysfont = pygame.font.SysFont(None, 36)
timer = 0
while True :
    for event in pygame.event.get():
        if event.type == QUIT :
            pygame.quit()
            sys.exit()
        timer += 1
        screen.fill((255, 255, 255))
        cnt_txt = sysfont.render("HI!", True, (0, 0, 0))
        screen.blit(cnt_txt, (randint(0, 400), randint(0,400)))
        pygame.display.update()
        CLOCK.tick(1)
       
        
    
