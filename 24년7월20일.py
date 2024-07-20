##class Car :
##    model = "BMW"
##    color = "white"
##
##bmw = Car()
##benz = Car()
##
##benz.model = "Benz"
##benz.color = "black"
##
##print(bmw.model)
##print(bmw.color)
##print(benz.model)
##print(benz.color)
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##class Car :
##    model = "BMW"
##    color = "white"
##
##    def speedChange(self, v) :
##        self.speed = v
##
##bmw = Car()
##bmw.speedChange(20)
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##class Car :
##    count = 0
##    speed = 0
##    def speedChange(self, v) :
##        Car.count += 1
##        self.speed = v
##
##bmw = Car()
##benz = Car()
##
##bmw.speedChange(100)
##print("bmw speed :", bmw.speed)
##print("number of speedChange :", Car.count)
##
##benz.speedChange(120)
##print("Benz speed :", benz.speed)
##print("number of speedChange :", Car.count)
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##class Car :
##    def __init__(self, model, color):
##         self.model = model
##         self.color = color
##
##
##    def info(self) :
##         print("Model : ", self.model, ", Color :" , self.color)
##
##benz= Car("Benz", "black")
##bmw = Car("BMW", "white")
##bmw.info()
##benz.info()
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##class Car :
##    def __init__(self, model, color) :
##        self.model = model
##        self.color = color
##
##    def info(self):
##        print("Model : ", self.model, ", Color :", self.color)
##
##class CarDrive(Car) :
##    def speedChange(self, v) :
##        self.speed = v
##        print("speedChange :", self.speed)
##
##
##bmw = CarDrive("BMW", "white")
##bmw.info()
##bmw.speedChange(100)
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##class Car :
##    def __init__(self, model, color) :
##        self.model = model
##        self.color = color
##
##    def info(self) :
##        print("Model :", self.model, ", Color :", self.color)
##
##
##class CarDrive(Car):
##    def info(self) :
##        print("The model of this car is %s." % self.model)
##        print("The color is %s." %self.color)
##
##    def speedChange(self,v) :
##        self.speed = v
##        print("speedChange :", self.speed)
##
##bmw = CarDrive("BMW" , "white")
##bmw.info()
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
class Character :
    def __init__(self, name, weapon) :
        self.name = name
        self.weapon = weapon

    def intro(self) :
        print("Name :", self.name)
        print("Weapon :", self.weapon)

class Action(Character) :
    step = 0

    def move_forward(self, n) :
        self.step += n
        print("Current location is %d." % self.step)

    def move_backward(self, n) :
        self.step -= n
        print("Current location is %d." % self.step)

    def turn_right(self) :
        print("Turn right.")

    def turn_left(self) :
        print("Turn left.")

lugo = Action("Lugo", "gun")
lugo.intro()
lugo.move_forward(10)
lugo.move_backward(3)
lugo.turn_right()
lugo.turn_left()
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
