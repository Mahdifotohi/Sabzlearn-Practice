number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))

list1 = []
list2 = []

for i in range(1, number1):
    if ((number1 % i) == 0):
      list1.append(i) 
    else:
        i += 1

for i in range(1, number2):
    if ((number2 % i) == 0):
        list2.append(i)   
    else:
        i += 1

list3 = (set(list1)) & (set(list2))
print("Resulte: ",list3 )