# Q14 - Factorial Calculator
# Calculates factorial with step-by-step display

def main():
    try:
        number = int(input("Enter a number: "))

        if number < 0:
            print("Factorial not defined for negative numbers.")
            return
        elif number == 0:
            print("0! = 1")
            return

        factorial = 1
        steps = ""

        for i in range(number, 0, -1):
            factorial *= i
            steps += str(i)
            if i != 1:
                steps += " x "

        print(f"{number}! = {steps} = {factorial}")

    except ValueError:
        print("Invalid input! Enter integer only.")
    except Exception as error:
        print("Error:", error)

if __name__ == "__main__":
    main()