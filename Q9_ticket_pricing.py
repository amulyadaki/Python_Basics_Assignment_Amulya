# Q9 - Ticket Pricing System
# Calculates movie ticket price based on age and day

def main():
    try:
        age = int(input("Enter age: "))
        day_of_week = input("Enter day of week: ").strip().lower()
        number_of_tickets = int(input("Enter number of tickets: "))

        # Validate ticket count
        if number_of_tickets <= 0:
            print("Number of tickets must be greater than 0.")
            return

        # Age-based pricing
        if age < 3:
            base_price = 0
        elif 3 <= age <= 12:
            base_price = 150
        elif 13 <= age <= 59:
            base_price = 300
        else:
            base_price = 200

        total_base_price = base_price * number_of_tickets

        # Weekend discount (20%)
        if day_of_week in ["friday", "saturday", "sunday"]:
            discount_amount = 0.20 * total_base_price
        else:
            discount_amount = 0

        final_amount = total_base_price - discount_amount

        # Display results
        print("\n=== TICKET BILL ===")
        print("Base Price per Ticket:", base_price)
        print("Total Base Price:", total_base_price)
        print("Discount:", discount_amount)
        print("Final Amount:", final_amount)

    except ValueError:
        print("Invalid input! Please enter correct values.")
    except Exception as error:
        print("Error:", error)


if __name__ == "__main__":
    main()