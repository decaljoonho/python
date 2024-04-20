##from random import*
##import turtle
##
##a = turtle.Turtle()
##a.penup()
##a.goto(300,-200)
##a.pendown()
##a.fillcolor("skyblue")
##a.begin_fill()
##a.goto(300,-100)
##a.goto(200,-100)
##a.goto(200,-200)
##a.goto(300,-200)
##a.end_fill()
##a.penup()
##a.goto(200,-100)
##a.pendown()
##a.fillcolor("blue")
##a.begin_fill()
##a.goto(250,0)
##a.goto(300,-100)
##a.end_fill()
##a.penup()
##a.goto(-400,-200)
##a.write("0")
##a.pendown()
##a.goto(-100,-200)
##a.write("50")
##a.goto(200,-200)
##a.write("100")
##a.penup()
##a.goto(-400,-200)
##a.color("pink")
##line = turtle.Turtle()
##t = turtle.Turtle(shape = "turtle")
##g = turtle.Turtle()
##g.write("씨큐브 코딩의 타자 게임", True, font = ("Arial", 20, "bold"))
##t.penup()
##t.goto(-400,-200)
##t.color("pink")
##
##f = ['apple','banana','strawberry','watermelon','mandarin','peach','grapes','orange','pear','kiwi']
##score = 0
##n = randint(5,10)
##for i in range(n) :
##   s = choice(f)
##   word = s
##   word = turtle.textinput("f", '%s(%d/%d)' % (s, i+1, n))
##   if word == s :
##    score += 1
##rate = score / n * 100
##
##g.penup()
##g.goto(0,-50)
##g.pendown()
##g.write(f"{score}번 성공!", True, font = ("Arial", 15, "bold"))
##g.penup()
##g.goto(0,-100)
##g.pendown()
##g.write(f"정확도 : {rate}", True, font = ("Arial", 15, "bold"))
##
##distance = t.distance(line)/100 * rate
##t.speed(1)
##t.forward(distance)
##
##if rate == 100 :
## t.write("집에 데려다줘서 고마워!!", False, "center", font = ("Arial", 15, "bold"))
## t.left(60)
## t.right(60)
## t.left(60)
## t.right(60)
##elif 100 > rate >= 80 :
## t.write("집이 코앞인데!! 한 번만 더 시도해줘!! ", False, "center", font = ("Arial", 15, "normal"))
##elif 80 > rate >=50 :
## t.write("집에 가고 싶어!! ㅠ0ㅠ ", False, "center", font = ("Arial", 15, "normal"))
##else :
## t.color('black')
## t.right(60)
## t.write("거북이가 쓰러졌어요 ㅠ_ㅠ", False, "center", font = ("Arial", 15, "normal"))
##
##turtle.done()
   
##--------------------------------------------------------------------
##from random import*
##q = ['월','화','수','목','금','토','일']
##a = randint(0,6)
##print(q[a])
##--------------------------------------------------------------------
##from random import*
##a = ['월','화','수','수','수','수','수','수','수','수','수','수','수','수','수','수','수','수','수','수','수','수','수','수','수','수','목','금']
##print(choice([True,False]))
##print(choice(a))
##--------------------------------------------------------------------
##from random import*
##a = [1,2,3,4,5]
##print(choices(a, [1,1,10,1,1],k = 3))
##--------------------------------------------------------------------
##from random import*
##q = [0,1,2,3,4,5]
##s = choice(q)
##if s == 0 :
##    print("Loss!")
##else :
##    print(f"No. {s} Spot!")
##--------------------------------------------------------------------
##from random import*
##a = ['legendary','mythic','epic','rare','common','poop']
##s = 5000
##q = choices(a, [1,2,3,4,10,20])
##p = input("뽑기 하는덴 1000코인입니다 할껀가요 : ")
##if p == '네' :
## s -= 1000
## print(f"남은 코인 : {s}")
## print(q)



