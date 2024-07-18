import json

odics = '{"K1":"Value","K2":"Value2"}'
jsonresult = json.loads(odics)
print(jsonresult["K1"])