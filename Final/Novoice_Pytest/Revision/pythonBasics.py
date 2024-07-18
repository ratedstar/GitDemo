#for loop in python
for char in "python":
    print("Char is:",char)
for num in [10,20,30,40]:
    if num>=25:
        print(num,"greater than 25")
    else:
        print(num,"less than 25")

#While Loop and this is also called definite loop because we know how many times loop will repeated
#by default in python print has /n it means next line if we declare end=' ' it will not go to next line
#everything will be printed in same line with a space
count = 1
while count<=5:
    print(count,end=' ')
    count += 1
print("goodBye")
print("*"*25)

#Break and continue
count = 1
while count<=5:
    if count ==3:
        break
    else:
        print(count)
    count += 1
print("Thank you")
#break using for loop
for char in "amuls":
    if char =="u":
        break
    else:
        print(char)
print("Thank you")
#continue
for char in "amuls":
    if char =='u':
        continue
    else:
        print(char,end=" ")
print("Thank you")
#continue using while
var= 10
while var >0:
    var = var-1
    if var == 3:
        continue
    print(var)
print("Thank you")
#List are mutuable we can alter it or change the list or delete it or add or replace the list
#its linear data structure elements are arranged in linear order, ZERO based indexing
animal = ["dog","cat","monkey"]
print(animal[0])
#nested list
number = [[10,20],30,40]
print(number[0][0])
#replace in list
list1 = [10,20,40,5.7]
list1[2] = 3.7
print(list1)
#insert when we want to insert at a specific position
list1.insert(2,"hello")
print(list1)
#sort
animal = ["dog","cat","monkey","Ant"]
# we cannot do print(animal.sort()) it will give none
#first we need to sort it and then print it
animal.sort()
print(animal)
#delete element in a list or delete list
list1 = [10,20,40,5.7]
list2 = [10,20,30,40]
del list1[3]
print(list1)
del list2
#append insert the element at the end
animal.append("donkey")
print(animal)
#reverse a list
animal.reverse()
print(animal)
#All operations of list in one example
fruits = ["Apple","Banana"]
fruits[1]="grape"
fruits.insert(1,"Orange")
fruits.append("grape")
del fruits[2]
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
#Tuples
animal =("dog","cat","monkey")
print(animal[0])
tuple1 = ((10,2,3),(3,5,4))
print(tuple1[0][0])
"""
Sequence Operations
Length, slice, index, concatenation, max value
select, count, membership, min value, sum
"""
name ="Kamesh"
list1 = [1,2,3,4,5,6]
tuple = (10,2.3,4,5)
#length
print(len(name))
print(len(list1))
print(len(tuple))
#select
print(name[0])
print(list1[1])
print(tuple[2])
#slicing
print(name[1:4])
print(list1[1:])
print(tuple[:2])
#count
print(name.count('m'))
print(list1.count(5))
print(tuple.count(10))
#indexing
print(list1.index(5))
print(tuple.index(10))
#membership
print('m' in name)
print('m' not in name)
#concatenation
s = ' hai'
print(name+s)
list2 = [2,'hello']
print(list1+list2)
tuple2 = ("king",2.3)
print("*"*20)
print(tuple+tuple2)
#min value
print(min(name))
print(min(list1))
print(min(tuple))
#max value
print(max(name))
print(max(list1))
print(max(tuple))
#sum
print(sum(list1))
print(sum(tuple))
#assignment in list
list2 = [2,22,33,44]
list3 = list2
print(list3)
list2[0] = "apple"
print(list2)
print(list3)
#copying in list
list4 = list(list2)
print(list4)
list2[0] = 33
print(list2)
print(list4)
# range function
# In range (1,11) 1 is included and 11 is excluded
for x in range(1,11):
    print(x)
print(10*'*')
#updating global varable, we need to use global keyword to update a global variable
var = 10
def func1():
    global var
    var += 1
    print(var," global var is updated")
func1()
# When we don't know how many parameters we need in a function we use variable length
def func2(*mylist):
    for num in mylist:
        print(num)
