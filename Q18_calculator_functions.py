# Q18 - Calculator Using Functions
# This program demonstrates modular programming.
# Each mathematical operation is written as a separate function.
# The main calculator function calls these based on user choice.

# -----------------------------
# Arithmetic Operation Functions
# -----------------------------

def add(a, b):
    # Returns sum of two numbers
    return a + b


def subtract(a, b):
    # Returns difference of two numbers
    return a - b


def multiply(a, b):
    # Returns product of two numbers
    return a * b


def divide(a, b):
    # Checks for division by zero
    if b == 0:
        return "Error: Division by zero not allowed"
    return a / b


def modulus(a, b):
    # Returns remainder of division
    if b == 0:
        return "Error: Modulus by zero not allowed"
    return a % b


def power(a, b):
    # Returns a raised to the power b
    return a ** b


# -----------------------------
# Main Calculator Function
# -----------------------------

def calculator():
    while True:  # Loop keeps calculator running until user exits
        try:
            print("\n=== FUNCTION CALCULATOR ===")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Modulus")
            print("6. Power")
            print("7. Exit")

            choice = int(input("Enter your choice: "))

            # Exit condition
            if choice == 7:
                print("Exiting Calculator...")
                break

            # Taking numeric inputs
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # Calling respective function
            if choice == 1:
                print("Result:", add(num1, num2))
            elif choice == 2:
                print("Result:", subtract(num1, num2))
            elif choice == 3:
                print("Result:", multiply(num1, num2))
            elif choice == 4:
                print("Result:", divide(num1, num2))
            elif choice == 5:
                print("Result:", modulus(num1, num2))
            elif choice == 6:
                print("Result:", power(num1, num2))
            else:
                print("Invalid choice! Please select 1–7.")

        except ValueError:
            # Handles non-numeric input
            print("Invalid input! Please enter numbers only.")
        except Exception as error:
            print("Unexpected Error:", error)


# Ensures program runs only when file is executed directly
if __name__ == "__main__":
    calculator()