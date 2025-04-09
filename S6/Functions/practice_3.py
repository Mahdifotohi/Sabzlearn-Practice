
def my_sum(arg):
    
    num = 0
    for i in arg:
        num = i + num
        i += i
    return num
 

a = (1, 2, 3, 4, 5)
print(my_sum(a))