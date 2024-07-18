"""
*
* *
* * *
"""
#We can also enter * or 1 or any alphabet in the place of "*"
num = int(input("Enter a num"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
"""
print * in odd rows
*
***
*****
"""
# for i in range(1,num+1):
#     if i%2 != 0:
#         for j in range(1,i+1):
#             print("*", end="")
#     print()
k=1
for i in range(1,num+1):
    for j in range(1,k+1):
        print("*",end="")
    k=k+2
    print()
"""
inverted right angle triangle
"""
for i in range(num,0,-1):
    for j in range(0,i):
        print("*",end="")
    print()
"""
1 
2 3 
4 5 6 
7 8 9 10
"""
M=1
for i in range(1,num+1):
    for j in range(1,i+1):
        print(M,end=" ")
        M = M+1
    print()

"""
p
py
pyt
pyth
pytho
python
"""
string = input("Enter a string")
length = len(string)
for i in range(length):
    for j in range(i+1):
        print(string[j],end="")
    print()
"""
pyramid
"""
num = int(input("Enter the number of rows"))
for i in range(0,num):
    for j in range(num-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()
