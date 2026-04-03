import random


def guess_number():
    number = random.randint(1, 10)
    guess = None
    tries = 10
    while guess != number:
        if tries == 0:
            print("Sorry, you ran out of tries!")
            break
        print(f"You have {tries} tries left.")
        guess = int(input("Guess a number between 1 and 10: "))
        if guess < number:
            print("Too low!")
            tries -= 1
        elif guess > number:
            print("Too high!")
            tries -= 1
        else:
            print("You guessed it!")
            break


if __name__ == "__main__":
    guess_number()
