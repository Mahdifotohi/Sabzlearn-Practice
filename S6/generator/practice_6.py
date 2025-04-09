def fanc_gen():
    num = 1
    while True:
        yield " ".join([str(num)] * num)
        num += 1


gen = fanc_gen()
for _ in range(5):
    print(next(gen))
    