class ATM:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.transaction_history = []
        self.pin = "9346"  # Example PIN

    def authenticate(self, entered_pin):
        return self.pin == entered_pin

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: ${amount}")
        print(f"${amount} deposited successfully.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount}")
            print(f"${amount} withdrawn successfully.")
        else:
            print("Insufficient funds.")
            self.transaction_history.append(f"Failed withdrawal attempt: ${amount}")

    def show_transaction_history(self):
        print("Transaction History:")
        if not self.transaction_history:
            print("No transactions found.")
        else:
            for transaction in self.transaction_history:
                print(transaction)

def main():
    atm = ATM(initial_balance=1000)

    # Simulating a user interaction
    entered_pin = input("Enter your PIN: ")
    if atm.authenticate(entered_pin):
        while True:
            print("\nATM Menu:")
            print("1. Check Balance")
            print("2. Deposit Funds")
            print("3. Withdraw Funds")
            print("4. Transaction History")
            print("5. Exit")
            
            choice = input("Choose an option: ")
            
            if choice == '1':
                atm.check_balance()
            elif choice == '2':
                amount = float(input("Enter amount to deposit: "))
                atm.deposit(amount)
            elif choice == '3':
                amount = float(input("Enter amount to withdraw: "))
                atm.withdraw(amount)
            elif choice == '4':
                atm.show_transaction_history()
            elif choice == '5':
                print("Thank you for using the ATM. Have a Good Day!")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Invalid PIN. Access denied.")

if __name__ == "__main__":
    main()
