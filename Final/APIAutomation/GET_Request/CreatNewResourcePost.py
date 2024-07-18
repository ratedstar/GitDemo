import requests
import json
import jsonpath
# Whenever we want to make a new resource in server we use post request
#API URL
"""
1. Read input json from file
2. Parse into json format
3. Hit post method
4. Parse response to json format
5. Validate Response 
"""
url = "https://reqres.in/api/users"
url1 = "https://reqres.in/api/users"

#Read input json file
file = open("C:\\Users\\HP\\Downloads\\API\\post.json","r")
json_input = file.read()
request_json = json.loads(json_input)

#Make Post request with json body
response = requests.post(url,request_json)
print(response.content)
assert response.status_code == 201

#Fetch headers from response
print(response.headers.get('Content-Length'))

#Parse response to json format
response_json = response.json()

#pick id using json path
id = jsonpath.jsonpath(response_json,'id')
print(id[0])