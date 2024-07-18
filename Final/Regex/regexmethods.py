import re

line1 = "pet:cats I love them"
line = "I love cats "
line2 = "pets are better. pets are good. pets are adorable. I have a pet."
line3 = "I love pet:cats them"

#match function
#match = re.match(pattern,string,<flag=0>)
# var = re.match("pet\:\w+",line3)
# print(var)
# print(var.group(0))
pattern = re.compile("pet")
var1 = pattern.match(line3,pos=7)
print(var1)
print(var1.group(0))