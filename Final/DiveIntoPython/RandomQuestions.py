# # An year is leap year or not
# #year = int(input("Enter an year:"))
# year = 2000
# if year%100 == 0 and year%400 == 0:
#     print("It a leap year:", year)
# elif year%100 !=0 and year %4 ==0:
#     print("Its a leap year", year)
# else:
#     print("Not a leap year")
#
# #While
# counter = 1
# while counter <=10:
#     print(counter, end=' ')
#     counter += 1
# # enter a string indexing using while loop
# s = input("Enter a string")
# index = 0
# while index < len(s):
#     print(s[index])
#     index += 1
#
# # little modified version for the above
# s= input("Enter a string")
# index = 0
# while index < len(s):
#     if s[index].isalpha():
#         print(s[index],end='')
#     else:
#         print("$",end='')
#     index += 1
# #While loop counter
# counter = 10
# while counter >1:
#     print(counter,end='')
#     counter -= 1
# # natural numbers n*(n+1)/2
#
# s = input("Enter a string")
# index = 0
# while index < len(s):
#     if s[index].isalpha():
#         print(s[index],end='')
#     else:
#         print("$",end='')
#     index += 1

"""
Print statement if we add end='' it will not go to next line, By default cursor will got to next line'\n'
if we want a seperater b/w. We need to write like this sep='', end = ''
"""
print(1, 2, 3, end=' '); print(1,2)   #1 2 3 1 2
print(1,2,3, end= '-' ); print(1,2)   #1 2 3-1 2
print(1,2,3, sep='-', end=' '); print(1,2)   # 1-2-3 1 2

"""
String char count
"""
# s = input("Enter a string")
# index = 0
# count = 0
# while index < len(s):
#     if s[index].isalpha():
#         print(s[index], end=' ')
#         count += 1
#     index += 1
# print('\n' ,count)

"""
calculator with 2 nos
"""
# repeat = 'Y'
# while repeat !='N':
#     n1 = int(input("Enter a number"))
#     n2 = int(input("Enter a 2nd number"))
#     opt = input("Select any operation '*,+,-,/'")
#     if opt == "*":
#         print(n1 * n2)
#     elif opt == "+":
#         print(n1 + n2)
#     elif opt == '-':
#         print(n1 - n2)
#     elif opt == '/':
#         print(n1 / n2)
#     else:
#         print("Invalid")
#     repeat = input("Enter Y/N if you want to repeat")
# import sys
# while True:
#     n1 = int(input("Enter a number"))
#     n2 = int(input("Enter 2nd number"))
#     opt = input("Select any operation *,/,+,-")
#     if opt == "*":
#         print(n1*n2)
#     elif opt == '/':
#         print(n1/n2)
#     elif opt == '+':
#         print(n1+n2)
#     elif opt == '-':
#         print(n1-n2)
#     repeat = input("Enter your choice y/n:")
#     if repeat == 'n' or repeat == 'N':
#         sys.exit()
# s = input("Enter a string")
# for ch in s:
#     print(ch)
# for num in range(1,5):
#     print(num)
#
# numa = int(input("Enter a number"))
# for num in range(2,numa+1,2):
#     print(num)

listexap = []
for num in range(1,11):
    listexap.append(num)
print(listexap)

listcompre = [num for num in range(1,10)]
print(listcompre)
sumof = sum([num for num in range(1,5)])
print(sumof)
evenexe = [num for num in range(1,11) if num%2==0]
print(evenexe)
"""
1
11
111
1111
11111
"""
for line in range(1,6):
    for sys in range(1,line+1):
        print(1,end='')
    print()

for line in range(1,6):
    print('1'*line)
"""
p
pa
pat
patt
patte
patter
pattern
"""
s = "pattern"
for chr in range(len(s)):
    for ch in range(0,chr+1):
        print(s[ch], end='')
    print()
print("*"*30)
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=' ')
    print()
for slice in range(0,len(s)):
    print(s[:slice+1])

for i in range(5):
    if i == 3:
        continue
    print(i)
