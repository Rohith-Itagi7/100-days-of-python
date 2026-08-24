class BankAccount:
    def __init__(self, account_number, name, balance):
        self.__account_number = account_number
        self.__name = name
        self.__balance = balance

    # Getter methods
    def get_account_number(self):
        return self.__account_number

    def get_name(self):
        return self.__name

    def get_balance(self):
        return self.__balance

    # Deposit
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    # Normal withdrawal
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def display_account(self):
        print("\n--- Account Details ---")
        print(f"Account Number: {self.__account_number}")
        print(f"Name: {self.__name}")
        print(f"Balance: ₹{self.__balance}")


# Savings Account
class SavingsAccount(BankAccount):

    def __init__(self, account_number, name, balance, interest_rate):
        super().__init__(account_number, name, balance)
        self.interest_rate = interest_rate
    def calculate_interest(self):
        interest = self.get_balance() * self.interest_rate / 100

        print(f"Interest earned: ₹{interest}")


# Current Account
class CurrentAccount(BankAccount):

    def __init__(self, account_number, name, balance, overdraft_limit):
        super().__init__(account_number, name, balance)
        self.overdraft_limit = overdraft_limit

    # Overriding withdraw()
    def withdraw(self, amount):

        if amount > 0 and amount <= self.get_balance() + self.overdraft_limit:
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Overdraft limit exceeded.")


# Dictionary to store accounts
accounts = {}


while True:

    print("\n===== BANKING SYSTEM =====")

    print("1. Create Savings Account")
    print("2. Create Current Account")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Check Balance")
    print("6. Calculate Interest")
    print("7. Display Account Details")
    print("8. Exit")

    choice = int(input("Enter your choice: "))


    # Create Savings Account
    if choice == 1:
        account_number = input("Enter account number: ")
        if account_number in accounts:
            print("Account already exists.")

        else:
            name = input("Enter name: ")
            balance = float(input("Enter initial balance: "))
            interest_rate = float(input("Enter interest rate: "))

            account = SavingsAccount(
                account_number,
                name,
                balance,
                interest_rate
            )

            accounts[account_number] = account

            print("Savings Account created successfully!")

    # Create Current Account
    elif choice == 2:

        account_number = input("Enter account number: ")

        if account_number in accounts:
            print("Account already exists.")

        else:
            name = input("Enter name: ")
            balance = float(input("Enter initial balance: "))
            overdraft_limit = float(input("Enter overdraft limit: "))

            account = CurrentAccount(
                account_number,
                name,
                balance,
                overdraft_limit
            )

            accounts[account_number] = account

            print("Current Account created successfully!")


    # Deposit
    elif choice == 3:
        account_number = input("Enter account number: ")
        if account_number in accounts:
            amount = float(input("Enter amount to deposit: "))
            accounts[account_number].deposit(amount)
        else:
            print("Account not found.")


    # Withdraw
    elif choice == 4:
        account_number = input("Enter account number: ")
        if account_number in accounts:
            amount = float(input("Enter amount to withdraw: "))
            accounts[account_number].withdraw(amount)
        else:
            print("Account not found.")


    # Check Balance
    elif choice == 5:
        account_number = input("Enter account number: ")
        if account_number in accounts:
            balance = accounts[account_number].get_balance()
            print(f"Current Balance: ₹{balance}")

        else:
            print("Account not found.")


    # Calculate Interest
    elif choice == 6:
        account_number = input("Enter account number: ")
        if account_number in accounts:
            account = accounts[account_number]
            if isinstance(account, SavingsAccount):
                account.calculate_interest()
            else:
                print("Interest is only available for Savings Accounts.")

        else:
            print("Account not found.")


    # Display Details
    elif choice == 7:
        account_number = input("Enter account number: ")
        if account_number in accounts:
            accounts[account_number].display_account()
        else:
            print("Account not found.")


    # Exit
    elif choice == 8:
        print("Thank you for using the Banking System!")
        break
    else:
        print("Invalid choice.")
