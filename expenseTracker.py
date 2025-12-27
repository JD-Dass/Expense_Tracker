Expenses_File = "expenses.txt"

def load_expenses():
    expenses = []

    try:
        with open(Expenses_File, "r") as file:
            for line in file:
                line = line.strip()
                if line == "" or line.startswith("Date") or line.startswith("-"):
                    continue
                
                date, amount, category, note = line.split("|")
                expense = {
                    "Date" : date.strip(),
                    "Amount" : float(amount.strip()),
                    "Category" : category.strip(),
                    "Note" : note.strip()
                }

                expenses.append(expense)                    
    except FileNotFoundError :
        pass

    return expenses


def add_expense():
    print("---Add Expense---")

    date = input("Enter The Date(YYYY-MM-DD): ")

    try:
        amount = float(input("Enter The Amount: "))
    except:
        print("Invalid Amount")
        return
    
    category = input("Enter The Category\n(Food / Travel / Medical / Others): ").capitalize()

    if category not in ["Food", "Medical", "Travel", "Others"]:
        category = "Others"
    
    note = input("Enter The Note (Optional): ")

    expense = {
        "Date" : date,
        "Amount" : amount,
        "Category" : category,
        "Note" : note
    }
        
    expenses.append(expense)
    print("The Expense Saveed Successfully... ")

def view_expenses():
    print("---View all Expenses---")
    if len(expenses) == 0:
        print("NO Expenses Found")
        return
    
    print("Date     | Amount   | Category   | Note\n")
    print("---------------------------------------\n")
    for exp in expenses:
        print(f"{exp['Date']} | {exp['Amount']} | {exp['Category']} | {exp['Note']} ")



def view_total(expenses):
    print("---View Total Expense---")
    if len(expenses) == 0:
        print("NO Expenses Found")
        return
    
    total = 0
    for expense in expenses:
        total += expense["Amount"]
    print(f"Total Expense: {total}")


def category_wise_summary():
    print("---Category-wise Summary---")
    if len(expenses) == 0:
        print("NO Expenses Found")
        return
    
    summary = {
        "Food" : 0,
        "Travel" : 0,
        "Medical" : 0,
        "Others" : 0
    }

    for exp in expenses:
        category = exp["Category"]
        amount = exp["Amount"]

        if category in summary:
            summary[category] += amount
        else:
            summary["Others"] += amount
    
    for category, total in summary.items():
        print(f"{category} : {total}")


def save_expenses(expenses):
    with open(Expenses_File, "w") as file:
        file.write("Date       | Amount   | Category  | Note\n")
        file.write("----------------------------------------\n")
        for exp in expenses:
            file.write(f"{exp['Date']} | {exp['Amount']} | {exp['Category']} | {exp['Note']}\n")
        print("Expenses save successfully. Existing...")



expenses = load_expenses()

while True:
    print("\n--- Expense Tracker Menu (Choose Number Only) ---")
    print("1. Add Expense")
    print("2. View all Expenses")
    print("3. View Total Expense")
    print("4. Category-wise Summary")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        view_total(expenses)
    elif choice == "4":
        category_wise_summary()
    elif choice == "5":
        save_expenses(expenses)
        break
    else:
        print("Invalid choice! Please select 1 to 5.")