"""
List comprehension
"""
l = [num*num for num in range(1,5)]
print(l)
l2 = [1 for num in range(0,5)]
print(l2)
l3 = [num for num in range(1,10) if num%2==0]
print(l3)
# 10 random numbers in a list
import random
l=[]
for counter in range(1,10):
    l.append(random.randrange(100))
print(l)
# even or odd
# num = int(input("Enter a number"))
# res = ['even','odd']
# print(res[num%2])
l = [20,2,32,4,64,56]
l2 =[elemt for elemt in l if elemt%2 ==0]
print(l2)
"""
extract capital words 
"""
# s= input("Enter a string")
# l_words = s.split(' ')
# capital_words = []
# for word in l_words:
#     if word.isupper():
#         capital_words.append(word)
# print(capital_words)
#
# capital_words1 = [word for word in s.split() if word.isupper()]
# print(capital_words1)
# WAP to join a list and a tuple
# l1 = [1,4,7,8]
# t1 = (3,6,9,10)
# ls = [n for n in l1 ]
# ls.extend(t1)
# ls.sort()
# print(ls)
# sl = l1+list(t1)
# sl.sort(reverse=True)
# print(sl)
# print("*"*20)
# # guess the o/p
# l = list(range(3,-4,1))
# print(len(l))
# l= list(range(2,10,3))
# print(len(l),max(l),min(l))
# l= list(range(3,-4,-1))
# print(l)  # [3, 2, 1, 0, -1, -2, -3]
# print(len(l), sum(l))
# l=[0,90,7,-10]
# l.sort(reverse=True)
# print(l[0],l[len(l)-1])
# # create a tuple from -1000 to 0 step size 5 reverse and store it in another variable RT
# tuple1 = tuple(range(-1000,0,5))
# RT = list(tuple1)
# RT.sort(reverse=True)
# print(RT)
# RT = tuple(RT)
# print(RT)
# # (20,15,10,5)
# tupleR = tuple(range(20,0,-5))
# print(tupleR)
# # WAP a input to count vowles in a string "a,e,i,o,u"
# sample_string = input("Enter a string")
# vowels_dict = dict(a=0,e=0,i=0,o=0,u=0)
# characters= [n for n in sample_string]
# for ch in characters:
#     if ch.lower() in vowels_dict:
#             vowels_dict[ch.lower()] += 1
# print(vowels_dict)
# d2 = dict(a=0,e=0,i=0,o=0,u=0)
# sample = input("Enter any string")
# for c in sample:
#     if c.lower() in d2:
#         d2[c.lower()] += 1
# print(d2)
#
# d3 = dict([(c,0) for c in 'aeiou'])
# print(d3)
# # count number of spaces in a string
# spacestring = input("Enter a string")
# count = 0
# for c in spacestring:
#     if c ==' ':
#         count += 1
# print(count)
# print(sum([1 for c in spacestring if c==' ']))
# if else in list comprehension

l1 = [num*num if num%2==0 else num*2 for num in range(0,5)]
print(l1)
l2 = [num*num if num%2==0 else num*2 for num in range(0,5)]
print(l2)
# loop num1,num2
l4=[]
for num1 in range(1,6):
    for num2 in range(10,16):
        l4.append((num1,num2))
    print(l4)
l2 = [(num1,num2) for num1 in range(1,6) for num2 in range(11,16)]
print(l2)
l3 = [(num1,num2) for num1 in range(1,6) for num2 in range(1,6) if num1!=num2]
print(l3)

# [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
l5 = [[num for num in range(1,6)] for counter in range(1,6)]
l33 = []
for counter in range(1,6):
    for num in range(1,6):
        l33.append([num])
print("This is l33............................",[l33])


print(l5)
#[[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]]
l6 =[[num for num in range(1,counter+1)] for counter in range(1,6)]
print(l6)
# take range from input
l7 = [num**2 for num in range(1,int(input("enter a number"))+1)]
print(l7)

"""
*
**
***
****
*****
"""
for counter in range(1,6):
    print("*"*counter)
print(("*"*counter for counter in range(1,5)))
