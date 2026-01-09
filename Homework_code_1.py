number = int(input("Enter a number: "))
while number%2==0:
    print(number)
    print("enter another number")
    number = int(input("Enter a number: "))
    if number%2!=0:
        print("your numbre isn't zugi")
       # number = int(input("Enter a number: ")) - אופציה להמשך אין סופי
