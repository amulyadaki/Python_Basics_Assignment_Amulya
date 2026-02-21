# Q16 - Number Guessing Game
# User gets 7 attempts to guess a random number

import random

def main():
    best_score = None

    while True:
        try:
            secret_number = random.randint(1, 100)
            attempts = 7
            attempts_used = 0

            print("\n=== NUMBER GUESSING GAME ===")
            print("Guess a number between 1 and 100")

            while attempts > 0:
                guess = int(input("Enter your guess: "))
                attempts_used += 1

                if guess < 1 or guess > 100:
                    print("Guess must be between 1 and 100.")
                    continue

                if guess == secret_number:
                    print(f"Correct! You guessed in {attempts_used} attempts.")
                    
                    if best_score is None or attempts_used < best_score:
                        best_score = attempts_used
                        print("New best score:", best_score)

                    break
                elif guess < secret_number:
                    print("Too low!")
                else:
                    print("Too high!")

                attempts -= 1
                print("Attempts remaining:", attempts)

            if attempts == 0:
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