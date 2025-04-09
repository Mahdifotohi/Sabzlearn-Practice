import csv

def sum_column(file_path, column_name):
    total_sum = 0
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # بررسی عددی بودن مقدار ستون
                value = row.get(column_name)
                if value and value.isdigit():
                    total_sum += int(value)
                else:
                    print(f"Skipping non-numeric value: {value}")
        
        return total_sum
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

file_path = "data.csv"
column_name = "age"
result = sum_column(file_path, column_name)
if result is not None:
    print(f"The sum of the '{column_name}' column is: {result}")