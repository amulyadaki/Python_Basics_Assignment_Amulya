# Q16 - Number Guessing Game
# The computer selects a random number between 1 and 100.
# The user gets 7 attempts to guess it.

import random

def main():
    best_score = None  # Stores minimum attempts taken across games

    while True:  # Allows replaying the game
        try:
            secret_number = random.randint(1, 100)
            attempts_remaining = 7
            attempts_used = 0

            print("\n=== NUMBER GUESSING GAME ===")
            print("Guess a number between 1 and 100")

            while attempts_remaining > 0:
                guess = int(input("Enter your guess: "))
                attempts_used += 1

                # Validating range
                if guess < 1 or guess > 100:
                    print("Please enter a number between 1 and 100.")
                    continue

                if guess == secret_number:
                    print(f"Correct! You guessed in {attempts_used} attempts.")

                    # Updating best score
                    if best_score is None or attempts_used < best_score:
                        best_score = attempts_used
                        print("New Best Score:", best_score)
                    break

                elif guess < secret_number:
                    print("Too low!")
                else:
                    print("Too high!")

                attempts_remaining -= 1
                print("Attempts remaining:", attempts_remaining)

            if attempts_remaining == 0:
                print("Game Over! The number was:", secret_number)

            play_again = input("Play again? (yes/no): ").lower()
            if play_again != "yes":
                break

        except ValueError:
            print("Invalid input! Enter integer only.")
        except Exception as error:
            print("Error:", error)


if __name__ == "__main__":
    main()