import json

with open('/Users/shruti/git/Python/data.json') as data_file:
    data = json.load(data_file)

print(data)

json_string = json.dumps(data)
print("JSON String: " + json_string)