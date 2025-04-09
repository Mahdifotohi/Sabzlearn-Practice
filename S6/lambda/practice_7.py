is_numiric = lambda string: True if string.replace('.', '', 1).isdigit() else False

strings = ["123", 'abc', "4.5", "11.75", "3.478"]
results = {string: is_numiric(string) for string in strings}
for string, result in results.items():
    print(f"Is the string '{string}' numeric? {result}")