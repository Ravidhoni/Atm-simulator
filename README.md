# ATM Simulator

This project is a simple ATM simulator implemented in Python. It allows users to perform basic banking operations such as checking balance, depositing funds, withdrawing funds, and viewing transaction history.

## Features

- **Check Balance**: View the current account balance.
- **Deposit Funds**: Add money to the account.
- **Withdraw Funds**: Withdraw money from the account, subject to available balance.
- **Transaction History**: View a list of all transactions performed during the session.

## Requirements

- Python 3.x

## How to Use

1. Clone this repository or download the `atm_simulator.py` file.
2. Open a terminal or command prompt.
3. Navigate to the directory where the `atm_simulator.py` file is located.
4. Run the script using the following command:
    ```sh
    python atm_simulator.py
    ```
5. Enter your PIN when prompted (default PIN is `1234`).
6. Choose from the menu options to perform various operations.

## Code Overview

### `ATM` Class

- `__init__(self, initial_balance=0)`: Initializes the ATM object with an initial balance and an empty transaction history.
- `authenticate(self, entered_pin)`: Checks if the entered PIN matches the predefined PIN.
- `check_balance(self)`: Prints the current balance.
- `deposit(self, amount)`: Adds the specified amount to the balance and logs the transaction.
- `withdraw(self, amount)`: Subtracts the specified amount from the balance if there are sufficient funds and logs the transaction. Logs a failed withdrawal attempt if there are insufficient funds.
- `show_transaction_history(self)`: Prints the list of all transactions. Informs the user if there are no transactions.

### `main` Function

Handles user interactions by presenting a menu and calling the appropriate methods based on user choices.

### Example Usage

```python
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
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Invalid PIN. Access denied.")

if __name__ == "__main__":
    main()
