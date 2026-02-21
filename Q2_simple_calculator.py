# Q2: Simple Calculator
# This program performs basic arithmetic operations

try:
    # Taking user input
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))

    print("\nResults:")

    print(f"{first_number} + {second_number} = {first_number + second_number}")
    print(f"{first_number} - {second_number} = {first_number - second_number}")
    print(f"{first_number} * {second_number} = {first_number * second_number}")

    # Handling division by zero
    if second_number != 0:
        print(f"{first_number} / {second_number} = {round(first_number / second_number, 2)}")
        print(f"{first_number} % {second_number} = {first_number % second_number}")
    else:
        print("Division and modulus not possible (division by zero).")

    print(f"{first_number} ^ {second_number} = {first_number ** second_number}")

except ValueError:
    print("Invalid input! Please enter numeric values only.")