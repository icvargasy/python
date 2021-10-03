"""
guess = input("what is the result of 5+2? ")

if int(guess) == 7: 
    print("congratulations")
else: 
    print("try again ")

print("The program terminated successfully")
"""

number1 = float(input("Please enter a number: "))
number2 = float(input("Please enter another number: "))
subtraction = number2 - number1

if subtraction > 10:
    print("The result is greather than 10")
elif subtraction > 0:
    print("The result is larger than 0 but smaller than 10")
elif subtraction == 0:
    print("The result is zero")
else: 
    print("The result is a negative number")

print("You can try again")
