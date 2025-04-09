with open(r"C:\Users\victus 15\Desktop\Sabzlearn\S9\numbers.txt", "r", encoding="utf8") as my_file:
    numbers = my_file.readlines()
    numbers = [int(num.strip()) for num in numbers]     
    total_sum = sum(numbers)
    avreage = total_sum / len(numbers)   
    print("Sum: ", total_sum)
    print("Avrage: ", avreage)

        