# Q10 - ATM Simulator
# This program simulates basic ATM operations:
# 1. Check Balance
# 2. Deposit Money
# 3. Withdraw Money
# 4. Exit

def atm_simulator():
    balance = 10000  # Initial account balance

    while True:
        try:
            print("\n=== ATM MENU ===")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = int(input("Enter your choice: "))

            # -------------------------
            # Option 1: Check Balance
            # -------------------------
            if choice == 1:
                print("Current Balance: ₹", balance)

            # -------------------------
            # Option 2: Deposit Money
            # -------------------------
            elif choice == 2:
                amount = float(input("Enter amount to deposit: ₹"))

                if amount <= 0:
                    print("Deposit amount must be positive.")
                else:
                    balance += amount
                    print("Deposit Successful!")
                    print("Updated Balance: ₹", balance)

            # -------------------------
            # Option 3: Withdraw Money
            # -------------------------
            elif choice == 3:
                amount = float(input("Enter amount to withdraw: ₹"))

                if amount <= 0:
                    print("Withdrawal amount must be positive.")
                elif amount > balance:
                    print("Insufficient balance!")
                else:
                    balance -= amount
                    print("Withdrawal Successful!")
                    print("Remaining Balance: ₹", balance)

            # -------------------------
            # Option 4: Exit
            # -------------------------
            elif choice == 4:
                print("Thank you for using the ATM.")
                break

            else:
                print("Invalid choice! Please select 1–4.")

        except ValueError:
            print("Invalid input! Please enter numeric values.")
        except Exception as error:
            print("Unexpected Error:", error)


if __name__ == "__main__":
    atm_simulator()