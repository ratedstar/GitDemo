import json
import jsonpath
import requests
path= "E:\PythonExe\API_Samples\Sampleinterview.json"

file = open("C:/Users/HP/workspace_python/Final/api.json",'r')
json_response = json.loads(file.read())
print(len(json_response['Employees']))
for employee in json_response['Employees']:
    print(employee['userId'])
    #del employee['phoneNumber']
    if employee['jobTitleName']=='Developer':
        employee['employeeCode'] = 'abc'
with open("C:/Users/HP/workspace_python/Final/api.json",'w') as f:
    json.dump(json_response,f)
file = open("C:/Users/HP/workspace_python/Final/api.json",'r')
json_response = json.loads(file.read())
print(json_response)
new_string = json.dumps(json_response, indent=2)
print(new_string)



# job_title = jsonpath.jsonpath(json_response,'Employees[0].jobTitleName')
# employee = jsonpath.jsonpath(json_response,'Employees')
# print(len(employee))
# for i in range(0,3):
#     employee = jsonpath.jsonpath(json_response,'Employees[{}].jobTitleName'.format(i))
#     print(employee[i])
#     if employee[i] == 'Developer':
#         employeeCode = jsonpath.jsonpath(json_response,'Employees[{}].employeeCode'.format(i))
#         print(employeeCode)
#
#
# print(job_title)

