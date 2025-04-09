while True:
    print("choise one of the options: \n\t 1) Encryption text \n\t 2) Deencryption text \n\t 3) Exit")
    choise = input("Enter: ")
    
    if choise == "1":
        text = input("Enter your text:")
        encrypted_text = ""
        for character in text:
            x = ord(character) * 2 + 6
            encrypted_text += chr(x)
        print("encrypted text:", encrypted_text)
        print("#"*40 + "\n")

    if choise == "2":
        encrypted_text = input("encrypted text: ")
        text = ""
        for character in  encrypted_text:
            x = (ord(character) - 6 ) // 2
            text += chr(x)
        print("text:", text)
        print("#"*40 + "\n")

        for character in text:
            x = ord(character) * 2 + 6
            encrypted_text += chr(x)
        print("encrypted text:", encrypted_text)
    elif choise == "3":
        print("*** See you later! ***")
        break