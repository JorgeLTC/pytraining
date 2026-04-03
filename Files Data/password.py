import random
import string


def generate_password(length):
    if length < 4:
        length = 4

    symbolpool = string.punctuation
    allchar = string.ascii_letters + string.digits + symbolpool

    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(symbolpool),
    ]

    while len(password) < length:
        password.append(random.choice(allchar))

    random.shuffle(password)
    return "".join(password)


if __name__ == "__main__":
    length = int(input("Enter password length: "))
    print(generate_password(length))
