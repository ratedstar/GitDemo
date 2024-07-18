import requests
import json
import jsonpath

url = "https://reqres.in/api/users/2"

file = open("C:\\Users\\HP\\Downloads\\API\\post.json",'r')
json_input = file.read()
request_json = json.loads(json_input)
# PUT method
response = requests.put(url,request_json)
print(response.text)
response_json = json.loads(response.text)
updateddate = jsonpath.jsonpath(response_json,"updatedAt")
name = jsonpath.jsonpath(response_json,"name")
print(name[0])
print(updateddate[0])
assert response.status_code == 200

