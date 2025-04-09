def rec_pow(x, y):
    if x == 0:
        return 1
    elif y == 1:
        return x
    else:
        return x * rec_pow(x, y - 1)

print(rec_pow(2, 4))