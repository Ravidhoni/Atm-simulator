class ATM:
    def __init__(self, balance=0):
        self.balance = balance
        self.pin = 9346
        sel.transaction_history = []

    def aunthenticate(self,entered_pin):
        return self.pin = entered_pin

    def check_balance(self):
        return f" your balance= ${self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return  f"Deposited {amount} successfully. New balance: {self.balance}"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrawn {amount} successfully. New balance: {self.balance}"
        else:
            return "Insufficient funds"

def show_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

# Main program
def main():
    atm = ATM(1000)  # Starting balance of 1000
    if atm.authenticate(entered_pin):
        while True:
            print("ATM Simulator")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. transaction history")
            print("5. quit")
    
            choice = input("Enter your choice (1-4): ")
    
            if choice == "1":
                balance = atm.check_balance()
                print(balance)
            elif choice == "2":
                amount = float(input("Enter the amount to deposit: "))
                result = atm.deposit(amount)
                print(result)
            elif choice == "3":
                amount = float(input("Enter the amount to withdraw: "))
                result = atm.withdraw(amount)
                print(result)
            elif choice == "4":
                atm.show_transaction_history()
            elif choice == "5":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("you entered invalid pin")
    
if __name__ == "__main__":
    main()
