import math

def my_fanc(arg):
    arg = int(str(arg))
    radicl = math.sqrt(arg)
    if radicl ** 2 == arg:
        print("Yes")
    else:
        print("No")

arg = input("Enter your number: ")
my_fanc(arg)