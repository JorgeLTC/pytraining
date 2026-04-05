import random


def main() -> None:
    # 1. Setup PhaseCreate your categories dictionary (you already have this)
    categories = {
        "Animals": ["LION", "TIGER", "BEAR"],
        "Cars": ["NISSAN", "HONDA", "MERCEDES", "VOLKSWAGEN"],
        "Tech": ["LAPTOP", "INTERNET", "DATABASE"],
        "Countries": ["MEXICO", "FRANCE", "SPAIN", "GERMANY"],
        "Food": ["TACOS", "PIZZA", "RAMEN", "SUSHI"],
    }

    print("\n" + "=" * 40)
    print("          HANGMAN")
    print("=" * 40)
    while True:
        # Category Selection
        print("\nChoose a category:")
        for cat in categories.keys():
            print(f" → {cat}")

        while True:
            choice_cat = input("\nPlease choose a category: ").strip().title()
            if choice_cat in categories:
                break
            print("Invalid category! Try again.")

        # Game Setup
        rand_word = random.choice(categories[choice_cat])
        display: list[str] = ["_"] * len(rand_word)
        guessed_letters: set[str] = set()
        lives: int = 6

        print(f"\nCategory: {choice_cat} | Word has {len(rand_word)} letters")

        # Main Guessing Loop
        while lives > 0 and "_" in display:
            print("\n" + " ".join(display))
            print(f"Lives left: {lives}")
            print(f"Guessed letters: {', '.join(sorted(guessed_letters)) or 'None'}")

            user_guess = input("\nGuess a letter: ").strip().upper()

            if len(user_guess) != 1 or not user_guess.isalpha():
                print("Please enter a single letter (A-Z).")
                continue

            if user_guess in guessed_letters:
                print("You already guessed that letter!")
                continue

            guessed_letters.add(user_guess)

            if user_guess in rand_word:
                for i in range(len(rand_word)):
                    if rand_word[i] == user_guess:
                        display[i] = user_guess
                print(" Good guess!")
            else:
                lives -= 1
                print("❌ Wrong guess!")

        # Game Result
        print("\n" + "=" * 40)
        if "_" not in display:
            print(f" YOU SAVED THE HANGMAN! The word was: {rand_word}")
        else:
            print(f" GAME OVER! The word was: {rand_word}")
        print("=" * 40)

        # Play Again
        confirm = input("\nDo you want to play again? (y/n): ").strip().lower()
        if confirm not in ("y", "yes"):
            print("Thank you for playing! Goodbye")
            break


if __name__ == "__main__":
    main()
