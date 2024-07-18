import math

num = 5
while num>0:
    num -= 1
    if num == 3:
        continue
    else:
        print(num)

num = 5
while num>0:
    num -= 1
    if num == 3:
        continue
    elif num == 1:
        break
    else:
        print(num)
num1 = 0
while num1<=5:
    num1 += 1
    if num1 ==3:
        continue
    else:
        print(num1)

for char in "amuls":
    if char == 'u':
        continue
    else:
        print(char)

for char in 'amuls':
    if char == 'l':
        break
    else:
        print(char)
#All operations of list
fruits = ['apple',"banana"]
fruits[1] = 'grape'
fruits.insert(1,'orange')
print(fruits)
fruits.append('straberry')
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
fruits.append(['banana','guava'])
fruits.extend(['muskmelon','watermelon'])
print(fruits)
del fruits[4]
print(fruits)
print(len(fruits))
print(fruits.index('grape'))
tuple = (1,2)
tuple1 = (3,4)
tuple = tuple+tuple1
print(tuple)
print(tuple+tuple1)
print(fruits)
lis2 = fruits
fruits[2] = 'dragonFruit'
print(fruits)
print(lis2)
list22 = list(fruits)
fruits[3] = 'grape'
print(fruits)
print(list22)
name = "kaamesh"
list1 = [1,2,3,4,56]
tuple1 = (10,2.3,4,5)
#Updating global variable
var = 10
def func1():
    global var
    var1 = 0
    var += 1
    print(var,"Global var is updated")
    print(f"global var is updated {var} {var1}")
    print("global var {1} {0}".format(var,var1))
func1()
#*args and **kwargs when we don't know how many parameters or keywords we need to pass
def funct2(*args):
    for num in args:
        print(num)
funct2(2,3,4)
def funct3(name,**kwargs):
    print(name)
    print(kwargs)
    for i,j in kwargs.items():
        print(i,j)
funct3(name='I kaamesh',age=20,mobile=9036992088,city = 'hyd')
#Capitalize will capitalize 1st letter in given str
str1 = "string in python"
print(str1.capitalize())
#endswith
print(str1.endswith("python"))
print(str1.startswith("string"))
list12 = str1.split(" ")
print(list12)
print(str1.title()) #String In Python
print(str1.swapcase()) #STRING IN PYTHON
# dict
emplyoee_emails = {"kaamesh":"kaamesh.test@test.com","Yoga":"Yoga@test.com","Krishiv":"Krishiv@test.com"}
print(emplyoee_emails["Yoga"])
print(emplyoee_emails.keys())
print(emplyoee_emails.values())
info = dict(emplyoee_emails)
print(info)
del info['Yoga']
print(info)
#Weekly Temp using list
day = 'sat'#input("Select a day sun,mon,tue,wed,thu,fri,sat")
daily_temp = [20,30,40,50,60,70,55]
if day == 'sun':
    day = 'Sunday'
    temp = daily_temp[0]
    print(f"You have selected {day} and the temp is {temp}")
elif day == 'mon':
    day = 'Monday'
    temp = daily_temp[1]
    print(f"You have selected {day} and the temp is {temp}")
elif day == 'tue':
    day = 'Tuesday'
    temp = daily_temp[2]
    print(f"You have selected {day} and the temp is {temp}")
elif day == 'wed':
    day = 'Wednesday'
    temp = daily_temp[3]
    print(f"You have selected {day} and the temp is {temp}")
elif day == 'thu':
    day = 'Thursday'
    temp = daily_temp[4]
    print(f"You have selected {day} and the temp is {temp}")
elif day == 'fri':
    day = 'Friday'
    temp = daily_temp[5]
    print(f"You have selected {day} and the temp is {temp}")
elif day == 'sat':
    day = 'Saturday'
    temp = daily_temp[6]
    print(f"You have selected {day} and the temp is {temp}")
else:
    print("please enter a valid day")
# daily temp using dict
days ={'sun':'sunday','mon':'Monday',"tue":"Tuesday","wed":"Wednesday","thu":"Thursday","fri":"Friday","sat":"saturday"}
temp = {'sun':40,'mon':45,"tue":48,"wed":49,"thu":50,"fri":45,"sat":55}
day = 'sat'#input("select a day mon,tue,wed,thu,fri,sat,sun")
print(f"you have selected {days[day]} and temp is {temp[day]}")
#list of tuples as dict
d = dict([(1,'one'),(2,"two"),(3,"Three")])
print(d)
# concate 2 lists
list1 = [1,2,3,4]
list2 = ["apple","banana","grape","orange"]
my_dict = {}
for i in range(len(list1)):
    my_dict[list1[i]] = list2[i]
