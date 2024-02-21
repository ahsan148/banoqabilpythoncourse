
#Easy Khaata

expenses = []  # This list will store our expenses
total_balance = 0  # This will keep track of our total balance

# Function to add an expense
def add_expense(date, description, amount):
    global total_balance
    if total_balance < float(amount):
        print("Insufficient balance! Cannot add expense. To apply for loan download our app 'Easy Loan' ")
        return
    expense = {'date': date, 'description': description, 'amount': amount}
    expenses.append(expense)
    total_balance -= float(amount)
    print("Expense added successfully!")
    print(f"Remaining balance: {total_balance}")

# Function to view expenses
def view_expenses():
    if not expenses:
        print("Your Khaata is empty enter add to add your expenses.")
    else:
        print("Your expenses:")
        for expense in expenses:
            print(f"Date: {expense['date']}, Description: {expense['description']}, Amount: {expense['amount']}")
    print(f"Remaining balance: {total_balance}")

# Function to get user input
def get_user_input():
    return input("Enter 'add' to add an expense, 'view' to view expenses, or 'exit' to exit: ")

# Function to set total balance
def set_total_balance():
    global total_balance
    total_balance = float(input("Enter your total amount: "))

# Main function
def main():
    set_total_balance()
    print(f"Your total balance: {total_balance}")
    while True:
        user_choice = get_user_input()

        if user_choice == 'add':
            date = input("Enter the date: ")
            description = input("Enter the expense description: ")
            amount = input("Enter the expense amount: ")
            add_expense(date, description, amount)

        elif user_choice == 'view':
            view_expenses()

        elif user_choice == 'exit':
            print("Exiting Easy Khaata. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 'add', 'view', or 'exit'.")

if __name__ == "__main__":
    main()