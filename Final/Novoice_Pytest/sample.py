#Count occurance of each character
string = "My name is automation test engineer"
dict = {}
for i in string:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print(dict)

str = "Jonny Jonny Yes Pappa Eating sugar No papa papa"
words = str.split(' ')
dict= {}
for word in words:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1
print(dict)
print("###############################################################")
str2 = "My name is kamesh, I am a your yoga teacher"
dict= {}
for char in str2:
    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1
print(dict)
print("*"*50)


for i in [1,2,3,4][::-1]:
    print(i)

str11 = "Yes yes yes No No no no Yes Why why"
dict = {}
words = str11.split(" ")
for word in words:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1
print(dict)
dict1={}
for char in str11:
    if char in dict1:
        dict1[char] += 1
    else:
        dict1[char] = 1
print(dict1)

i = 1
while True:
    if i%3 == 0:
        break
    print(i)
    i += 1

list1 = ["yoga",[2,3,"king","Murli"],"Calithenics"]
print(list1[1][3][2])