import json
import requests
import jsonpath

#API URL
url = "https://reqres.in/api/users?page=2"

# Send request
response = requests.get(url)

# parse json
json_response = json.loads(response.text)
print(json_response)
#Fetch data from json path
firstname = jsonpath.jsonpath(json_response,'data[1].first_name')
print(firstname[0])

# If we want all names
for i in range(0,3):
    firstname = jsonpath.jsonpath(json_response,'data['+str(i)+'].first_name')
    print(firstname[0])

