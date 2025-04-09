import json

def updated(string, key_value):
    my_dict = json.loads(string)
    my_dict.update(key_value)
    return my_dict


my_json = '{"name": "amir", "job": "enginear", "age": "19", "bol": "True"}'
key_value = {"name": "mahdi"}
print(updated(my_json, key_value))
