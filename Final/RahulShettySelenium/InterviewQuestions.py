# i/p: "kaamesh is qa"
#o/p: "Kaamesh Is Qa"
str1 = "Kaamesh is qa"
list_of_words = str1.split()
list_of_new_str = []
str2 =" "
for word in list_of_words:
    result = word[0].upper()+word[1:]
    list_of_new_str.append(result)
print(list_of_new_str)
str2 = str2.join(list_of_new_str)
print(str2)