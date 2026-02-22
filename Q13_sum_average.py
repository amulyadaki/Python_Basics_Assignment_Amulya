# Q13 - Sum and Average Calculator
# Calculates sum, average, maximum, and minimum from user input numbers

def main():
    try:
        count = int(input("How many numbers? "))

        if count <= 0:
            print("Count must be positive.")
            return

        numbers = []

        # Collecting numbers from user
        for i in range(count):
            value = float(input(f"Enter number {i+1}: "))
            numbers.append(value)

        total_sum = sum(numbers)
        average = total_sum / count
        maximum = max(numbers)
        minimum = min(numbers)

        # Display results
        print("\n=== RESULTS ===")
        print("Sum:", total_sum)
        print("Average:", average)
        print("Maximum:", maximum)
        print("Minimum:", minimum)

    except ValueError:
        print("Invalid input! Enter numeric values.")
    except Exception as error:
        print("Error:", error)


if __name__ == "__main__":
    main()