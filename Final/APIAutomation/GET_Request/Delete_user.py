import requests
import json
import jsonpath

#Api url
url = "https://reqres.in/api/users/2"

#Delete
response = requests.delete(url)
print(response.status_code)

assert response.status_code==204

