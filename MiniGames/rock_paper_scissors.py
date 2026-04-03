import random


def main() -> None:
    moves: list[str] = ["Rock", "Paper", "Scissors"]

    print("\n" + "=" * 40)
    print("          ROCK, PAPER, SCISSORS!")
    print("=" * 40)
    print("best of 3 wins!\n")

    while True:
        user_score: int = 0
        comp_score: int = 0

        while user_score < 2 and comp_score < 2:
            # Show the current score
            print(f"Score: Player {user_score} | Computer {comp_score}")
            # Get the user's move
            user_move = (
                input("\nEnter your move (Rock, Paper, Scissors): ").strip().title()
            )

            if user_move not in moves:
                print(
                    "Invalid input, please choose between (Rock, Paper, Scissors).\n "
                )
                continue
            # Computer's move and display moves in this round
            comp_move = random.choice(moves)
            print(f"Player played: {user_move}")
            print(f"Computer played: {comp_move}")
            # Determine winner
            if user_move == comp_move:
                print("It's a tie!")
            elif (
                (user_move == "Rock" and comp_move == "Scissors")
                or (user_move == "Paper" and comp_move == "Rock")
                or (user_move == "Scissors" and comp_move == "Paper")
            ):
                print("Player wins this round!")
                user_score += 1
            else:
                print("Computer wins this round!")
                comp_score += 1
        # Game over - display final result
        print("=" * 40)
        if user_score > comp_score:
            print(f"Player Won! {user_score} to {comp_score}")
        else:
            print(f"Computer Won! {user_score} to {comp_score}")
        print("=" * 40)
        # Play again?
        choice = input("Do you want to play again? (y/n): ").strip().lower()
        if choice not in ("y", "yes"):
            print("Thank you for playing!")
            break


if __name__ == "__main__":
    main()
