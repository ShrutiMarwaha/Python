import json
import yaml

print("--------------JSON--------------------")
with open('/Users/shruti/git/Python/data.json') as jason_file:
    jdata = json.load(jason_file)

print(jdata)

json_string = json.dumps(jdata)
print("JSON String: " + json_string)

print("\n--------------YAML--------------------")
with open('/Users/shruti/git/Python/data.yaml') as yaml_file:
    ydata = yaml.load(yaml_file)

print(ydata)

yaml_string = json.dumps(ydata)
print("yaml String: " + yaml_string)