### Leap Year or not
# year = input("Enter an year").strip()
# print(len(year))
# print(year.isdigit())
# if year.isdigit() and len(year) == 4:
#     year = int(year)
#     if year%100 == 0 and year% 400 ==0:
#         print("Year is leap year")
#     elif year%100!=0 and year%4 ==0:
#         print("leap year")
#     else:
#         print("Not a leap year")
# else:
#     print("Enter a valid year ")

s= "welcome"
revstr = ''
for i in s:
    revstr = i+revstr
print(revstr)

for i in s:
    print(i)

class MyClass():
    def m1(self):
        print("hello")
    @staticmethod
    def m2(self,num):
        print("Hi")
MyClass.m2(10,20)

a,b =10,20
class MyVar():
    a,b = 30,40
    def m3(self):
        a,b = 50,60
        print(globals()['a'] + globals()['b'])

# to print constructor values we use __str__ constructor
class Emp:
    def __init__(self,empid,empname,empsal):
        self.empid = empid
        self.empname = empname
        self.empsal = empsal

    def __str__(self):
        return self.empname

mc = Emp(123,"john",5000)
print(mc)

class A:
    x,y = 4,5
    def m1(self):
        print(self.x+self.y)
class B(A):
    a,b = 6,7
    def m2(self):
        print(self.x+self.b)

bobj = B()
bobj.m2()
# to invoke parent class method we use super() keyword
class A:
    def m1(self):
        print("This is a method from class A")
class B(A):
    def m1(self):
        print("THis is a method from class B")
        super().m1()
bob1 = B()
bob1.m1()

#to over ride variables n access parent class variable
class Parent:
    name = "Sumit"
class Child(Parent):
    name = "John"
    def test(self):
        print(super().name)

ch = Child()
print(ch.name)
ch.test()