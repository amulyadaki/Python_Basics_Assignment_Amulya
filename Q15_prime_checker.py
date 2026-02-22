# Q15 - Prime Number Checker
# Part 1: Checks if a number is prime
# Part 2: Finds all prime numbers within a range

def is_prime(number):
    # Prime numbers are greater than 1
    if number <= 1:
        return False

    # Checking divisibility from 2 to square root of number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


def main():
    try:
        number = int(input("Enter a number: "))

        if is_prime(number):
            print(f"{number} is a PRIME number.")
        else:
            print(f"{number} is NOT a prime number.")

        # Range input
        start = int(input("\nEnter start range: "))
        end = int(input("Enter end range: "))

        print("Prime numbers in range:")
        prime_list = []

        for n in range(start, end + 1):
            if is_prime(n):
                prime_list.append(str(n))

        print(", ".join(prime_list))

    except ValueError:
        print("Invalid input! Enter integers only.")
    except Exception as error:
        print("Error:", error)


if __name__ == "__main__":
    main()