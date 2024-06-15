##def get_sum(n) :
##    s = 0
##    for i in range(1, n+1) :
##        s += i
##    return s
##
##n = int(input())
##print("1부터 %d까지의 합은 %d입니다." % (n, get_sum(n)))
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##def get_sum(a,b) :
##    s = 0
##    for i in range(a,b+1) :
##        s += i
##    return s
##        
##    
##
##
##a = int(input())
##b = int(input())
##print(f"{a}부터 {b}까지의 합은 {get_sum(a,b)}입니다.")
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##def area(n) :
##    return 3.14 *n**2
##    
##
##n = int(input())
##print(area(n))
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##def number(n) :
##    if n % 2 == 0 :
##        return"even"
##    else :
##        return"odd"
##    
##
##
##
##n = int(input())
##print(number(n))
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##def get_sum(n) :
##    s = 0
##    for i in range(n) :
##        s += int(input())
##    return s
##
##n = int(input("Enter integer n :  "))
##
##print(f"sum : {get_sum(n)}")
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##def get_max(n) :
##    max = 0 
##    for i in range(n) :
##        a = int(input())
##
##        if a > max :
##            max = a
##
##    return max      
##        
##    
##        
##
##
##n = int(input("Enter integer n : "))
##print("max value : %d" %get_max(n))
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##def rect(w, h) :
##    return w * h
##
##def tri(w,h) :
##    return w * h / 2
##
##def circle(r) :
##    return r ** 2 * 3.14
##
##print("Choose a shape : ")
##print("1. Rectangle", "2. Triangle", "3. Circle", sep = '\n')
##n = int(input())
##
##if n == 1 :
##    w = int(input("width : "))
##    h = int(input("height : "))
##    area = rect(w,h)
##
##elif n == 2 :
##    w = int(input("width : "))
##    h = int(input("height : "))
##    area = tri(w,h)
##
##elif n == 3 :
##    r = int(input("radius : "))
##    area = circle(r)
##
##print(area)
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
def Login(id, password) :
    if id == Cube and password == 1234 :
        return 1
    elif id == Cube and password != 1234 :
        return 2
    elif id != Cube and password == 1234 :
        return 3
    elif id != Cube and password != 1234 :
        return 4
    


id = input("ID : ")
password = int(input("PW : "))



