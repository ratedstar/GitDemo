num ={1:'one',2:'two',3:'three'}
numbers = dict(num)
print(numbers)
num[1] ='apple'
print(num)

print(len(num))
del num[2]
print(num)
print(2 in num)
print(1 in num)
#List VS Dict
# daily_temp = [49,35,36.5,38.9,34.3,40,43]
# day = input("Enter any day from 'sun','mon','tue','wed','thu','fri','sat'")
#
# if day == 'sun':
#     dayname= 'sunday'
#     temp = daily_temp[0]
# elif day =='mon':
#     dayname = 'monday'
#     temp = daily_temp[1]
# elif day == 'tue':
#     dayname ='tuesday'
#     temp = daily_temp[2]
# elif day == 'wed':
#     dayname = 'wednesday'
#     temp = daily_temp[3]
# elif day == 'thu':
#     dayname = 'thursday'
#     temp = daily_temp[4]
# elif day == 'fri':
#     dayname = 'friday'
#     temp = daily_temp[5]
# elif day == 'sat':
#     dayname = 'saturday'
#     temp = daily_temp[6]
# else:
#     print("Please select correct day")
# print(f"You have selected {dayname} and {temp}")
#
# # Using dictionary
# temp = {'sun':49,'mon':48,'tue':45,'wed':50,'thu':54,'fri':45,'sat':50}
# day_name = {'sun':'sunday','mon':'monday','tue':'tuesday','wed':'wednesday','thu':'thursday','fri':'friday','sat':'saturday'}
# day = input("enter any day from 'sun','mon','tue','wed','thu','fri','sat'")
# print(temp[day])
# print(day_name[day])
# print("you have selected",day_name[day],"temp",temp[day])
# print(f"you  {day_name[day]}and temp{temp[day]}")
# print("You have selected",day_name[day], "and temp is", temp[day])

# value can be any type string integer list tuple #but key should be immutable type int float string or tuple
# Ways to create a dictionary
#1
my_dict = {1:'apple',2:'banana',3:'papaya'}
#2 from empty dict
my_dict2 = {}
my_dict2[1] ='bike'
my_dict2[2] = 'car'
my_dict2[3] = 'yoga'
print(my_dict2)
# 3 using dictionary constructor and list of tuples
d = dict([(1,'bike'),(2,'car'),(3,'youtube')])
print(d)
#4 using two parallel
a =[1,2,3,4]
b= ['apple','ball','cat','king']
my_dict3 = {}
for i in range(len(a)):
    my_dict3[a[i]] = b[i]
print(my_dict3[4])
print(my_dict3.get(0))
print(my_dict3.get(1))
print(my_dict3.keys())
print(my_dict3.values())
my_dict3[5] = "Yoga"
print(my_dict3)
#from Keys we can create dict using tuple list range or any iterables fromkeys(iterables , value) value is optional
list1=[1,2,3,4]
print(dict.fromkeys(list1))
print({}.fromkeys(range(1,7),10))
#set default chk for the key if present gives value if not it will add to the dict
#setdefault(key,value)
student = {'john':20,"kamesh":30,"king":23}
print(student.setdefault("yoga"))
print(student.setdefault("bike",26))
print(student)
#update() dict.update(dict2)
dict1 = {'king':20,"yoga":23,'kamesh':29}
dict2 = {'apple':2}
dict1.update(dict2)
print(dict1)
print(dict2)
dict3 = {1:'a',2:'b'}
list4 = [3,'c']
dict3.update(y=3,z=2,x=8)
print(dict3)
dict43 = {2:'apple',3:'king',5:'yoga',6:"bike"}
del dict43[2]
print(dict43)
dict43.pop(3)
print(dict43)
dict43.clear()
print(dict43)
del dict43
print(dict43)