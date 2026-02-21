# Q9 - Ticket Pricing System
# Calculates movie ticket price based on age and day

def main():
    try:
        age = int(input("Enter age: "))
        day = input("Enter day of week: ").strip().lower()
        number_of_tickets = int(input("Enter number of tickets: "))

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

        total_base = base_price * number_of_tickets

        # Day-based discount
        if day in ["friday", "saturday", "sunday"]:
            discount = 0.20 * total_base
        else:
            discount = 0

        final_price = total_base - discount

        print("\n=== TICKET BILL ===")
        print("Base Price per ticket:", base_price)
        print("Total Base Amount:", total_base)
        print("Discount:", discount)
        print("Final Amount:", final_price)

    except ValueError:
        print("Invalid input! Enter proper values.")
    except Exception as error:
        print("Error:", error)

if __name__ == "__main__":
    main()