from random import random,randint

num = 0
while (r := randint(1, 100)) > 80:
        print("numbers:",r)
        num += 1

print("count:",num)
