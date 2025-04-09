my_list = [1, 2, 3, 4, 5]

for i in my_list:
    if (x := i) == 5:
        print("yes it is and index:", my_list.index(x))
        break
    i += 1

