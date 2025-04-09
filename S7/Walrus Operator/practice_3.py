num = 0
while True:
    my_input = input("Enter number: (EXET:"")")
    
    if (s:= my_input) == "":
        print("***EXET***: sum your numbers:",(num))
        break
    else:
        num += int(my_input)
        print("sum your numbers:",(num))
        continue
        


