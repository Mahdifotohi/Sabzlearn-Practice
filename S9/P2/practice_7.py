import csv

def write(my_dict):
    with open("CSV_file.csv", "w", encoding="utf8", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=my_dict[0].keys())
        writer.writeheader()
        writer.writerows(my_dict)
    return "Task Is Comped :) "


my_dict =   [
            {"name": "amir", "job": "enginear", "age": "19", "bol": "True"},
            {"name": "mahdi", "job": "enginear", "age": "23", "bol": "Fals"}
            ]
print(write(my_dict))