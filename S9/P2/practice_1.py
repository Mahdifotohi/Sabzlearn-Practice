import json

def parse(my_input):
    convert = json.loads(my_input)
    return convert

my_json = '{"name": "amir", "job": "enginear", "age": "19", "bol": "True"}'
print(parse(my_json))

