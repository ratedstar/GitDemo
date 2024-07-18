import requests
import json
import jsonpath

url = "https://reqres.in/api/users?page=2"
headerdata = {"T1":"firstHeader","T2":"SeconHeader"}
respose = requests.get("https://httpbin.org/get",headers=headerdata)
print(respose.text)

param = {"name":"kamesh","Class":"Yoga"}

response = requests.get("https://httpbin.org/get",params=param)
print(response.text)