def inf_number(even=True):
    num = 0 if even else 1
    while True:
        yield num
        num += 2


even_gen = inf_number(even=True)
odd_gen = inf_number(even=False)

for _ in range(10):
    print(next(odd_gen))

# for _ in range(10):
#     print(next(even_gen))

