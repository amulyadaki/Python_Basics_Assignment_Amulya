# Q20 - Number System Functions
# This program provides a menu-driven system
# to perform various mathematical operations.

# -----------------------------
# Mathematical Functions
# -----------------------------

def factorial(n):
    # Returns factorial using iterative approach
    if n < 0:
        return "Not defined for negative numbers"

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


def is_prime(n):
    # Checks if number is prime
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def fibonacci(n):
    # Returns nth Fibonacci number
    if n <= 0:
        return "Enter positive number"

    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b

    return b


def sum_of_digits(n):
    # Adds all digits of number
    return sum(int(digit) for digit in str(abs(n)))


def reverse_number(n):
    # Reverses digits of number
    return int(str(n)[::-1])


def is_armstrong(n):
    # Checks Armstrong number
    digits = str(n)
    power = len(digits)

    return n == sum(int(d) ** power for d in digits)


def gcd(a, b):
    # Uses Euclidean algorithm
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    # Uses GCD to calculate LCM
    return abs(a * b) // gcd(a, b)


def is_perfect_number(n):
    # Perfect number = sum of proper divisors equals number
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n


# -----------------------------
# Menu System
# -----------------------------

def math_menu():
    while True:
        try:
            print("\n=== NUMBER SYSTEM MENU ===")
            print("1. Factorial")
            print("2. Prime Check")
            print("3. Fibonacci")
            print("4. Sum of Digits")
            print("5. Reverse Number")
            print("6. Armstrong Number")
            print("7. GCD")
            print("8. LCM")
            print("9. Perfect Number")
            print("10. Exit")

            choice = int(input("Enter choice: "))

            if choice == 10:
                print("Exiting Program...")
                break

            if choice in [1,2,3,4,5,6,9]:
                num = int(input("Enter number: "))

            if choice == 1:
                print("Factorial:", factorial(num))
            elif choice == 2:
                print("Is Prime:", is_prime(num))
            elif choice == 3:
                print("Fibonacci:", fibonacci(num))
            elif choice == 4:
                print("Sum of Digits:", sum_of_digits(num))
            elif choice == 5:
                print("Reversed Number:", reverse_number(num))
            elif choice == 6:
                print("Armstrong:", is_armstrong(num))
            elif choice == 7:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                print("GCD:", gcd(a, b))
            elif choice == 8:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                print("LCM:", lcm(a, b))
            elif choice == 9:
                print("Perfect Number:", is_perfect_number(num))
            else:
                print("Invalid choice.")

        except ValueError:
            print("Invalid input! Enter integers only.")
        except Exception as error:
            print("Unexpected Error:", error)


if __name__ == "__main__":
    math_menu()