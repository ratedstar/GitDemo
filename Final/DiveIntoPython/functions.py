# def print_pattern():
#     sys = input("Enter any symbol")
#     for num in range(1,6):
#         print(sys*num)
# print_pattern()
#
# def print_pattern1(sys):
#     for num in range(1,6):
#         print(sys*num)
# ch = input("Enter a symbol")
# print_pattern1(ch)
# # 1+1/2+1/3+1/4.....1/n
# limit = int(input("Enter a number"))
# s = sum([1/n for n in range(1,limit+1)])
# print(s)
#
# def sum_series(num):
#     s = sum([1/n for n in range(1,num+1) ])
#     print(s)
# num = int(input("Enter a number"))
# sum_series(num)

#WAF a takes 2 nums and returns sum of num b/w 2 nos
def sum_range(start,end):
    s = sum([n for n in range(start,end+1)])
    return s
c=sum_range(10,15)
print(c)

def sum_range1(start,end):
    s = 0
    for num in range(start,end+1):
        s += num
    return s
ans = sum_range1(10,15) + sum_range1(10,15)
print(ans)
def return_value(num):
    return("even" if num%2==0 else "odd")
print(return_value(41))

def CtoF(C):
    F = 9*C/5+32
    return F
print(CtoF(30))
# find the largest of three numbers
def largest(n1,n2,n3):
    if n1>=n2 and n1>=n3:
        print(n1,"Is greater")
        return n1
    elif n2>=n1 and n2>=n3:
        print(n2,"Is Greater")
        return n2
    else:
        print(n3,"Is Greater")
        return n3
largest(11,11,13)
# min value
def find_min_max(l):
    return(min(l), max(l))
v = [1,2,3,-1]
print(find_min_max(v))
x,y = find_min_max(v)
print(x)
print(y)
# string list to int list
s = input("Enter some numbers")
l = s.split(' ')
l = [int(val) for val in l]
print(l)
# func ()
def realfunction():
    print("I m a real function")
print('1')
r2 = realfunction
print(2)
r2()
print(3)
r1=realfunction()
print('4')
r1()


# calculator with 4 operations
def mul(n1,n2):
    return n1*n2
def sum(n1,n2):
    return n1+n2
def sub(n1,n2):
    return(n1-n2)
def div(n1,n2):
    return n1/n2
# n1 = int(input("enter a number"))
# n2 = int(input("enter second number"))
# choice = input("Select any character *,/,+,-")
choice={'+':sum,'-':sub,'*':mul,"/":div}

if choice =='*':
    print(mul(n1,n2))
elif choice =="/":
    print(div(n1,n2))
elif choice == '+':
    print(n1+n2)
elif choice == '-':
    print(n1-n2)
else:
    print("Enter a valid choice")

func = choice['+']
res = func(5,6)
