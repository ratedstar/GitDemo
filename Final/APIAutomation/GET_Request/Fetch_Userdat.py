import json
import jsonpath
import requests

# API URL
url = "https://reqres.in/api/users?page=2"

# Send Get Request
response=requests.get(url)
print(response)

# Display Response Content
print(response.content)
print("Header")
print(response.headers)

# Validate status code
print(response.status_code)
assert response.status_code==200

# Fetch Response Header
print(response.headers)
print(response.headers.get("Date"))
print(response.headers.get("Server"))
# elapsed time is nothing but the time taken for sending request and getting the request
print(response.elapsed)
print("########################################################################")
#Parse response into JSON Format
json_response = json.loads(response.text)
print(json_response)
# Fetch value using jsonpath
#Whenever we apply jsonpath to any response it will return a list 
pages = jsonpath.jsonpath(json_response,'total_pages')
assert pages[0]==2
