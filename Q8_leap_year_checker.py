# Q8 - Leap Year Checker
# Checks whether a given year is a leap year

def main():
    try:
        year = int(input("Enter a year: "))

        # Leap year logic:
        # Divisible by 4 AND (Not divisible by 100 OR divisible by 400)
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            print(f"{year} is a Leap Year.")
            print("Reason: It satisfies leap year conditions.")
        else:
            print(f"{year} is NOT a Leap Year.")
            print("Reason: It does not satisfy leap year rules.")

    except ValueError:
        print("Invalid input! Please enter a valid year.")
    except Exception as error:
        print("Error:", error)


if __name__ == "__main__":
    main()