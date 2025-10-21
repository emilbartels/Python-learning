print("Enter two numbers, which i will then add together")
firstnumber = input("First number: ")
secondnumber = input("Second number: ")

try:
    result = int(firstnumber) + int(secondnumber)
    print(f"The result of {firstnumber} + {secondnumber} is {result}")
except ValueError:
    print("You have to enter numbers!")