print(my_dict)
print(my_dict.get(1))
#print(my_dict[5]) KeyError: 5
print(my_dict.get(5))
#update
my_dict[4] = "papaya"
my_dict[5] = 'orange'
print(my_dict)
#from keys dict.fromkeys(iterable,value)
list22 = [1,2,3,4]
print(dict.fromkeys(list22))
print(dict.fromkeys(list22,10))
print(dict.fromkeys(range(10,14),20))
#setdefault() it will give the value if the key is present if the key is not present it will add the key
#in the place of value it will add none
print(my_dict.setdefault(5))
print(my_dict.setdefault(6))
print(my_dict)
#update() is nothing but concatination
dict1 = {1:'a',2:"b",3:'c'}
dict2 = {4:'d',5:'e'}
dict1.update(dict2)
print(dict1)
list23 = [6,'f']
dict1.update([list23])
print(dict1)
dict1.update(y=3,x=4,z=5)
print(dict1)
del dict1[6]
print(dict1.pop(3))
print(dict1)
#try except
num = 5
try:
    result = math.factorial(5)
    print(result)
except:
    print("Factorial of negative num cannot be generated")
#raise value error
try:
    if num<=0:
        raise ValueError("That is not a positive number")
except ValueError as error:
    print(error)
#finally
try:
    result = math.factorial(4)
    print(result)
except:
    print("Negative number cannot be com")

class person:
    def __init__(self,name):
        self.name = name
    def display(self):
        print("hello",self.name)
p = person(name)
p.display()
#class variable and instance variable
class student:
    clg = "Yoga"
    def __init__(self,rollnum,name):
        self.name = name
        self.rollnum = rollnum
    def display(self):
        print("Student name:",self.name)
        print("student rollnum:",self.rollnum)
        print("student college",self.clg,student.clg)

std = student("kaamesh",1234)
#inherictance
class Company():
    def Wishes(self):
        print("Welcome to nexTurn")
class Employee(Company):
    def info(self):
        print("Welcome to testing team")
Emp = Employee()
Emp.Wishes()
Emp.info()
# MultiLevel and multiple inherictance
class Person:
    def __init__(self,name):
        self.name = name
    def info(self):
        print("Hello", name)
class Employee(Person):
    def __init__(self, companyName, name):
        super().__init__(name)
        self.companyName = companyName
    def display(self):
        print("Welcome to ",self.companyName)
class Programmer(Employee):
    def __init__(self, team, companyName,name):
        super().__init__(companyName,name)
        self.team = team
    def show(self):
        print("Welcome to", self.team)
pmg = Programmer("Testing","NexTurn","Kaamesh")
pmg.info()
pmg.display()
pmg.show()
# Mutiple
print("Multiple"*20)
class College:
    def __init__(self,collegeName):
        self.collegeName = collegeName
    def info(self):
        print("Welcome to",)
class Department:
    def __init__(self,department):
        self.department = department
    def display(self):
        print("Welcome to ",self.department)
class Student(Department,College):
    def __init__(self, classroomName,department):
        super().__init__(department)
        self.classroomName = classroomName
    def classroom(self):
        print("Welcome to", self.classroomName)
stu = Student("Csc","csit")
stu.info()
stu.display()
stu.classroom()
# method overloading
class Honda:
    def twoWheeler(self):
        print("Welcome to honda 2 wheeler non gear segments")
class Hero(Honda):
    def twoWheeler(self):
        print("Welcome to hero 2 wheeler gear segemnts")
bike = Hero()
bike.twoWheeler()
#encapsulation on methods
class car:
    def __init__(self):
        self.__updatesoftware()
    def drive(self):
        print(" I am driving nexon")
    def __updatesoftware(self):
        print("Software has been updated")
c1 = car()
c1.drive()
#encapsulation on variables
class blackcar:
    __maxspeed = 0
    __name = ""
    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Test"
    def drive(self):
        print("Driving")
        print(self.__maxspeed)
    def setspeed(self,speed):
        self.__maxspeed = speed
        print(self.__maxspeed)
    def setyourspeed(self):
        print(self.__maxspeed)

redcar = blackcar()
redcar.drive()
redcar.setspeed(100)
redcar.drive()
redcar.setyourspeed()
#polymorphism
class Honda:
    def twoWheeler(self):
        print("We have hornet in gear segment")
class Hero:
    def twoWheeler(self):
        print("We have splendor in gear segment")
def bike(company):
    company.twoWheeler()

honda1 = Honda()
hero = Hero()
bike(hero)
bike(honda1)
# read a file
file = open("test.txt")
print(file.read())
file.close()