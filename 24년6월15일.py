##def warning() :
##    for _ in range(3) :
##        print("Fire!")
##warning()
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##def two_times() :
##              for i in range(1,10) :
##                  print("2 * %d = %d" % (i, 2 * i ) , end = ' ')
##two_times()
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##from random import *
##def random_number() :
##    num = random() + 10
##    return num
##print(random_number())
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##a = 0
##def f() :
##    global a
##    global b
##    print(a)
##    a = 10
##    b = 20
##f()
##print(a)
##print(b)
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##def A() :
##    print(1)
##    r = B()
##    print(r)
##def B() :
##    print(2)
##    return 3
##A()
##print(4)
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##def f(n) :
##    print(n)
##    if n > 1 :
##        f(n-1)
##f(3)
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##def factorial(n) :
##    if n == 1 :
##        return 1
##    else :
##        return n * factorial(n-1)
##fac = factorial(4)
##print("4! = ", fac)
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##def judge(n) :
##    if n > 0 :
##        print("plus")
##    elif n < 0 :
##        print("minus")
##    else :
##        print("zero")
##n = int(input())
##judge(n)
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##def season(n) :
##    if 2<n<6 :
##        print("spring")
##    elif 5<n<9 :
##        print("summer")
##    elif 8<n<12 :
##        print("fall")
##    elif n == 12 or n == 1 or n == 2 :
##        print("winter")
##
##n = int(input())
##season(n)
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##from random import *
##
##def lotto () :
##    lot = []
##
##    for i in range(6) :
##        lot.append(randint(1,45))
##
##    lot.sort()
##    print(lot)
##
##lotto()
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##from random import *
##
##def lotto () :
##    lot = set()
##    while len(lot) < 6 :
##        lot.add(randint(1,45))
##    lot = list(lot)
##    lot.sort()
##    print(lot)
##
##lotto()
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##def times_table(a,b) :
##    if a > b :
##        temp = a
##        a = b
##        b = temp
##
##
##
##    for i in range(a, b+1) :
##        print(" == %d Times == "%i)
##        for j in range(1,10) :
##            print("%d * %d = %d"%(i,j,i*j))
##
##n = input(). split()
##a = int(n[0])
##b = int(n[1])
##times_table(a,b)
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##def func_abs(n) :
##    if n < 0 :
##        print(n+n*-2)
##    elif n>0 :
##        print(n)
##    elif n == 0 :
##        print(0)
##        
## 
##
##
##n = int(input())
##func_abs(n)
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
def f(n):
    for i in range(1, n+1) :
        print(n)
        for j in range(1, n+1) :
            print("%3d" %(i*j),end = ' ')
            
        




n = int(input("숫자 : "))
f(n)

    
            
              
