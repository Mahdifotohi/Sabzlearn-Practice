with open(r"C:\Users\victus 15\Desktop\Sabzlearn\S9\source.txt", "r", encoding="utf8") as file:
    data = file.read()
with open(r"C:\Users\victus 15\Desktop\Sabzlearn\S9\destination.txt", "w", encoding="utf8") as file2:
    file2.writelines(data)
    print("#" * 40)
    print("Your file has been copied.")
    print("#" * 40)


