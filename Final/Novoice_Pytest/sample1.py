a= "kamesssaaaah"
newlst = list(a)
print(newlst)

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
def remove_dup(b):
    i = 0
    while i < len(b):
        j= i + 1
        while j < len(b):
            if b[i] == b[j]:
                del b[j]
            else:
                j += 1
        i += 1
# def remove_dup1(a):
#     for i in range(0,len(a)):
#         for j in range(1,i+1):
#             if a[i] ==a[j]:
#                 del a[j]
#     print()

"""
The challenge is that deleting a value shifts later values to the left. 
This messes with the next indexed value and the total length of the list. 
Your index i is based on the position and length of the original list but you are carving up the underlying list.
Suppose you did the process in reverse. Scan from the end to the front 
and only delete values that are past the next indexed value you will traverse. 
This way you won't affect the list items you haven't processed.
"""
s =  list(a)
remove_dup(s)
print('*'*20)
print(s)


# def remove_dup1(a):
#    for i in range(len(a) - 1, -1, -1):
#       print(a[i])
#       for j in range(i - 1, -1, -1):
#          print(a[j],"*"*3)
#          if a[i] == a[j]:
#             del a[i]
#             break
#
#
# s1 = [1, 2, 2, 2, 2, 3, 3, 4, 5, 5, 5, 8, 7, 8]
# remove_dup1(s1)
# print(s1)

# string occurance of each character

def count_char(text):
  for i in range(len(text)):
    if len(text) == 0:
      break
    ch = text[0]
    # don't count frequency of space3
    if ch == ' ' or ch == '\t':
        continue
    count = 1
    for j in range(1, len(text)):
      if ch == text[j]:
        count += 1
    text = text.replace(ch, '').strip()
    print(ch + " - ", count)

count_char('Python')

