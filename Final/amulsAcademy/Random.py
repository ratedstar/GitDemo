# initializing dictionary
test_dict = {"Gfg": ["ab", "cd", "ef"],
             "Best": ["gh", "ij"], "is": ["kl"]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))
print(test_dict)

# using a for loop to iterate over the dictionary keys and values
for key, value in test_dict.items():
    # using a nested for loop to iterate over the list values and convert them to uppercase
    for i in range(len(value)):
        value[i] = value[i].upper()

# printing result
print("The dictionary after conversion " + str(test_dict))

# append in list
def function(n,list1=[]):
    list1.append(list1.append(n))
    return list1

for i in range(4):
    list2 = function(i)
print(list2)


#Enumerate
marks = [12,23,45,67,98,0,45,90]
for index, mark in enumerate(marks):
    print(index, mark)
    if index == 4:
        print("Thats awesome")
for index, mark in enumerate(marks,start=1):
    print(index, mark)

#Lambda function
sum = lambda x,y : x+y
print(sum(2,3))
# map function is used apply a function to all the elements of the sequence
a= [1,2,3,4]
b = [1,2,3,4]
def square(x):
    return x*x
print(list(map(square,a)))

print(list(map(lambda x:x*x,a)))
print(list(map(lambda x,y:x+y,a,b)))

#filter function will filter the unwanted elements
print(list(filter(lambda x:x%2==0,range(1,11))))

#reduce will reduce the iterables to single element using some functions
import functools
a= [2,3,4,5]
print(functools.reduce(lambda x,y:x+y,a))


class A:
    def display(self):
        print("This is from class A")
class B:
    def display(self):
        print("This is from class B")
b1 = B()
b1.display()