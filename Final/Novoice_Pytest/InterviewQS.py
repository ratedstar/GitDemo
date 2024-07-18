print("Hello world")

dict = {"name": ["kamesh", "Kiran"], "location": ["pune", "hyderabad"]}
for i in range(0, 2):
    print(dict["name"][i].upper())
for i in range(0, 2):
    print(dict["location"][i].title())

print(dict.items())
for i in range(0, 2):
    dict[i]
for k, v in dict.items():
    dict.update(k.upper(): v.upper())
    print(dict)