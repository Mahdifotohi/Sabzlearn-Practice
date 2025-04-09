with open(r"C:\Users\victus 15\Desktop\Sabzlearn\S9\data.txt", "r", encoding="utf8") as file:
    linse = file.readlines()

    for line in linse:
        after_line = " ".join(line.split())
        print(after_line)
