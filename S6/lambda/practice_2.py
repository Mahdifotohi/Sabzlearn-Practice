from functools import reduce
my_list = [('Ali', 93), ('Reza', 65), ('Mahdi', 81), ('Baran', 21)]
print(sorted(my_list, key= lambda x: x[1]))
