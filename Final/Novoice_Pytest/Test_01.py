str1 = "This is my Automation Code"
d1 = {}
count = 0
def countChar(a):
    str = a.lower()

    if len(a) == 1:
        print("Value of", a, ": 1")
        return 1
    for i in a:
        if i == " ":
            continue
        if i in d1:
            d1[i] += 1
        else:
            d1[i] = 1
    print(d1)
    return

m1 = countChar("This is my Automation Code")


str2 = "Hello world"
l1 = str2.split(" ")
d2 = {}
for i in l1:
    if i in d2:
        d2[i] += 1
    else:
        d2[i] = 1
print(d2)

str3 = "Hello World"
d3 = {}
def countChars(a):
    if len(a) == 1:
        print("Value of a",":1")
    for i in a:
        if i == " ":
            continue
        if i in d3:
            d3[i] += 1
        else:     
            d3[i] = 1
    print(d3)
m2 = countChars(str3)

l22 = [1,1,2,2,2,2,3,3,3,4,5,5,6,7,7,8]

def removeDup(a):
   i = 0
   while i < len(a):
      j = i + 1
      while j < len(a):
         if a[i] == a[j]:
            del a[j]
         else:
            j += 1
      i += 1
   print(a)
removeDup(l22)

i=0
while i< len(l22):
    j= i+1
    while j<len(l22):
        if l22[i]==l22[j]:
            del l22[j]
        else:
            j += 1
    i += 1
print(l22)

str4 = "My name is kamesh i am a yoga teacher"
d11={}
if len(str4) == 1:
    print("Value of str4",":1")
for i in str4:
    if i == " ":
        continue
    if i in d11:
        d11[i] += 1
    else:
        d11[i] = 1

print(d11)

#number = [64, 25, 12, 22, 11, 1, 2, 44, 3, 122, 23, 34]
string1 = "amuls"
list1=[]
list1[:0]=string1
print(list1)
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]>list1[j]:
            list1[i],list1[j] = list1[j],list1[i]
print(list1)
number = ['a','m','u','b','i']

for i in range(len(number)):
    for j in range(i + 1, len(number)):

        if number[i] > number[j]:
            number[i], number[j] = number[j], number[i]

print(number)

num = int(input("Enter number of rows:"))
for i in range(num+1,1,-1):
    for j in range(1,i):
        print(j,end="")
    print()