from random import choice
name = ["ali", "amir", "mahdi", "mahsa", "saba", "ahora", "mohammad", "zynab", "reza", "hadi"]

copy = name.copy()

for _ in range(10):
    input1 = choice(copy)
    print( "dorost hads zadam?",input1)
    h = input("yes or no?")
    if h == "no":
        copy.remove(input1)
    if h == "yes":
        print()
        print("*" * 20)
        print("didi zehneto khondam :)")
        print("*" * 20)
        print()
        break