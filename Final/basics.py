
list = [1,2,2,2,2,3,3,4,5,5,5,8,7,8]
x = len(list)
print(x)
print('*'*20)
print(list[:])
for i in list[:]:
    if (list.count(i) > 1):
        list.remove(i)
print("Unique List : ", list)

a = [10, 20, 10, 20, 20, 30, 30, 10, 80, 40,
     100, 50, 60, 70, 80, 90, 40, 60, 90, 10]

# removing duplicates via list.count() + list.remove() method
for element in a[:]:
    if (a.count(element) > 1):
        a.remove(element)

print("Unique List : ", a)

def remove_dup(a):
   i = 0
   while i < len(a):
      j = i + 1
      while j < len(a):
         if a[i] == a[j]:
            del a[j]
         else:
            j += 1
      i += 1

s = [1,2,2,2,2,3,3,4,5,5,5,8,7,8]
remove_dup(s)
print('*'*20)
print(s)

# def remove_dup1(a):
#     for i in range(len(a)):
#         for j in range(1, len(a)):
#             if a[i] == a[j]:
#                 del a[j]
#     print(a)
# s1 = [1,2,2,2,2,3,3,4,5,5,5,8,7,8]
# remove_dup1(s1)
# print(s1)
