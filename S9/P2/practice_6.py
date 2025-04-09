import json
import csv

def convert(string):
    with open("json_file.csv", "w", encoding="utf8") as file:
       my_file = file.write(string)
    return "Compeled Task :)"


my_json = '{"name": "amir", "job": "enginear", "age": "19", "bol": "True"}'
print(convert(my_json))
