print(round(8/3,2))
result = 4 /2
result /= 2
print(4//2)
score = 0
height = 1.8
iswining = True

print(f"your score is {score}")
print(f"Your score is {score}, Your height is {height}, Your winning is {iswining}")

# how many days, weeks and months
# Age = int(input("Enter your Age"))
# years_left = 90-Age
# days_left = years_left*365
# weeks_left = years_left*52
# months_left = years_left*12
# print(f"You are left with {days_left} days,{weeks_left} weeks, {months_left} months")

# int("5") is 5, int(2.7) is 2, so the code becomes: a = 5 ÷ 2 which equals 2.5, which is a float.
#Tip calculator restaurant bill divided b/w friends including tip
print("Welcome to tip calculator")
Totalbill = float(input("Whats your total bill"))
perTip = int(input("What percentage of tip you like to give? 10, 12, or 15"))
NumberofPeople = int(input("How many people to split the bill"))
tip_per = perTip/100
total_tip = Totalbill*tip_per
Total = Totalbill+total_tip
bill_each = Total/NumberofPeople
final_bill = round(bill_each,2)
final_bill = "{:.2f}".format(final_bill)

# eachbill = round(((Totalbill*perTip/100)+Totalbill)/NumberofPeople,2)
# print(f"Each person should pay:{eachbill}")
# print(f"Each person should pay:{final_bill}")

# Day3 conditional statements
#Odd/Even
# number = int(input("Enter a number"))
# if number%2 == 0:
#     print("Number is even")
# else:
#     print("Number is odd")

#Rollercoster ride height and age price
height = int(input("Enter your Height"))
if height>=120:
    print("Your are eligibale fro the ride")
    age = int(input("Enter your age"))
    if age < 12:
        print("You habve to pay $5 ")
    elif age <= 20:
        print("You have to pay $10")
    elif age < 30:
        print("you've to pay $15")
    else:
        print("You have to pay $12")
else:
    print("your are not eligible for the ride")

#BMI calculator
# height = float(input("Enter your height"))
# weight = float(input("Enter your weight "))

# bmi = round(weight/height**2)
# print(bmi)
# if bmi < 18.5:
#     print(f"Your {bmi} UNDER WEIGHT")
# elif bmi > 18.5 and bmi <25:
#     print(f"You have a{bmi} NORMAL Weight")
# elif bmi >25 and bmi <30:
#     print(f"Your {bmi} over weight")
# elif bmi > 30:
#     print(f"Your{bmi} obessed")
# else:
#     print("Check your weight again")
#Leap year
# year = int(input("Enter a year"))
# if year%4 ==0:
#     print("Its divisible by 4")
# if year%400 ==0:
#     print("Leap year")
#     if year%100 ==0:
#         print("Not a leapyear")
#     else:
#         print("Leap year")
year = int(input("Enter a year"))
if year%4 ==0:
    print("Leap year")
    if year%400==0:
        print("leap year")
#for loops are better when we are iterating thru a list
#for fruit in fruits: fruits = ['apple','banana','grape'] this is difficult to do with while loop
#OR for n in range(0,6): print(n)
# while loop we don't really care what number we are in or sequence in which item thru iterating in list
# just simply we want to carry out one simple functionality many many times until some sort of condn that you set
#it will run until the particular condn switches to false
