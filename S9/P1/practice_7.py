serch_world = input("Enter your word for search: ")
re_world = input("Enter your word for replace: ")

with open(r"C:\Users\victus 15\Desktop\Sabzlearn\S9\document.txt", "r", encoding="utf8") as my_file:
    contents = my_file.read()

new_contents = contents.replace(serch_world.lower(), re_world.lower())

with open(r"C:\Users\victus 15\Desktop\Sabzlearn\S9\document.txt", "w", encoding="utf8") as my_file:
    my_file.write(new_contents)
