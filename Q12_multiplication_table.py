# Q12 - Multiplication Table Generator
# Generates multiplication table for a number

def main():
    try:
        number = int(input("Enter number: "))
        end_range = int(input("Enter range (end): "))

        if end_range <= 0:
            print("Range must be positive.")
            return

        print(f"\nMultiplication Table of {number}")
        for i in range(1, end_range + 1):
            print(f"{number} x {i} = {number * i}")

    except ValueError:
        print("Invalid input! Enter integers only.")
    except Exception as error:
        print("Error:", error)

if __name__ == "__main__":
    main()