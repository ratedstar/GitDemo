""" LIST """
a_list = ["a",'b','Yoga','MMA','Youtube']

print(a_list[-1])
"""
a_list[-n] == a_list[len(a_list)-n]
a_list[-3] == a_list[5-3] == a_list[2]
"""

"""
Slicing
"""
print(a_list[1:-1])
print(a_list[-1:1:]) #o/p will be empty because -1 to 1 it cannot go we need to mention step as -1
print(a_list[-1:1:-1])
print(a_list[0:3])
print(a_list[3:])
print(a_list[:])

"""
Adding there are 4 ways to add an item in a list
"""
b_list = ['a']
b_list = b_list + [2.3,3]
print(b_list)
b_list.append(True)
print(b_list)
b_list.extend(['four',"actor"])
print(b_list)
b_list.insert(0,'actor')
print(b_list)

"""
difference between append() and extend().
"""
c_list = ['a','b','c']
c_list.extend(['d','e','f'])
print(c_list)
print(len(c_list))
print(c_list[-1])

c_list.append(['g','h','i'])
print(c_list)
print(len(c_list))
print(c_list[-1])

"""
The extend() method takes a single argument, which is always a list, and adds each of the items of that list 
to a_list.
②	If you start with a list of three items and extend it with a list of another three items, you end up with 
a list of six items.
③	On the other hand, the append() method takes a single argument, which can be any datatype. Here, you’re 
calling the append() method with a list of three items.
④	If you start with a list of six items and append a list onto it, you end up with... a list of seven 
items. Why seven? Because the last item (which you just appended)
 is itself a list. Lists can contain any type of data, including other lists. That may be what you want, 
 or it may not. But it’s what you asked for, and it’s what you got.

"""

"""
Searching for values in a string
"""

a_list = ["a",'b','Yoga','MMA','Youtube',"a"]
print(a_list.count('a'))
print('a' in a_list)
print('c' in a_list)
print(a_list.index('Yoga'))
print(a_list.index("MMA"))
#print(a_list.index('c'))

"""
Removing items from a list
"""
a_list = ["a",'b','Yoga','MMA','Youtube',"a"]
print(a_list[1])
del a_list[1]
print(a_list)
print(a_list[1])

"""
We can also remove items by value instead.
The remove() method takes a value and removes the first occurrence of that value from the list. 
Again, all items after the deleted item will have their positional indices bumped down to “fill the gap.” 
Lists never have gaps.
"""
a_list.remove("MMA")
print(a_list)

"""
Another interesting list method is pop(). The pop() method is yet another way to remove items from a list,
but with a twist. pop() can remove only if pass an index not by value and without index it will remove last item
"""
a_list = ["a",'b','Yoga','MMA','Youtube']
print(a_list.pop())
print(a_list.pop(1))
"""
List in boolen context
"""
def is_it_true(anything):
    if anything:
        print("Yes, Its True")
    else:
        print("No, its False")


is_it_true([])
is_it_true('a')
is_it_true([False])

"""
①	In a boolean context, an empty list is false.
②	Any list with at least one item is true.
③	Any list with at least one item is true. The value of the items is irrelevant.
⁂
"""

"""
Tuples : A tuple is an immutable list. A tuple can not be changed in any way once it is created.
Lists have methods like append(), extend(), insert(), remove(), and pop(). Tuples have none of these methods.
Some tuples can be used as dictionary keys (specifically, tuples that contain immutable values like strings, 
numbers, and other tuples). Lists can never be used as dictionary keys, because lists are not immutable.
"""
a_tuple = ("Yoga","MMA","YouTube","Business","Job","Yoga")
print(a_tuple[1])
print(a_tuple[-1])
print(a_tuple[1:3])
print(a_tuple.index("Yoga"))
print("MMA" in a_tuple)
print(a_tuple.count("Yoga"))
"""
Tuples in boolean context
To create a tuple of one item, you need a comma after the value. Without the comma, Python just assumes 
you have an extra pair of parentheses, which is harmless, but it doesn’t create a tuple.
"""
def is_it_true(anything):
    if anything:
        print("Yes, Its True")
    else:
        print("No, Its False")
is_it_true(())
is_it_true(("a","b"))
is_it_true((False,))
print(type((False,)))
# without comma its boolean
print(type((False)))
is_it_true((False))

"""
Assigning Multiple Values At Once
v is a tuple of three elements, and (x, y, z) is a tuple of three variables.
Assigning one to the other assigns each of the values of v to each of the variables, in order.
"""
v = ('a', 2, True)
(x, y, z) = v
print(x)
print(y)
print(z)
b_tuple = ("Yoga","MMA","YouTube")
(a,b,c) = b_tuple
print(a)
print(b)
print(c)
# Same tried for list
c_list = ["Yoga","MMA","YouTube"]
(e,f,g) = c_list
print(e)
print(f)
print(g)
(Mondays,Tuesdays,Wednesdays,Thursdays,Fridays,Saturdays,Sundays) = range(7)
print(Mondays)
print(Sundays)
[Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday] = range(7,14)
print(Monday)
print(Sunday)
"""
A set is an unordered “bag” of unique values. A single set can contain values of any immutable datatype.
Once you have two sets, you can do standard set operations like union, intersection, and set difference.
"""
a_set = {1}
print(type(a_set))
a_set = {1,2}
print(a_set)

