secret_number = 10
secret_word = "hola"

def word_number(number:float,word:str) -> str: 
    if number >20 or number < 0 :
        return "number out of interval"
    else :
        if number == secret_number and word == secret_word:
            return "you guessed both"
        elif number == secret_number or word == secret_word:
            return "you guessed one"
        else:
            return "better luck next time" + "\n" + "good night"

print(word_number(
            float(input("provide a number between 0 and 20: ")),
            input("provide a word: ").lower()
    ))