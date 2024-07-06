##f = open("example.txt", "w")
##for i in range(1, 4) :
##    f.write("Line %d\n" % i)
##f.close()
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##f = open("example.txt", "a")
##alphabet = ['A' , 'B', 'C', 'D', 'E']
##for c in alphabet :
##    f.write(c)
##f.close()
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##f = open("example.txt", "r")
##data = f.read()
##print(data)
##f.close()
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##f = open("example.txt", "r")
##while True :
##    line = f.readline()
##    if not line : break
##    print(line, end = '')
##f.close()
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##f = open("example.txt", "r")
##data = f.readlines()
##for line in data :
##    print(line, end = '')
##f.close()
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##f = open("example.txt", "r")
##while True :
##    print(f.tell(), end = ' ')
##    line = f.readline()
##    print(line.strip())
##    if not line : break
##f.seek(26)
##print("포인터의 위치 : %d(%s)" % (f.tell(), f.read()[0]))
##f.close()
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##f = open("profile.txt", "w")
##name = input("Name : ")
##age = input("Age : ")
##f.write("Name : %s\n" %name)
##f.write("age : %s\n" %age)
##f.close()
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##f = open("profile.txt", "a")
##School = input("School : ")
##f.write("School : %s\n" % School)
##f.close()
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##f = open("profile.txt", "r")
##data= f.read()
##print(data)
##f.close()
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##f = open("profile.txt", "r")
##while True :
##    line = f.readline()
##    if not line : break
##    print(line, end = '')
##f.close()
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##f = open("profile.txt", "r")
##f.seek(28)
##data = f.readline()
##print(data)
##f.close()
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##f = open("alphabet.txt", "w")
##f.write("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
##f.close()
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##f = open("alphabet.txt", "r")
##ind = int(input("index : "))
##f.seek(ind)
##data = f.readline()
##print(data)
##f.close()
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##f = open("fruit.txt", "r")
##data = f.readlines()
##for line in data :
##    if len(line) >= 11 :
##        print(line)
##f.close()     
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
def read_file(file_name) :
    f = open(file_name, "r")
    data = f.read()
    print(data)
    
##def write_file(file_name , mode) :


file_name = input("File name : ")
mode = input("FIle mode(r/w/a) : ")

if mode == "r" :
    read_file(file_name)
else :
    write_file(file_name, mode)
