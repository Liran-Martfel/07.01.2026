num_1 = int(input("Please enter a number: "))
num_2 = int(input("Please enter a number: "))
while num_1!=num_2:
    print("your sum of numbers are: ",num_1+num_2)
    num_1 = int(input("Enter a number: "))
    num_2 = int(input("Enter a number: "))
    if num_1==num_2:
        print("your numbers are the same")
