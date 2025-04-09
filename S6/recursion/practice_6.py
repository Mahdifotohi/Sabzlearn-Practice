def rec_fanc(num):
    if num == 0:
        return 0
    else:
        return num % 10 + rec_fanc(num // 10)



print(rec_fanc(123456))