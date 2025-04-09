import json

def maching(string1, string2):
    my_string1 = json.loads(string1)
    my_string2 = json.loads(string2)
    my_string1.update(my_string2)
    my_json = json.dumps(my_string1)
    return my_json


my_json1 = '{"name": "amir", "job": "enginear", "age": "19", "bol": "True"}'
my_json2 = '{"txt": "Hello World"}'
print(maching(my_json1, my_json2))
