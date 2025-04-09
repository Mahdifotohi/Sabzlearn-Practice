a = int(input("Enter Number 1 : "))
b = int(input("Enter Number 2 : "))
c = int(input("Enter Number 3 : "))

if ((a + b) > c) or ((c + a) > b) or ((b + c) > a):
    print("Yes, It Is a Triangle.")
    if a == b or a == c or b == c:
        print("isosceles Triangle")
    if a == b == c:
        print("Equilateral Triangle.")
    if (a ** 2) == ((b ** 2) + (c ** 2)):
        print("Right Triangle.")

    if a and b and c:
        print("مختلف الاضلاع")

else:
    print("NO, It Is Not a Triangle.")