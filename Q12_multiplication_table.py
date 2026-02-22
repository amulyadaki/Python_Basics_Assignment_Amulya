# Q12 - Multiplication Table
# This program prints the multiplication table
# of a given number from 1 to 10.

def main():
    try:
        number = int(input("Enter a number: "))

        print("\n=== MULTIPLICATION TABLE ===\n")

        # Loop runs from 1 to 10
        for i in range(1, 11):
            result = number * i
            print(f"{number} x {i} = {result}")

    except ValueError:
        print("Invalid input! Please enter an integer.")
    except Exception as error:
        print("Unexpected Error:", error)


if __name__ == "__main__":
    main()