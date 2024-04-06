##num = input('주민 번호 : ')
##z = num[2]
##a = num[3]
##b = num[4]
##c = num[5]
##print(f'생일 : {z}{a}월 {b}{c}일')
##--------------------------------------------------
##print("A{:-7d}30{:6s}A".format(2023, "KITPA"))
##-------------------------------------------------
##t1 = (1, )
##t2 = (4, 5, 6)
##print(t1 + t2)
##print(t2 * 2)
##print(t2[0])
##print(t2[1:3])
##del t2[0]
##-------------------------------------------------
##a = "Carpe Diem!"
##b = [1, 2, 3, 4, 5, 6]
##print(len(a))
##print(len(b))
##-------------------------------------------------
##d = {'name' : 'Jane', 'name' : 'Mason', 'age' : 12, 'number' : 123456 }
##print(d)
##print(d['age'])
##-------------------------------------------------
##d = {'a' : 1, 'b' : 2}
##d['c'] = 3
##del d['a']
##print(d)

##d = {'a' : 2, 'b' : 3}
##d['c'] = 4
##del d ['b']
##print(d)
##-------------------------------------------------
##s1 = set([1,2,3,4,5,6])
##s2 = set([4,5,6,7,8,9])
##print(s1 - s2)
##print(s1 & s2)
##print (s1 | s2)
##-------------------------------------------------
##a = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4}
##print(a.keys())
##print(a.values())
##print(a.items())
##a.clear()
##print(a)
##-------------------------------------------------
##a = {'name' : 'Minsu', 'address' : 'Seoul', 'phone' : '010-1234-1234'}
##print(a.keys())
##-------------------------------------------------
##a = set([1, 2, 3])
##a.add(4)
##print(a)
##a.update('abc')
##print(a)
##a.remove('c')
##print(a)
##-------------------------------------------------
##n = int(input('몇 단? : '))
##a = 1
##print('%d * %d = %d' % (n, a, n*a))
##a += 1
##print('%d * %d = %d' % (n, a, n*a))
##a += 1
##print('%d * %d = %d' % (n, a, n*a))
##a += 1
##print('%d * %d = %d' % (n, a, n*a))
##a += 1
##print('%d * %d = %d' % (n, a, n*a))
##a += 1
##print('%d * %d = %d' % (n, a, n*a))
##a += 1
##print('%d * %d = %d' % (n, a, n*a))
##a += 1
##print('%d * %d = %d' % (n, a, n*a))
##a += 1
##print('%d * %d = %d' % (n, a, n*a))
##-------------------------------------------------
##import turtle
##
##t = turtle.Turtle()
##
##t.fillcolor('red')
##t.begin_fill()
##t.right(60)
##t.circle(25, 180)
##t.right(120)
##t.circle(25, 180)
##t.right(120)
##t.circle(25, 180)
##t.right(120)
##t.circle(25, 180)
##t.right(120)
##t.circle(25, 180)
##t.right(120)
##t.circle(25, 180)
##t.right(120)
##t.circle(25,180)
##t.end_fill()
##
##t.fillcolor('yellow')
##t.begin_fill()
##t.right(60)
##t.circle(50)
##t.end_fill()
##
##turtle.done()
##-------------------------------------------------
##import turtle
##
##t = turtle.Turtle()
##
##s = turtle.textinput('즐거운 씨큐브 코딩', '당신의 이름은?')
##
##t.write(f"{s}님 반갑습니다")
##
##turtle.done()
##-------------------------------------------------
##t1 = (1, )
##t2 = (2,3,4)
##print(t1 + t2)
##-------------------------------------------------
##import turtle
##
##t = turtle.Turtle(shape = "turtle")
##
##s = "즐거운 씨큐브 코딩"
##n = turtle.numinput(s, "앞으로 얼마나 이동할까요?")
##t.forward(n)
##
##ang = turtle.numinput(s, "오른쪽으로 얼마나 회전할까요? : ", default = 0, minval = 0, maxval = 360)
##t.right(ang)
##
##turtle.done()
##-------------------------------------------------
##list1 = ['a' , 'b' , 'c', 'd', 'e', 'a']
##print(set(list1))
##-------------------------------------------------
##d = {'a' : 90, 'b' : 85, 'c' : 95}
##d['e'] = 70
##d['a'] = 100
##print(d)
#-------------------------------------------------
##d = {'plus' : ['더하기', '장점'], 'minus' : ['빼기', '적자'], 'multiply' : ['곱하다', '다양하게'], 'division' : ['나누기, 분열']}
##n = input("단어 : ")
##print(d[n])

##print(d.keys())
##d['square'] = '제곱'
##print(d.items())

##n = input(" 단어 : ")
##del d[n]
##print(d)
#-------------------------------------------------
##import turtle
##from random import*
##t = turtle.Turtle()
##color = ['red' , 'yellow', 'pink', 'blue', 'orange']
##r = randint(0,5)
##t.fillcolor(color[r])
##t.begin_fill()







                                     






