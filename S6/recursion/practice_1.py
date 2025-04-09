
def fanc(mylist):
    if not mylist:
        return 0
    return mylist[0] + fanc(mylist[1:])
    


print(fanc([1, 2, 3, 4]))
