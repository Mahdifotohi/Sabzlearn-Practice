def fanc_gen(my_list):
    a = 0
    for i in my_list:
        a = a + i
        yield a



print(list(fanc_gen([1, 2, 3, 4, 5])))
