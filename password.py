import random
import string

wordbank = [
    "summer",
    "warehouse",
    "winter",
    "apple",
    "jackson",
    "sunday",
    "monday",
    "freedom",
    "safety",
]
symbolpool = string.punctuation


def generate_password():
    password = ""
    for i in range(4):
        password += f"{random.choice(wordbank[0].upper())}{random.choice(wordbank[1:])}{random.randint(1, 20)}{random.choice(symbolpool)}"
    return password


print(generate_password())
