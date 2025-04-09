number1 = int(input("Enter your number: "))

count = 0
while (number1 > 0):
    count += 1
    number1 = number1 // 10

print("Resulte: ", count)