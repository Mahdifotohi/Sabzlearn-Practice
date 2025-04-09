while True:
    my_input = input("Enter your text: ")
    if my_input == "":
        break
    else:
        with open(r"C:\Users\victus 15\Desktop\Sabzlearn\S9\notes.txt", "a", encoding="utf8") as my_file:
            my_file.write(my_input + "\n" )
            