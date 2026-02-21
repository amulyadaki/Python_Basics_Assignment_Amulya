# Q15 - Prime Number Checker
# Checks if a number is prime and finds primes in range

def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for i in range(3, int(number ** 0.5) + 1, 2):
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

        start = int(input("\nEnter start range: "))
        end = int(input("Enter end range: "))

        print("Prime numbers in range:")
        primes = [str(n) for n in range(start, end + 1) if is_prime(n)]
        print(", ".join(primes))

    except ValueError:
        print("Invalid input! Enter integers only.")
    except Exception as error:
        print("Error:", error)

if __name__ == "__main__":
    main()