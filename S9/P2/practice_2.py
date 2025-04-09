import json

def convert(key, string):
    string_json = json.loads(string)
    return string_json.get(key, "key not find")



my_json = '{"name": "amir", "job": "enginear", "age": "19", "bol": "True"}'
my_key = "job"
print(convert(my_key, my_json))