func2(10,20,30,40)
func2(101,201)
########Strings#############
print(10*"*","Strings",10*"*")
#Capitalize() will capitalize 1st letter of the given string
str1 = "strings in python"
print(str1.capitalize())
#count() will count the number of repeated words
str2 = "johny johny yes papa johny yes papa"
print(str2.count("johny"))
#ends with will very string ends
str1 = "google.com"
print(str1.endswith(".com"))
# find will give the index of the alphabet or word
str22 = "amuals academy"
print(str22.find("y"))
print(str22.find("academy"))
#len will give the length of the string
print(len(str22))
#split will split the words of string into list
newstr = str22.split()
print(newstr)
#title() it will capitalize the first letter of words of a string "This Is Python"
print(str22.title())
# lower() everything in lower
str1 = "amuls academy"
print(str1.lower())
#upper() everything in upper
print(str1.upper())
#islower() will check everything is in lower or not
print(str1.islower())
#isupper() will check everything is in upper or not
print(str1.isupper())
#swapcase() lowercase letters to uppercase n uppercase letters to lowercase letters
str23 = "hello Welcome to Python course"
print(str23.swapcase())    # o/p HELLO wELCOME TO pYTHON COURSE
#replace a word or letter with other word or letter
str24 = "hello welocome to kamesh"
str25 = "amulas"
print(str24.replace("kamesh","yoga")) #o/p hello welocome to yoga
print(str25.replace("a","s")) #o/p smulss
# isdigit it will check weather a string has all digits
str25 = "1234567"
print(str25.isdigit())
# isalpha it will check weather a string has all alphabets
str25 = "kamesh"
print(str25.isalpha())
#strip it will strip left and right side not in the middle
str1 = "aaaaaaakaaaaaaameshaaaaaaa"
print(str1.strip('a')) #o/p kaaaaaaamesh
# lstrip will strip left side rstrip will strip right side
print(str1.lstrip('a'))   #o/p kaaaaaaameshaaaaaaa
print(str1.rstrip('a'))   #o/p aaaaaaakaaaaaaamesh
print(10*"*","DICTIONARIES",10*"*")
# Dictinary
temp = {}
temp['sun'] = 34
temp['Mon'] = 23
temp['Tue'] = 35
print(temp)   #o/p {'sun': 34, 'Mon': 23, 'Tue': 35}
mail_address = {'amul':'amuls@gmail.com','jenni':'jenni@gmail.com'}
#to get only keys from a dictionary
print(mail_address.keys())   #o/p dict_keys(['amul', 'jenni'])
#to get only values from a given dictionary
print(mail_address.values())   #o/p dict_values(['amuls@gmail.com', 'jenni@gmail.com'])
# To access a value from a dictionary
print(mail_address['amul']) #o/p amuls@gmail.com
#Operations in dict
#copy a dict
num = {1:'one',2:'two',3:"three"}
numbers = dict(num)
print(numbers)
#length of a dict
print(len(num))
#Delete an item or value from dict
del num[2]
print(num)
#To check a value present in a dict
print(1 in num)
print(2 in num)
#List vs Dict
# select a day n it will give you temp
daily_temp = [28,29,30,32,33.5,35,34]
#day = input("Select any day sun,mon,tue,wed,thu,fri,sat")
day = 'sat'
if day =='sun':
    day = 'Sunday'
    temp = daily_temp[0]
    print("You have selected",day,temp)
elif day == 'mon':
    day = 'Monday'
    temp = daily_temp[1]
    print("You have selected", day,temp)
elif day == 'tue':
    day = 'Tuesday'
    temp = daily_temp[2]
    print("You have selected", day,temp)
elif day == 'wed':
    day = 'Wednesday'
    temp = daily_temp[3]
    print("You have selected", day,temp)
elif day == 'thu':
    day = 'Thuday'
    temp = daily_temp[4]
    print("You have selected", day,temp)
elif day == 'fri':
    day = 'Friday'
    temp = daily_temp[5]
    print("You have selected", day,temp)
elif day == 'sat':
    day = 'Satday'
    temp = daily_temp[6]
    print("You have selected", day,temp)
#dictinory selection
days = {'sun':'sunday','mon':'monday','tue':'tuesday','wed':'wednesday','thu':'thursday','fri':'friday','sat':'saturday'}
daily_temp = {'sun':34,'mon':32,'tue':31,'wed':34.5,'thu':35,'fri':36,'sat':37}
#days = input("Select any day sun,mon,tue,wed,thu,fri,sat")
day= 'sat'
print("You have selected",days[day],'n',daily_temp[day])
#Different ways for creating dictionary
#1 dict
my_dict = {1:"one",2:"Two",3:"Three"}
print(my_dict)
#2 creating empty dict filling one by one
my_dict = {}
my_dict[1]="one"
my_dict[2] = "Two"
my_dict[3] = "Three"
print(my_dict)
#dict constructor and a list of tuples
d = dict([(1,'One'),(2,"Two"),(3,"Three")])
print(d)
# from 2 parallel lists
a = [1,2,3,4]
b= ['apple','banana','grape','lemon']
my_dict ={}
for i in range(len(a)):
    my_dict[a[i]] = b[i]
