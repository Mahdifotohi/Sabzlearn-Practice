
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("even:", len(list(filter(lambda x: x % 2 == 0, num))))
print("odd:", len(list(filter(lambda x: x % 2 > 0, num))))
