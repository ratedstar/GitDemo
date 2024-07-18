obj = open("C:\\Users\\HP\\workspace_python\\Final\\Novoice_Pytest\\SampleRead.txt",'r')
print(obj.read())


import json
import jsonpath
import requests

url = "https://reqres.in/api/users?page=2"

# response = requests.get(url)
# print(response.text)
# print(response.status_code)
# assert response.status_code == 200
# print(response.headers)
# print(response.headers.get("Date"))
# print(response.headers.get("Server"))
#
# json_response = json.loads(response.text)
# page = jsonpath.jsonpath(json_response,"data[0].first_name")
# id = jsonpath.jsonpath(json_response,"data[0].id")
# print(page[0])
# print(id[0])
"""
POST 
Read input json from file
Parse input json format
Hit post method 
Parse response to json format
Validate response
"""
file = open("C:\\Users\\HP\\Downloads\\API\\post.json",'r')
json_input = file.read()
request_json = json.loads(json_input)

response = requests.post(url,request_json)
json_response = json.loads(response.text)
print(json_response)
assert response.status_code == 201

id = jsonpath.jsonpath(json_response,"id")
create = jsonpath.jsonpath(json_response,"createdAt")
print(create)
print(id)