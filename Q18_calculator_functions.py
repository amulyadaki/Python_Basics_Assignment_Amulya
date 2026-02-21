# Q18 - Calculator using Functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero not allowed"
    return a / b

def modulus(a, b):
    if b == 0:
        return "Modulus by zero not allowed"
    return a % b

def power(a, b):
    return a ** b

def calculator():
    while True:
        try:
            print("\n=== FUNCTION CALCULATOR ===")
            print("1.Add 2.Subtract 3.Multiply 4.Divide 5.Modulus 6.Power 7.Exit")
            choice = int(input("Enter choice: "))

            if choice == 7:
                break

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

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
                print("Invalid choice.")

        except ValueError:
            print("Invalid input! Enter numeric values.")
        except Exception as error:
            print("Error:", error)

if __name__ == "__main__":
    calculator()