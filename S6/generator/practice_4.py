def fanc_gen(string):
    for i in reversed(string):

        yield i


my_string = "hello"
gen = fanc_gen(my_string)
for char in gen:
    print(char)