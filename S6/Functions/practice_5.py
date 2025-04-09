
def off(price, percent):
    new_price = ((price * percent) / 100)
    return new_price


price = int(input("Enter your price: "))
percent = int(input("Enter your percent: "))
print(off(price, percent))

