while (True):
    input1 = input("Enter your text (exit = exit): ")
    if input1.lower() == "exit":
        break
    else:
        with open("outpute.txt", "a", encoding="utf8") as my_file:
            my_file.write(input1 + "\n" )
                             


 