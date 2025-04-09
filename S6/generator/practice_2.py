
def fibonachi(x):
    a, b = 0, 1
    for _ in range(x):
        yield a
        a, b = b, a + b


print(list(fibonachi(10)))