# list can be converted into a set
d_list = ["True","Yoga","MMA","Yogabar"]
b_set = set(d_list)
print(b_set)
# To create an empty set
c_set = set() #To create an empty set, call set() with no arguments.
print(type(c_set))
d_set = {}
print(type(d_set)) # this will give dict as {} means dict
# Modifying a set
a_set.add(4)
print(a_set)
print(len(a_set))
a_set.add(1) # already one is there in the set it will not take duplicate item again
print(a_set)
print(len(a_set))
#Update
a_set.update({3,5,6})
print(a_set)
a_set.update({7,8,9},{10,11,12})
print(a_set)
a_set.update([13,14,15])
a_set.update((16,17,18))
print(a_set)
# Removing items from a set
a_set.discard(10)
print(a_set)
a_set.discard(10) #if we call it again with same number it will not throw any error
a_set.remove(11)
print(a_set)
#a_set.remove(11) Here’s the difference: if the value doesn’t exist in the set,
# the remove() method raises a KeyError exception.
"""
pop()
①	The pop() method removes a single value from a set and returns the value. However, 
since sets are unordered, there is no “last” value in a set, so there is no way to control which 
value gets removed. It is completely arbitrary.
②	The clear() method removes all values from a set, leaving you with an empty set. 
This is equivalent to a_set = set(), which would create a new empty set and overwrite the previous 
value of the a_set variable.
③	Attempting to pop a value from an empty set will raise a KeyError exception.
"""
print(a_set.pop())
print(a_set)
#print(a_set.pop(12))  #TypeError: set.pop() takes no arguments (1 given)
a_set.clear()
print(a_set)
#a_set.pop() #KeyError: 'pop from an empty set'
"""
Common set operations

①	To test whether a value is a member of a set, use the in operator. This works the same as lists.
②	The union() method returns a new set containing all the elements that are in either set.
③	The intersection() method returns a new set containing all the elements that are in both sets.
④	The difference() method returns a new set containing all the elements that are in a_set but not b_set.
⑤	The symmetric_difference() method returns a new set containing all the elements that are in exactly 
one of the sets.
"""
b_set = {1,2,3,4,5,6,7}
c_set = {6,5,4,8,9,10,12,13}

print(5 in b_set)
print(30 in c_set)
print(b_set.union(c_set))
print(b_set.intersection(c_set))
print(b_set.difference(c_set)) # all the elements in b_set but not in c_set
print(b_set.symmetric_difference(c_set))
"""
①	a_set is a subset of b_set — all the members of a_set are also members of b_set.
②	Asking the same question in reverse, b_set is a superset of a_set, because all the members of 
a_set are also members of b_set.
③	As soon as you add a value to a_set that is not in b_set, both tests return False.
"""
e_set = {1,2,3}
f_set = {1,2,3,4}
print(e_set.issubset(f_set))
print(f_set.issuperset(e_set))
e_set.add(5)
print(e_set.issubset(f_set))
print(f_set.issuperset(e_set))
"""
SET in boolean context
"""
def is_it_true(anything):
    if anything:
        print("Yes, It is true")
    else:
        print("No, Its false")
is_it_true(set())
is_it_true({'a'})
is_it_true({False})
"""
Dictionaries: A dictionary is an unordered set of key-value pairs. When you add a key to a dictionary,
you must also add a value for that key. (You can always change the value later.) Python dictionaries 
are optimized for retrieving the value when you know the key, but not the other way around.
"""
dict = {"Teacher":"Kamesh","Subject":"Yoga"}
print(dict["Teacher"])
print(dict["Subject"])
#print(dict["Yoga"]) # we can call using a key. This will raises an exception, because 'Yoga' is not a key.
"""
Modifying a dictionaries
"""
dict["Student"] = "Chandan"
print(dict)
dict["Teacher"] = 'I Kamesh'
print(dict)

SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

print(len(SUFFIXES))
print(1000 in SUFFIXES)
print('KB' in SUFFIXES) # it will only check keys not value
print(SUFFIXES[1000])
print(SUFFIXES[1024][3])
"""
Dictionaries in boolean context
"""
def is_it_true(anything):
    if anything:
        print("Yes,It is True")
    else:
        print("No its False")
is_it_true({})
is_it_true({'a':1})
"""
None:
None is a special constant in Python. It is a null value. None is not the same as False.
None is not 0. None is not an empty string. Comparing None to anything other than None will always return False.
None is the only null value. It has its own datatype (NoneType). You can assign None to any variable, but 
you can not create other NoneType objects. All variables whose value is None are equal to each other.
"""
print(type(None))
print(None == False)
print(None == 0)
print(None == '')
print(None == None)
x = None
print(x == None)
y = None
print(x == y)
"""
None in boolean context
"""
def is_it_true(anything):
    if anything:
        print("Yes, Its True")
    else:
        print("No, Its false")
is_it_true(None)
is_it_true(not None)



