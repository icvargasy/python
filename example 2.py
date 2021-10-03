"""
secret_number = 5
guess = input("Enter a number between 1 and 10: ")
print(secret_number == int(guess))

secret_word = "kitty"
guess_word = input("Enter a word of 5 letters: ")
comparison = secret_word == guess_word
print("Your guess is " + str(comparison))
"""

def money_converter(amount:float, div1: str, rate:float, div2:str) -> str:
    result = amount / rate 
    msg_1 = " " + div1 + " in " + div2 + " is "
    new_func(result)
    return str(amount) + msg_1 + str(round(result,2))

def new_func(result):
    if result  >= 10 :
        print("this is a lot of money")
    else:
        print("naaaa....")

amount = float(input("Please input the amount to convert: "))
div1 = str(input("Which currency it is? "))
rate = float(input("Which is the exchange rate? "))
div2 = str(input("To which currency you convert? " ))
print(money_converter(amount,div1,rate,div2))

