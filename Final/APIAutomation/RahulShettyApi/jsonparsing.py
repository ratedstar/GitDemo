import json

course = '{"name":"Kaamesh","Languages":["java","Python"]}'


# loads method will parse string and returns dictionary
dict_json = json.loads(course)
print(dict_json)
print(dict_json["Languages"][0])

with open("C:\\Users\\HP\\Downloads\\PythonSeleniumAPI\\course1.json") as f:
    data = json.load(f)
    print(data)
    print(type(data))
    print(data["courses"][2]["title"])
    print(data["dashboard"]["website"])
    print(data["courses"][2]["price"])
    print("*"*20)
    for course in data["courses"]:
        if course['title'] == "RPA":
            print(course["price"])
            assert course["price"] == 45
with open("C:\\Users\\HP\\Downloads\\PythonSeleniumAPI\\course.json") as fi:
    data2 = json.load(fi)
    assert data == data2