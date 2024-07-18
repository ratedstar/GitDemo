import requests
import json

#URL parameters n url are separated by ? it it is a get http method these are called query parameters
#sometime we have / we call these parameters as form parameters
# get() will take url, parameters in dict format n thrid is any optional parameters or header values
#get() will not have any body to talk to servers
response = requests.get("https://reqres.in/api/users",params={"page":"2"},)
print(response.text)
print(type(response.text))
json_response = response.json()

print(json_response["data"][0]['email'])