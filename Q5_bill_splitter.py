# Q5 - Bill Splitter
# Calculates total bill including tax and tip and splits among people

def main():
    try:
        total_bill = float(input("Enter total bill amount: "))
        number_of_people = int(input("Enter number of people: "))
        tax_percentage = float(input("Enter tax percentage: "))
        tip_percentage = float(input("Enter tip percentage: "))

        # Validation
        if number_of_people <= 0:
            print("Number of people must be greater than 0.")
            return

        # Tax calculation
        tax_amount = (tax_percentage / 100) * total_bill
        bill_after_tax = total_bill + tax_amount

        # Tip calculation on taxed amount
        tip_amount = (tip_percentage / 100) * bill_after_tax
        final_total = bill_after_tax + tip_amount

        # Per person calculation
        amount_per_person = final_total / number_of_people

        # Display
        print("\n=== BILL BREAKDOWN ===")
        print(f"Subtotal: ₹{total_bill:.2f}")
        print(f"Tax ({tax_percentage}%): ₹{tax_amount:.2f}")
        print(f"After tax: ₹{bill_after_tax:.2f}")
        print(f"Tip ({tip_percentage}%): ₹{tip_amount:.2f}")
        print(f"Total: ₹{final_total:.2f}")
        print(f"Per person: ₹{amount_per_person:.2f}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")
    except Exception as error:
        print("Error:", error)


if __name__ == "__main__":
    main()