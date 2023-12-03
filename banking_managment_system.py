class Bank:
    def __init__(self):
        self.users = []
        self.loan_feature_enabled = True

    def toggle_loan_feature(self):
        self.loan_feature_enabled = not self.loan_feature_enabled
        print(f"Loan feature {'enabled' if self.loan_feature_enabled else 'disabled'}")
        
    def check_total_balance(self):
        total_balance = sum(user.balance for user in self.users)
        print(f"Total Balance in the bank: {total_balance}")

    def check_total_loan_amount(self):
        total_loan_amount = sum(user.balance for user in self.users if user.balance < 0)
        print(f"Total Loan Amount in the bank: {abs(total_loan_amount)}")


class User:
    def __init__(self, name, account_number, balance, pin):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.pin = pin
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited {amount}")
            print(f"Deposited {amount}. Your new balance is {self.balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        pin= int(input("Enter your pin : "))
        if self.pin!=pin:
            print("Wrong pin. please, try again...")
            return
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew {amount}")
            print(f"Withdrew {amount}. Your new balance is {self.balance}")
        else:
            print("Insufficient funds")

    def check_balance(self):
        print(f"Your available balance is {self.balance}")

    def transfer(self, amount, recipient):
        if amount > 0 and amount <= self.balance:
            recipient.balance += amount
            self.balance -= amount
            self.transaction_history.append(f"Transferred {amount} to {recipient.name}")
            recipient.transaction_history.append(f"Received {amount} from {self.name}")
            print(f"Transferred {amount} to {recipient.name}. Your new balance is {self.balance}")
        else:
            print("Insufficient funds")

    def check_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

    def take_loan(self):
        if bank.loan_feature_enabled:
            loan_amount = self.balance * 2
            self.balance += loan_amount
            self.transaction_history.append(f"Took a loan of {loan_amount}")
            print(f"Loan of {loan_amount} approved. Your new balance is {self.balance}")
        else:
            print("Loan feature is currently disabled")

    def pin_change(self):
        new_pin=int(input("Enter new pin : "))
        old_pin=int(input("Enter old pin : "))
        if self.pin==old_pin:
            self.pin=new_pin
            print("Pin change Successfully.")
        else:
            print("Your pin is Wrong. Try again, sir....")


class Admin:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def toggle_loan_feature(self):
        bank.toggle_loan_feature()


bank = Bank()
admin = Admin("Khaled Amin", "Khaled123Amin")


def signup():
    name = input("Enter your name: ")
    account_number = int(input("Enter your account number: "))
    balance = float(input("Enter your initial balance: "))
    pin = int(input("Create a 4-digit PIN: "))

    new_user = User(name, account_number, balance, pin)
    bank.users.append(new_user)
    print(f"User {name} created successfully\nBank account number is {account_number}")


def login():
    account_number = int(input("Enter your account number: "))
    pin = int(input("Enter your PIN: "))

    for user in bank.users:
        if user.account_number == account_number and user.pin == pin:
            print(f"Welcome back, {user.name}!")
            user_actions(user)
            break
    else:
        print("Invalid account number or PIN. Please try again.")


def user_actions(user):
    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Transfer\n5. Transaction History\n6. Take Loan\n7. Pin change  \n8. Logout")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = float(input("Enter deposit amount: "))
            user.deposit(amount)
        elif choice == 2:
            amount = float(input("Enter withdrawal amount: "))
            user.withdraw(amount)
        elif choice == 3:
            user.check_balance()
        elif choice == 4:
            recipient_account_number = int(input("Enter recipient's account number: "))
            recipient = next((u for u in bank.users if u.account_number == recipient_account_number), None)
            if recipient:
                amount = float(input("Enter transfer amount: "))
                user.transfer(amount, recipient)
            else:
                print("Recipient not found.")
        elif choice == 5:
            user.check_transaction_history()
        elif choice == 6:
            user.take_loan()
        elif choice == 7:
            user.pin_change()
        elif choice == 8:
            break
        else:
            print("Invalid choice. Please try again.")


def admin_actions():
    password = input("Enter admin password: ")
    if password == admin.password:
        while True:
            print("\n1. Toggle Loan Feature\n2. Check Total Balance\n3. Check Total Loan Amount\n4. Logout")
            admin_choice = int(input("Enter your choice: "))

            if admin_choice == 1:
                admin.toggle_loan_feature()
            elif admin_choice == 2:
                bank.check_total_balance()
            elif admin_choice == 3:
                bank.check_total_loan_amount()
            elif admin_choice == 4:
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Incorrect admin password. Access denied.")


def main():
    while True:
        print("\n1. User\n2. Admin\n3. Exit")
        role_choice = int(input("Enter your role: "))

        if role_choice == 1:
            print("\n1. Sign Up\n2. Log In\n3. Back")
            user_choice = int(input("Enter your choice: "))

            if user_choice == 1:
                signup()
            elif user_choice == 2:
                login()
            elif user_choice == 3:
                continue
            else:
                print("Invalid choice. Please try again.")
        elif role_choice == 2:
            admin_actions()
        elif role_choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
