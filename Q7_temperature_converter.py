# Q7 - Temperature Converter
# Menu-driven temperature conversion program

def main():
    while True:  # Loop allows multiple conversions
        try:
            print("\n=== TEMPERATURE CONVERTER ===")
            print("1. Celsius to Fahrenheit")
            print("2. Fahrenheit to Celsius")
            print("3. Celsius to Kelvin")
            print("4. Kelvin to Celsius")
            print("5. Fahrenheit to Kelvin")
            print("6. Kelvin to Fahrenheit")
            print("7. Exit")

            choice = int(input("Enter your choice: "))

            # Exit condition
            if choice == 7:
                print("Exiting program...")
                break

            temperature_value = float(input("Enter temperature value: "))

            # Conversion formulas
            if choice == 1:
                result = (temperature_value * 9/5) + 32
            elif choice == 2:
                result = (temperature_value - 32) * 5/9
            elif choice == 3:
                result = temperature_value + 273.15
            elif choice == 4:
                result = temperature_value - 273.15
            elif choice == 5:
                result = (temperature_value - 32) * 5/9 + 273.15
            elif choice == 6:
                result = (temperature_value - 273.15) * 9/5 + 32
            else:
                print("Invalid choice! Please select from menu.")
                continue

            print("Converted Temperature:", result)

        except ValueError:
            print("Invalid input! Please enter numeric values.")
        except Exception as error:
            print("Error:", error)


if __name__ == "__main__":
    main()