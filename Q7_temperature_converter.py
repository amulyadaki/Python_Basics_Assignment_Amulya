# Q7 - Temperature Converter
# Menu-driven temperature conversion program

def main():
    while True:
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

            if choice == 7:
                print("Exiting program...")
                break

            temperature = float(input("Enter temperature value: "))

            if choice == 1:
                result = (temperature * 9/5) + 32
                print("Converted Temperature:", result)

            elif choice == 2:
                result = (temperature - 32) * 5/9
                print("Converted Temperature:", result)

            elif choice == 3:
                result = temperature + 273.15
                print("Converted Temperature:", result)

            elif choice == 4:
                result = temperature - 273.15
                print("Converted Temperature:", result)

            elif choice == 5:
                result = (temperature - 32) * 5/9 + 273.15
                print("Converted Temperature:", result)

            elif choice == 6:
                result = (temperature - 273.15) * 9/5 + 32
                print("Converted Temperature:", result)

            else:
                print("Invalid choice! Please select from menu.")

        except ValueError:
            print("Invalid input! Please enter numeric values.")
        except Exception as error:
            print("Error:", error)

if __name__ == "__main__":
    main()