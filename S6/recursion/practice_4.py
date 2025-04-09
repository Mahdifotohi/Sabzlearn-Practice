def rec_fanc(mylist, element):
    if not mylist:
        return 0
    return (1 if mylist[0] == element else 0) + rec_fanc(mylist[1:], element)


print(rec_fanc([1, 2, 3, "reza", 3, 10], 3))