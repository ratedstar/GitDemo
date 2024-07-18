
# year = int(input("Enter any year"))
# if year%4==0:
#     if year%100!=0:
#         if year%400==0:
#             print("leap year")
#         else:
#             print("Not leap year")
#     else:
#         print("Not leap year")
# else:
#     print("Not a leap year")
#
# if((year%400==0)or(year%100!=0 and year%4==0)):
#     print("Given year is leap year")
# else:
#     print("Not a leap year")
#
# #Roller coaster ride with photo
# print("Welcome to roller coaster ride")
# height= int(input("Enter your height"))
# if height >120:
#     print("you are eligible for the ride")
#     age = int(input("Enter your age"))
#     if age <=12:
#         bill = 6
#         print(f"You have to pay {bill} with out photo")
#     elif age <= 18:
#         bill = 7
#         print(f"You have to pay {bill} with out photo")
#     else:
#         bill = 12
#     with_photo = input("If you want photo select Y or N")
#     if with_photo=='Y':
#         bill = bill+3
#     print(f"Your total amount is {bill}")
# else:
#     print("Sorry you are not eligible for the ride")
#Pizza order
# size = input("what is the size of the pizza you like 'S'or 'M'or'L'")
# add_pepperoni = input("Do you want pepperoni 'Y'or 'N'")
# extra_cheese = input("Do you want extra cheese 'Y' or 'N'")
# if size == 'S':
#     if add_pepperoni=='Y' and extra_cheese=='Y':
#         bill = 15+4
#     elif add_pepperoni == 'Y':
#         bill = 15+2
#     elif extra_cheese == 'Y':
#         bill = 15+2
#
#     print(f"Your small pizza bill is ${bill} ")
# if size == 'M':
#     if add_pepperoni == 'Y':
#         bill = 20+2
#     elif extra_cheese == 'Y':
#         bill = 20+3
# if size == 'L':
#     if add_pepperoni == 'Y':
#         bill = 25+2
#     elif extra_cheese == 'Y':
#         bill = 25+3
# else:
#     print("Please select proper input")
# bill =0
# if size =='S':
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
# if extra_cheese == 'Y':
#     bill += 1
# print(f"Your final pizza bill is ${bill}")
#Love calculator in this exe we are going to take 2 name in that we have to check for TRUE and LOVE
# characters an combine for exe TRUE t occurs once + U occures 2 + e 2 total 5 similallry count LOVE 3
#its 53
# name1 = input("Enter first name ")
# name2 = input("Enter 2nd name")
# name1 = name1.lower()
# name2 = name2.lower()
# print(name1)
# print(name2)
# #instead of this we can add both and the check for the true n love
# T = name1.count('t')+ name2.count('t')
# R = name1.count('r')+ name2.count('r')
# U = name1.count('u')+ name2.count('u')
# E = name1.count('e')+ name2.count('e')
# total_TRUE = T+R+U+E
# print(f"T occurs {T} times")
# print(f"R occurs {R} times")
# print(f"U occurs {U} times")
# print(f"E occurs {E} times")
# print(f'Total of true is {total_TRUE}')
# L = name1.count('l')+name2.count('l')
# O = name1.count('o')+name2.count('o')
# V = name1.count('v')+name2.count('v')
# E = name1.count('e')+name2.count('e')
# total_LOVE = L+O+V+E
# print(f"L occurs {L} times")
# print(f"O occurs {O} times")
# print(f"V occurs {V} times")
# print(f"E occurs {E} times")
# print(f"Total Love count is {total_LOVE}")
# a = str(total_TRUE)+str(total_LOVE)
# a= int(a)
# if a<10 or a>90:
#     print(f"Your score is {a} you can go for coke and mentos")
# elif a>=40 and a<=50:
#     print(f"Your score is {a} you are okay together")
# else:
#     print(f"Your score is {a}")

#Treasure hunt pgm
# print("Welcome to the treasure island.")
# print("Your mission is to find the treasure")
# way = input("You\'re at crossword.Please where you want to go 'left' or 'right'.\n").lower()
# if way == 'left':
#     whattodo = input("You\'ve come to a lake.Please select 'swim'or'wait'.\n").lower()
#     if whattodo == 'swim':
#         print("GameOver")
#     elif whattodo== 'wait':
#         whichdoor = input("You\'ve come to a lake. please select color 'red'or 'blue'or'yellow'.\n").lower()
#         if whichdoor == 'red':
#             print("GameOver")
#         elif whichdoor == 'blue':
#             print("GameOver")
#         elif whichdoor == 'yellow':
#             print("You win")
#         else:
#             print("GameOver")
#     else:
#         print("GameOver")
# else:
#     print("You fell into a hole. GameOver")

# import random
#
# random_int = random.randint(0,1)
# print(random_int)
# if random_int==1:
#     print("You got tails")
# else:
#     print("You got heads")
# # random bill payer group of friends went to a hotel
# names_string = input("Give me list or group of names seperated by commas\n")
# name = names_string.split(',')
# n= len(name)
# billpayer = random.randint(0,n-1)
# # instead of this we can use choice also to randomize a list
# billpayer1 = random.choice(name)
# print(f"bill payer is {billpayer1}")
# paybill = name[billpayer]
# print(f"bill payer is {paybill}")
# Matrix give position and value
# column = int(input("Enter the column number"))
# row = int(input("Enter the row number"))
# value = input("Enter the value")
# row1 = ["","",""]
# row2 = ["","",""]
# row3 = ["","",""]
# matrix = [row1,row2,row3]
# matrix[row-1][column-1]=value

# position = input("Enter a two digit number")
# value = 'X'
# vert=int(position[0])
# hori=int(position[1])
# row1 =[" "," "," "]
# row2 =[" "," "," "]
# row3 =[" "," "," "]
# map = [row1,row2,row3]
# map[hori-1][vert-1] = value
# print(f"{row1}\n{row2}\n{row3}\n")

# Students average height by adding all heights / number of students
# students_height = input("Students height seperated by ").split(',')
# for n in range(0, len(students_height)):
#     students_height[n]=int(students_height[n])
# print(students_height)
# count = 0
# total_height=0
# for height in students_height:
#     count += 1
#     total_height = int(height)+total_height
# avg_height = round(total_height/count)
# print(count)
# print(total_height)
# print(f"The avg height is {avg_height}")

# Max score without using max func
# marks = input("Enter marks of class").split(',')
# temp = 0
# for i in marks:
#     if int(i) > temp:
#         temp = int(i)
# print(f"Heighst score is {temp}")
#
# students_score = input("Enter students scores").split(',')
# for n in range(0,len(students_score)):
#     students_score[n] = int(students_score[n])

#adding all numbers from 1 to 100
total =0
for number in range(1,101):
    total += number
print(total)
# adding even number from 1 to 100
total1 = 0
for n in range(2,101,2):
    total1 += n
print(total1)
# 2nd method
total2 = 0
for n1 in range(1,101):
    if n1%2==0:
        total2 += n1
print(total2)

# fizz buzz pgm
for number in range(1,101):
    if number%3==0 and number%5 ==0:
        print("FizzBuzz")
    elif number%3 ==0:
        print("fizz")
    elif number%5 ==0:
        print("buzz")
    else:
        print(number)
# password generator pgm
