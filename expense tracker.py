import datetime
import json

# Function to load expense data from file
def load_expenses(file_name="expenses.json"):
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save expense data to file
def save_expenses(expenses, file_name="expenses.json"):
    with open(file_name, "w") as file:
        json.dump(expenses, file, indent=4)

# Function to add a new expense
def add_expense(amount, category, description):
    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": datetime.date.today().strftime("%Y-%m-%d")
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully.")

# Function to view expenses by month
def view_monthly_summary(month):
    monthly_expenses = [expense for expense in expenses if expense["date"].startswith(month)]
    if not monthly_expenses:
        print("No expenses found for this month.")
        return
    total = sum(exp["amount"] for exp in monthly_expenses)
    print(f"\nMonthly Summary for {month}:")
    print(f"Total spent: {total}")
    for exp in monthly_expenses:
        print(f"{exp['date']} - {exp['category']}: {exp['amount']} - {exp['description']}")

# Function to view expenses by category
def view_category_summary(category):
    category_expenses = [expense for expense in expenses if expense["category"] == category]
    if not category_expenses:
        print(f"No expenses found for the category '{category}'.")
        return
    total = sum(exp["amount"] for exp in category_expenses)
    print(f"\nCategory Summary for '{category}':")
    print(f"Total spent: {total}")
    for exp in category_expenses:
        print(f"{exp['date']} - {exp['amount']} - {exp['description']}")

# Load expenses data
expenses = load_expenses()

# User interface
def main():
    print("Welcome to the Expense Tracker")
    while True:
        print("\nOptions:")
        print("1. Add Expense")
        print("2. View Monthly Summary")
        print("3. View Category Summary")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                amount = float(input("Enter amount spent: "))
                category = input("Enter category (e.g., food, transportation, entertainment): ").lower()
                description = input("Enter a brief description: ")
                add_expense(amount, category, description)
            elif choice == 2:
                month = input("Enter the month (YYYY-MM): ")
                view_monthly_summary(month)
            elif choice == 3:
                category = input("Enter the category: ").lower()
                view_category_summary(category)
            elif choice == 4:
                print("Exiting the Expense Tracker. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()