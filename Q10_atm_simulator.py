# Q10 - Simple ATM Simulator
# Simulates basic ATM operations

def main():
    balance = 10000  # Initial balance

    while True:
        try:
            print("\n=== ATM SIMULATOR ===")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")

            choice = int(input("Enter choice: "))

            if choice == 1:
                print("Current Balance: ₹", balance)

            elif choice == 2:
                deposit_amount = float(input("Enter amount to deposit: "))
                if deposit_amount <= 0:
                    print("Deposit amount must be positive.")
                else:
                    balance += deposit_amount
                    print("Deposit successful! New balance: ₹", balance)

            elif choice == 3:
                withdraw_amount = float(input("Enter amount to withdraw: "))
                if withdraw_amount <= 0:
                    print("Withdrawal amount must be positive.")
                elif balance - withdraw_amount < 500:
                    print("Minimum balance of ₹500 must remain.")
                else:
                    balance -= withdraw_amount
                    print("Withdrawal successful! New balance: ₹", balance)

            elif choice == 4:
                print("Thank you for using ATM.")
                break

            else:
                print("Invalid choice! Select from menu.")

        except ValueError:
            print("Invalid input! Enter numeric values.")
        except Exception as error:
            print("Error:", error)

if __name__ == "__main__":
    main()