# Q11 - Number Pattern Printer
# Prints different number patterns based on user choice

def print_pattern_1(height):
    for i in range(1, height + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

def print_pattern_2(height):
    for i in range(1, height + 1):
        print(str(i) * i)

def print_pattern_3(height):
    for i in range(height, 0, -1):
        for j in range(i, 0, -1):
            print(j, end="")
        print()

def print_pattern_4(height):
    for i in range(1, height + 1):
        for j in range(1, i + 1):
            print(j, end="")
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()

def main():
    try:
        print("\n=== NUMBER PATTERN PRINTER ===")
        print("1. Pattern 1")
        print("2. Pattern 2")
        print("3. Pattern 3")
        print("4. Pattern 4")

        choice = int(input("Choose pattern: "))
        height = int(input("Enter height: "))

        if height <= 0:
            print("Height must be positive.")
            return

        if choice == 1:
            print_pattern_1(height)
        elif choice == 2:
            print_pattern_2(height)
        elif choice == 3:
            print_pattern_3(height)
        elif choice == 4:
            print_pattern_4(height)
        else:
            print("Invalid choice.")

    except ValueError:
        print("Invalid input! Enter numeric values.")
    except Exception as error:
        print("Error:", error)

if __name__ == "__main__":
    main()