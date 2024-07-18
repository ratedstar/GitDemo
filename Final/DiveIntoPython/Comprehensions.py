"""
List Comprehensions:
A list comprehension provides a compact way of mapping a list into another list by applying a function to 
each of the elements of the list.
"""
a_list = [1,9,8,4]
print([elem*2 for elem in a_list]) # it will not modify the existing list it will return new list
print([elemt*3 for elemt in a_list])
print(a_list)
a_list = [elem *2 for elem in a_list]
b_list = [elem*3 for elem in a_list]
print(b_list)
"""
 Dictionary Comprehensions
"""
dict = {"a":1,"b":2,"c":3}
print({value:key for key,value in dict.items()})
print({value:key for key,value in dict.items()})
"""
this only works if the values of the dictionary are immutable, like strings or tuples. If you try this 
with a dictionary that contains lists, it will fail most spectacularly.
"""
a_dict = {'a':[1,2,3],"b":4,"c":5}
#print({value:key for key,value in a_dict.items()}) TypeError: unhashable type: 'list'
b_dict = {'a':(1,2,3),"b":4,"c":5}
print({value:key for key,value in b_dict.items()}) #It worked for tuple
"""
Set comprehensions
"""
a_set = set(range(6))
print(a_set)
print({x*2 for x in a_set})
print({x*2 for x in a_set})
print({x for x in a_set if x%2 ==0})
print({x for x in a_set if x%2==0})

