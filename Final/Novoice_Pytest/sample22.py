# str= "today is thursday today is thursday"
# dict = {}
# str1 = str.split(" ")
# count = 0
# print(str1)
# for word in str1:
#     if word in dict:
#         dict[word] += 1
#     else:
#         dict[word] = 1
# print(dict)
str = "This is kamesh kamesh is my name"
dict = {}
words = str.split(" ")
for word in words:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1
print(dict)

str = "kaaaaammmmeeeeesssssshhhhhhh"
dict={}
for char in str:
    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1
print(dict)




string1 = input("Enter any string")
dict ={}
for char in string1:
    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1
print(dict)

sentence = input("Enter a sentence")
dict={}
words = sentence.split(" ")
for word in words:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1
print(dict)




