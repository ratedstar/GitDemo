input_string ="cat is a animal"
input_word = "cat"
for char_input_word in input_word:
    print("for character\"%s\":"% char_input_word, end="")
    no_of_occurances =0
    print("index:",end="")
    for index, char_input_string in enumerate(input_string,1):
        if char_input_string == char_input_word:
            print("[%s]," % index,end="")
            no_of_occurances += 1
    print(":no of occurance \"%s\"\n"% no_of_occurances)


i=1
for word in input_word:
    if input_word[:i] in input_string:
        print("%s"%input_word[:i])
        i += 1


# input_string = "cat is a animal"
# input_word = "cat"
# for char_input_word in input_word:
#     print("for character \"%s\:"% char_input_word, end="")
#     no_of_occurances =0
#     print("index:",end="")
#     for index, char_input_string in enumerate(input_string,1):
#         if char_input_string == char_input_word:
#             print("[%s],"% index, end="")
#             no_of_occurances += 1
#     print(":no of occurance\"%s\"\n"% no_of_occurances)
#
#
# input_string = "cat is a animal"
# input_word = "cat"
# for char_input_word in input_word:
#     print("for character\"%s\":"%char_input_word, end='')
#     no_of_occurances = 0
#     print("index:",end="")
#     for index, char_input_string in enumerate(input_string,1):
#         print("[%s],"% index,end="")
#         no_of_occurances += 1
#     print(":no of occurance\"%s\"\n" % no_of_occurances)