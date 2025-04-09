
def main(my_input):
    while True:
        if 65 <= my_input <= 122 :
            print("It Is a Char")
            break
        elif 48 <= my_input <= 57:
            print("It Is a Number") 
            break 
        elif 123 <= my_input <= 225 or 0 <= my_input <= 47:
            print("It Is a cimbele")  
            break
        else:
            print("other")
            break


my_input = ord(input("Enter character: "))
main(my_input)
    


