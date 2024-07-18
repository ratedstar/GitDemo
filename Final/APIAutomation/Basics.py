import json
odics = '{"K1":"V1","K2":"V2"}'
json_result = json.loads(odics)

print(json_result)

"""
JIRA, BUGZILLA rest api based tools. Behind the scene they use rest api
operations in jira we can report a bug or fetch info the bug or update info about the bug or delete info about 
a bug
GET Fetch data from an application (Reported a bug previously we need to get info about the bug)
POST Add new data / resource to the application(Whenever we want to add new info to the system exp: New Bug)
PUT update data into application (If we want to update summary or description of a bug)
DELETE delete data in application
PATCH its similar to PUT but will require only updated date to send 
When we are making request to the server in the response we are getting header and body 
body contains actual response but header has some other info like date and time what is the format of the body
Do we use any encription over there 
Head: Fetch only header data from the application
Options: to find out which requests methods server supports (Allow: OPTIONS,GET,HEAD,POST)
TRACE: This method performs a message loop-back means it will return message content as Response, providing a useful
debugging mechanism 

API with parameters 
When we use a uri suppose we use get() means we are going to fetch some data from the server 
when we hit any request and we are sending some data, data will be send as part of URI and we call it as parameters
https://reqres.in/api/users?page=2
"""