print(my_dict)
# get in dict we can access any element in a dict using get()
my_dict = {1: 'apple', 2: 'banana', 3: 'grape', 4: 'lemon'}
print(my_dict.get(1))
#if we want to get any element which is not in the list we will not get an error instead we get none
print(my_dict.get(5))
# insert a value update a value
my_dict[5] = "cherry"
print(my_dict)
#update
my_dict[2] = "papaya"
print(my_dict)
#length
print(len(my_dict))
#fromkeys() using this method we can create dictionary from keys using iterables(list tuple range function or any
#itreables)
#syntax: fromkeys(iterable,value) iterable: list tuple range() value is optional
list1 = [1,2,3,4]
print(dict.fromkeys(list1))
print(dict.fromkeys(list1,10))
print({}.fromkeys(range(1,10),10))
#setdefault() if the key is present it will give the value or else it will add the key to the dictionary
# and in place of value it will add none to the dictionary
students ={'john':20,"ria":22,'yoga':23}
print(students.setdefault('john'))
print(students.setdefault('mike'))
print(students)
print(students.setdefault('john',10))
print(students.setdefault('rohi',26))
print(students)
#update() is nothing but concatination
dict1 = {1:'a',2:"b",3:'c'}
dict2 = {4:'d'}
dict1.update(dict2)
print(dict1)
list1=[5,'e']
dict1.update([list1])
print(dict1)
dict1.update(x=1,y=3,z=7)
print(dict1)
dict2 = {1:'apple'}
dict1.update(dict2)
print(dict1)
# delete or pop will also delete but it will give value of deleted key
del dict1[1]
print(dict1)
print(dict1.pop(2))
print(dict1)
# to clear a dict clear()
dict2 = {1:'apple'}
dict2.clear()
print(dict2)
#to delete a dictionary
del dict2
#print(dict2)
#Exception Handling
import math
num = 5
num1 = -5
try:
    result = math.factorial(5)
    print(result)
except:
    print("cannot compute factorial for negative numbers")
#Exception raising: programmer can raise exceptions
try:
    #num=int(input("Enter a number"))
    if num<=0:
        raise ValueError("That is not a positive number")
except ValueError as error:
    print(error)
#Exception finally
#num = int(input("Enter a number"))
try:
    result = math.factorial(4)
    print(result)
finally:
    print("goodBye")
print("################################################")
#OOPS
class person:
    def __init__(self,name):
        self.name = name
    def display(self):
        print("hello",self.name)
p = person(name)
p.display()
# Class variable and instance variable
class Student:
    clg = "Yoga"
    def __init__(self,name,rollnum):
        self.name = name
        self.rollnum = rollnum
    def display(self):
        print("student Name:",self.name)
        print("student rollnum:",self.rollnum)
        print("Student college:",Student.clg)
student1 = Student("Ramesh",123)
student1.display()

student2 = Student("Vardhan",121)
student2.display()
# instead of self we can use anything or static method
class Person:
    @staticmethod
    def display():
        print("This is a static method")
p = Person()
p.display()
Person().display()
#InHeritance
class Animal:
    def eating(self):
        print("I am eating")
class Dog(Animal):
    def barking(self):
        print("I am barking")
a = Animal()
a.eating()
D = Dog()
D.eating()
D.barking()
# 2nd example
class Animal:
    def __init__(self,name):
        self.name = name
class Dog(Animal):
    def display(self):
        print("My name is:",self.name)
dog = Dog("BabyDog")
dog.display()
#Multilevel and multiple inheritance
class person():
    def display(self):
        print("hello,this is person")
class employee(person):
    def printing(self):
        print("Hello, this is derived class employee")
class programmer(employee):
    def show(self):
        print("hello ", "This medthod is from programmer class")
p1 = programmer()
p1.display()
p1.show()
p1.printing()
#Python supports multiple inheritance
class land_animal:
    def printing(self):
        print("This animal is land living")
class water_animal():
    def display(self):
        print("THis is a water animal")
class frog(land_animal,water_animal):
    pass
f1= frog()
f1.printing()
f1.display()
# Method overriding ablity of the class to change its method implementation provided by its parent class
class A:
    def display(self):
        print("method belongs to class A")
class B(A):
    def display(self):
        print("Method belongs to class B")
b = B()
b.display()
#Encapsulation: In ops we can restrict the access to the variables and methods
#Public methods can be accessed outside the class But private methods cannot be accessed outside the class
# If we give __ before any method or variable it becomes private
class car:
    def __init__(self):
        self.__updatesoftware()
    def drive(self):
        print("driving")
    def __updatesoftware(self):
        print("Updating software")
c1 = car()
c1.drive()
"""
In the above example if we call c1.__updatesoftware(). It will give an error "car object has no attribute 
__updatesoftware"
Beacuse we cannot call __updatesoftware outside the class
"""
#Lets see this with variables
class blackcar:
    __maxspeed = 0
    __name = ""

    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"

    def drive(self):
        print("driving")
        print(self.__maxspeed)

    def setspeed(self, speed):
        self.__maxspeed = speed
        print(self.__maxspeed)

