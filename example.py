print('Hello \" world')
celsius = 21
farenheit = celsius*9/5 + 32
print(farenheit)

def colors() :
    print( 'Red is a color')
    print( 'Blue is a color')

colors()

def subtract(num1, num2) :
    result = num1 - num2
    print(result)

def multiply(num1, num2, num3) :
    result = num1 * num2 * num3
    print(result)

subtract(5,3)
multiply(1,2,3)

def converter(celsius:float) -> str :
    result = celsius*9/5 + 32
    return str(celsius) + " degrees Celsius are " + str(result) + " degrees Farenheit"

print(converter(21.5))
print(converter(-7))

def money_converter(amount:float, div1: str, rate:float, div2:str) -> str:
    result = amount / rate 
    msg_1 = " " + div1 + " in " + div2 + " is "
    return str(amount) + msg_1 + str(round(result,2))

amount = float(input("Please input the amount to convert: "))
div1 = str(input("Which currency it is? "))
rate = float(input("Which is the exchange rate? "))
div2 = str(input("To which currency you convert? " ))
print(money_converter(amount,div1,rate,div2))