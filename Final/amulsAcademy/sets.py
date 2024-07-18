# set is a mutuable data type with non duplicate unordered values
fruits ={'apple','banana'}
fruits.add('grapes')
fruits.add(12)
print(fruits)
#frozen set this is a immutable set, we cannot add or delete anything syn frozenset([])
animal = frozenset(['tiger','lion'])
#we cannot add an element in frozenset
#print(animal.add('monkey'))

# lets add duplicate values in set
num = {1,2,2,3,3,4.5,5,6,6,6}
print(num)
# creating an empty set syn set()
emptyset = set()
# copyimg a set
num1 = set(num)
print(num1)
#operations in set
#membership
print(6 in num)
print(7 in num)
# add if we want to add any element set.add()
num.add(10)
print(num)
#REMOVE set.remove
print(num)
# union add 2 sets
print(num|num1)
#clear
num.clear()
print(num)
#Intersection it will give common values in 2 or more set
A = {1,2,3,4}
B = {1,5,7,3}
print(A&B)
# difference it gives element belongs to A but not B elements which are not present in another set will be given
print(A-B)
print(B-A)
#SYM difference it will give values which are not commom in A & B
print(A^B)
#len
print(len(A))
#copy
C = A.copy()
print(C)