redcar = blackcar()
redcar.drive()
redcar.setspeed(100)
#Polymorphism: Is ability of an object to adapt the code to the type of data processing
class dog:
    def sound(self):
        print("Bow bow")

class cat:
    def sound(self):
        print("Meow meow")
def makesound(animaltype):
    animaltype.sound()

catobj = cat()
dogobj = dog()
makesound(catobj)
makesound(dogobj)
#SET: It is a mutable data type with non duplicated unordered values
fruits = {'apple',"banana"}
#if we want to add an item in set
fruits.add("grapes")
print(fruits)
#If we want to create an immutable set by using frozenset keyword
animal = frozenset(['lion',"monkey"])
print(animal) #o/p: frozenset({'monkey', 'lion'})
frozenset({'monkey', 'lion'})
"""if we try to add or remove any value animal.add('cat')
it gives an error as "frozenset object has no attribute add"
"""
num = {1,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,}
print(num) #o/p {1, 2, 3, 4, 5, 6}
# to create an empty set
emptyset = set()

#copy a set in another set
num1 = {1,2,3,4}
num2 = set(num1)
print(num2)
#Membership in set
set1 = {1,2,3,4,5,"hello"}
print(5 in set1)
# add in set
set1.add(6)
# remove in set
set1.remove(4)
#Union in set
set2 = {"Yoga","Kamesh",1}
list1 = [1,2]
print(set1|set2)
# clear in set
set1.clear()
print(set1) #o/p set()


# *args and **kwargs
def funct(*mylist):
    for num in mylist:
        print(num)
funct(2,3,4)
funct(2,3)

# **kwargs we are sending multiple data with the help of keywords
def person(name,**kwargs):
    print(name)
    print(kwargs)
    # if we want to loop the data then
    for i, j in kwargs.items():
        print(i,j)
person(name, age=20,city="Hyderabad",mob=998765)

# Read a text file
file = open("test.txt")
print(file.read())
file.close()
#for each line
file = open("test.txt")
print(file.readline())
file.close()
#for reading n number of characters
file = open("test.txt")
print(file.read(5))
file.close()

file = open("test.txt")
line = file.readline()
while line!="":
    print(line)
    line = file.readline()
file.close()
#Using for loop
file = open("test.txt")
for line in file.readlines():
    print(line)
file.close()
""" #Using with for writing in a file we can read also but if we don't want to write file.close() 
each and everytime we can go for with
"""
with open("test.txt",'r') as reader:
    content = reader.readlines()
    with open("test.txt",'w') as writer:
        for line in reversed(content):
            writer.write(line)

# Exceptions using raise exception or assert
Itemsincart = 0
if Itemsincart != 0:
    raise Exception("This value is not matching")

Itemsincart=1
#assert (Itemsincart==3)
#Try except this is user defined exception
try:
    with open("test123.txt", 'w') as writer:
        writer.write(line)
except:
    print("There no such file")
#If we want python exception
try:
     with open("test12345.txt", 'r') as reader:
        writer.write(line)
        raise Exception
except Exception as e:
    print(e)
#zip it will connect two components
names = ("kaamesh","Chandan","anusha","Ramesh","suresh")
companies = ("Mphasis","capgemini","optum")

zipped = list(zip(names,companies))
print(zipped)
# we can also use set here or dict
zipped1 = set(zip(names,companies))

zipped2 = dict(zip(names,companies))
print(zipped2)
print(zipped1)
for a,b in zip(names,companies):
    print(a,b)

#enumerate
letters = ["a","b","c","d"]
for index, l in enumerate(letters):
    print(l,index)
#enumerate on 2 lists
fruits = ["apple","banana","grape",""]
veggies = ["potato","onion","cabbage","zomato"]

for index ,(value1,value2) in enumerate(zip(fruits,veggies)):
    print(index,value1 , value2)
#count number of words
string = "hi hello hi hello"
words = string.split(" ")
dict1 = {}
for word in words:
    if word in dict1:
        dict1[word] += 1
    else:
        dict1[word] = 1
print(dict1)
#lambda function
#lambda x,y:x+y

a = lambda x,y:x+y
print(a(2,3))
#map function
#map(func,sequence) sequence are nothing but list, tuple n strings
a=[1,2,3,4]
def square(x):
    return x*x
l1= list(map(square,a))
print(l1)
#lambda func
l2 = list(map(lambda x:x*x,a))
print(l2)
#we can add two list we can add them
b= [1,1,1,1]
l3=list(map(lambda x,y:x+y,a,b))
print(l3)
c= (1,2,3,4)
l4=list(map(lambda x,y:x+y,b,c))
print(l4)
#filter(func,iterables)
l6 = list(filter(lambda x:x%2==0,range(1,11)))
print(l6)
#reduce func will reduce iterables to a single element
import functools
num = [1,2,3,4]
f7= functools.reduce(lambda x,y:x+y,num)
print(f7)
