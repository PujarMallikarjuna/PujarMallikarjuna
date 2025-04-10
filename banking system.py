import json
import os

# File to store account data
DATA_FILE = "accounts.json"

# Load accounts from file or initialize empty
def load_accounts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    else:
        return {}

# Save accounts to file
def save_accounts(accounts):
    with open(DATA_FILE, "w") as file:
        json.dump(accounts, file, indent=4)

# Create a new account
def create_account(accounts):
    name = input("Enter your name: ")
    account_number = input("Enter a new account number: ")
    if account_number in accounts:
        print("⚠️ Account number already exists!")
        return
    accounts[account_number] = {
        "name": name,
        "balance": 0.0
    }
    print(f"✅ Account created for {name}.")
    save_accounts(accounts)

# Deposit money
def deposit(accounts):
    account_number = input("Enter your account number: ")
    if account_number not in accounts:
        print("❌ Account not found.")
        return
    amount = float(input("Enter amount to deposit: "))
    accounts[account_number]["balance"] += amount
    print(f"✅ Deposited ${amount:.2f}. New Balance: ${accounts[account_number]['balance']:.2f}")
    save_accounts(accounts)

# Withdraw money
def withdraw(accounts):
    account_number = input("Enter your account number: ")
    if account_number not in accounts:
        print("❌ Account not found.")
        return
    amount = float(input("Enter amount to withdraw: "))
    if amount > accounts[account_number]["balance"]:
        print("⚠️ Insufficient balance.")
        return
    accounts[account_number]["balance"] -= amount
    print(f"✅ Withdrawn ${amount:.2f}. New Balance: ${accounts[account_number]['balance']:.2f}")
    save_accounts(accounts)

# Check balance
def check_balance(accounts):
    account_number = input("Enter your account number: ")
    if account_number not in accounts:
        print("❌ Account not found.")
        return
    balance = accounts[account_number]["balance"]
    print(f"💰 Account Balance for {accounts[account_number]['name']}: ${balance:.2f}")

# Main menu
def main():
    accounts = load_accounts()
    while True:
        print("\n📋 Welcome to Banking System")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")
        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            deposit(accounts)
        elif choice == "3":
            withdraw(accounts)
        elif choice == "4":
            check_balance(accounts)
        elif choice == "5":
            print("👋 Thank you for using Python Bank!")
            break
        else:
            print("❌ Invalid choice. Please choose between 1-5.")

if __name__ == "__main__":
    main()
