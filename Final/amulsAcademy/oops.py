# import math
# num = int(input("Enter a number "))
# # fact = math.factorial(num)
# # print(fact)
# #our pgm takes only +ve numbers so use exceptional handling
# try:
#     fact1 = math.factorial(num)
#     print(fact1)
# except ValueError:
#     print("This is value error")
# finally:
#     print("GoodBye")
# #lets check for the raise value exception
# try:
#     num1 = int(input("Enter a positive number"))
#     if num1>=0:
#         print("That is not a positive number")
# except ValueError as error:
#     print(error)
# class n object
# class and instance variable
class student:
    clg = "xyz"
    def __init__(self,rollnum,name):
        self.name = name
        self.rollnum = rollnum
    def display(self):
        print("Student name is",self.name)
        print(f"roll num is {self.rollnum}")
        print(f"college name is {student.clg}")

s1 = student(112,"ramesh")
s1.display()
s2 = student(113,"king")
s2.display()
# inheritance
class animal:
    def eating(self):
        print("eating")

class dog(animal):
    def bark(self):
        print("can bark")
d1 = dog()
d1.eating()
d1.bark()

class animal1:
    print("Welcome")
    def __init__(self,name):
        self.name = name
class dog1(animal1):
    print("Good bye")
    def display1(self):
        print(f"we have a {self.name}")

d2 = dog1("babydog")
d2.display1()
#Multilevel inheritance
class person:
    def display(self):
        print("This is person class")
class employer(person):
    def printing(self):
        print("This is from employee class")
class programmer(employer):
    def show(self):
        print("This from show class")

p1 = programmer()
p1.display()
p1.printing()
p1.show()
# multiple level inheritance
class land:
    def print(self):
        print("This is from land class")
class water:
    def show(self):
        print("This is from water class")
class frog(land,water):
    pass
f1 = frog()
f1.show()
f1.print()
# method overriding: changing the implementation of derived class
class A:
    def disp(self):
        print("This is from class A")
class B(A):
    def disp(self):
        print("This is from class B")

a1 = B()
a1.disp()
# Encapsulation for methods
class encaps:
    def __init__(self):
        self.__updatesoftware()
    def drive(self):
        print("driving")
    def __updatesoftware(self):
        print("this a private method")
e1 = encaps()
e1.drive()
# Encapsulation using variables private variables can only be modified inside the class but not outside the class
class car:
    __maxspeed =0
    __name =""
    def __init__ (self):
        self.__maxspeed = 200
        self.__name = "blackcar"
    def drive(self):
        print("driving")
        print(self.__maxspeed)
    def setspeed(self,speed):
        self.__maxspeed = speed
        print(self.__maxspeed)

c1 = car()
c1.drive()
c1.setspeed(100)
# polymorphsim
class dog:
    def sound(self):
        print("Bow Bow")
class cat:
    def sound(self):
        print("Meow Meow")
def makesound(animaltype):
    animaltype.sound()

d1 = dog()
c1= cat()
makesound(c1)
makesound(d1)