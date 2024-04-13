##y = True
##print('not y = ', not y)
##------------------------------------------------------------------
##a = int(input('점수 : '))
##
##if a > 90 and a <=100 :
##      print("Pass")
##
##else :
##
##    print("Fail")
##------------------------------------------------------------------
##score = 72
##if score >= 90 :
##    print("A")
##elif score >= 60 :
##    print("B")
##else :
##    print("C")
##------------------------------------------------------------------
##x = 10
##print(x >= 0 and x <= 10)
##print(x < 0 or x > 10)
##print(not x)
##------------------------------------------------------------------
##a = int(input())
##b = int(input())
##c = int(input())
##
##print(a >= 140 and b >= 140 and c >= 140)
##------------------------------------------------------------------
##a = int(input('점수 : '))
##
##if a >= 90 :
##    print("A")
##if a >= 80 and a < 90 :
##    print("B")
##if a >= 70 and a < 80 :
##    print("C")
##if a < 70 :
##    print("F")
##------------------------------------------------------------------
##a = int(input('수 : '))
##if a % 2  == 0 :
##  print("Even")
##else :
##  print("Odd")
##------------------------------------------------------------------
##y = int(input('year : '))
##
##if y % 400 == 0 or y%4 == 0 and y%100 != 0 :
##        print('leap year')
##else :
##        print('common year')
##------------------------------------------------------------------
##a = input('성별 : ')
##if a ==  'M' :
##  print('Man')
##elif a == 'W' :
##  print('Woman')
##else :
##    print('What?')
##------------------------------------------------------------------
##a = int(input('월: '))
##if a >= 1 and a <= 6  :
##  print("first half")
##elif a >= 7 and a <= 12 :
##  print("second half")
##------------------------------------------------------------------
##a = ['Burger','Sandwitch','Hotdog','Coke','milk']
##y = int(input('번호 : '))
##if y == '1' :
## print("Burgers are not available")
##elif y == '2' or '3' :
## print("What would you like to drink")
##elif y == '4' :
## print("I like coke, too")
##elif y == '5' :
## print("Would you like hot or cold?")
##------------------------------------------------------------------
##import random
##
##com = random.randint(1, 2)
##user = int(input('odd : 1, even : 2\n'))
##
##print('COM(%d) : USER(%d)' %(com, user))
##if com == user :
##    print('Correct')
##else :
##    print('Incorrect')
##------------------------------------------------------------------
##import random
##
##com = random.randint(1, 3)
##user = int(input(' '))
##
##print("1 : 가위, 2 : 바위, 3 : 보")
##print(f'컴퓨터의 선택 : {com}')
##
##if com ==1 and user == 3 :
## print("Com Wins")
##elif com ==1 and user == 2 :
## print("User Wins")
##elif com ==1 and user == 1 :
## print("Draw")
##elif com ==2 and user == 1 :
## print("Com Wins")
##elif com == 2 and user == 3 :
## print("User Wins")
##elif com == 2 and user == 2 :
## print("Draw")
##elif com == 3 and user == 1 :
## print("User Wins")
##elif com == 3 and user == 3 :
## print("Draw")
##elif com == 3 and user == 2 :
## print("Com Wins")
##------------------------------------------------------------------
##import turtle
##
##t = turtle.Turtle(shape = "turtle")
##t.penup()
##t.setx(200)
##t.write('동', font=('Arial', 30))
##t.setx(-200)
##t.write('서', font=('Arial', 30))
##t.setx(0)
##t.sety(-200)
##t.write('남', font=('Arial', 30))
##t.sety(200)
##t.write('북', font=('Arial', 30))
##t.goto(0, 0)
##t.pendown()
##t.pencolor('blue')
##
##s = "Python turtle"
##n = turtle.textinput(s, "방향을 입력해 주세요.")
##
##if n == '동' :
## t.pendown
## t.setx(200)
## t.penup
##elif n == '서' :
##  t.pendown
##  t.setx(-200)
##  t.penup
##elif n == '남' :
##  t.pendown
##  t.sety(-200)
##  t.penup
##
##elif n == '북' :
##    t.pendown
##    t.sety(200)
##    t.penup
##------------------------------------------------------------------

        
