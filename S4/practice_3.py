ch = ord(input("enter Character: "))

if 65 <= ch <= 122 :
    print("It Is a Char")
elif 123 <= ch <= 225 or 0 <= ch <= 47:
    print("It Is a cimbele")
elif 48 <= ch <= 57:
    print("It Is a Number")