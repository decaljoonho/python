##import sys
##import pygame
##from pygame.locals import *
##
##pygame.init()
##SCREEN = pygame.display.set_mode((200, 200))
##CLOCK = pygame.time.Clock()
##
##img = pygame.image.load("man.png")
##img_size = img.get_size()
##print(img_size)
##
##while True :
##
##    SCREEN.fill((255,255,255))
##
##    for event in pygame.event.get() :
##        if event.type == QUIT :
##            pygame.quit()
##            sys.exit()
##
##    SCREEN.blit(img,  (25, 40))
##
##    pygame.display.update()
##    CLOCK.tick(1)
##-----------------------------------------------------------
##import sys
##import pygame
##from pygame.locals import *
##
##pygame.init()
##SCREEN = pygame.display.set_mode((300, 300))
##CLOCK = pygame.time.Clock()
##sysfont = pygame.font.SysFont(None, 30)
##txt = "Wait..."
##txt2 = " Key Down! "
##
##while True :
##    SCREEN.fill((255,255,255))
##    for event in pygame.event.get() :
##        if event.type == QUIT :
##            pygame.quit()
##            sys.exit()
##
##    key_event = pygame.key.get_pressed()
##    if key_event[pygame.K_LEFT]:
##        txt = "Left" + txt2
##    if key_event[pygame.K_RIGHT] :
##        txt = "Right" + txt2
##    if key_event[pygame.K_UP]:
##        txt = "Up" + txt2
##    if key_event[pygame.K_DOWN]:
##        txt = "Down" + txt2
##    if key_event[pygame.K_ESCAPE] :
##        pygame.quit()
##        sys.exit()
##
##    msg = sysfont.render(txt, True, (0,0,0))
##    SCREEN.blit(msg, (50,100))
##    pygame.display.update()
##    CLOCK.tick(60)
##-----------------------------------------------------------
import sys
import pygame
from pygame.locals import *
import random

pygame.init()
SCREEN = pygame.display.set_mode((600,600))
CLOCK = pygame.time.Clock()
sysfont = pygame.font.SysFont(None, 72)

light_img = pygame.image.load("light.png")
man_img = pygame.image.load("man.png")
m_x, m_y = 250, 480

l_size = light_img.get_size()
m_size = man_img.get_size()

game_over = False




l_x = []
l_y = []

cnt = 0

while True :
    if game_over :
        break
    SCREEN.fill((0, 0, 0))
    for event in pygame.event.get() :
        if event.type == QUIT :
            pygame.quit()
            sys.exit()

    for i in range(len(l_x)) :
        if  l_x[i] + l_size[0] >= m_x and m_x + m_size[0] >= l_x[i] :
            if l_y[i] + l_size[1] >= m_y :
                msg = sysfont.render("Game over!", True, (255,0,0))
                SCREEN.blit(msg, (160, 250))
                game_over = True

    key_event = pygame.key.get_pressed()
    if key_event[pygame.K_LEFT] :
        if m_x > 0 :
            m_x -= 5
    if key_event[pygame.K_RIGHT] :
        if m_x < 500 :
            m_x += 5



    cnt += 1
    if cnt >= 20 :
        cnt = 0
        l_x.append(random.randint(0, 600))
        l_y.append(0)
    for i in range(len(l_x)) :
        l_y[i] += 5
        SCREEN.blit(light_img,(l_x[i],l_y[i]))




        if l_y[i] >= 550 :
          l_x.remove(l_x[i])
          l_y.remove(l_y[i])
          break



    SCREEN.blit(man_img,(m_x,m_y))


    pygame.display.update()
    CLOCK.tick(60)
        
