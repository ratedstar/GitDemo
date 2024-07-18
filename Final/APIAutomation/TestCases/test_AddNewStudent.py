import requests
import json
import jsonpath

def test_add_student_data():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails"
    file = open("E:/PythonExe/API_Samples/PostJSON.json","r")
    json_request = json.loads(file.read())
    response= requests.post(API_URL,json_request)
    print(response.text)

def test_get_student_data():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/3841561"
    response = requests.get(API_URL)
    #json_response = json.loads(response.text)n
    json_response= response.json()
    id = jsonpath.jsonpath(json_response,'data.id')
    assert id[0] == 3841561,"Assert Fail"
    print(response.text)