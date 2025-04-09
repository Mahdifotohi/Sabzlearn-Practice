 
def my_len(i):

    mylist = list(str(i))
    num = 0
    for _ in mylist:
        num += 1
    return num


i = input("Enter your wolrd: ")
print("Resulte: ", my_len(i))


