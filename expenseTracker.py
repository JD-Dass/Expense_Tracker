import csv
import os

EXPENSES_FILE = "expenses.csv"   # file to store expenses and create the csv file

# Load expenses
def load_expenses():  # load expenses from the csv file
    expenses = []  #list to store expenses

    if not os.path.exists(EXPENSES_FILE):  # check if file exists
        return expenses  #returs empty list if file dose not exists
    
    with open(EXPENSES_FILE, "r", newline = "") as file:  #open the file in read mode with new line as a empty string
        reader = csv.DictReader(file)  #read the file as a dictionary and store the data in reader variable
        for row in reader:    #iterate through each row in the reader
            row["Amount"] = float(row["Amount"])   #conver the amount from string to float
            expenses.append(row)   # append the row to the expenses list
    return expenses  # return the expenses list

# save expenses
def save_expenses(expenses):   # save expenses to the csv file
    with open(EXPENSES_FILE, "w", newline="") as file:   # open the file in the write mode and newline as empty string
        fieldnames = ["Date", "Amount", "Category", "Note"]   # create the column names for the csv file
        writer = csv.DictWriter(file, fieldnames = fieldnames)   # create a csv dictionary writer object

        writer.writeheader()  # write the header to the csv file
        for expense in expenses:   # iterate through each expense in the expenses list 
            writer.writerow(expense)   #write the expense to the csv file

#  add expense
def add_expense(expenses):   # add new expense to the expenses list
    print("\n---Add Expense---")   # print the add expense header

    date = input("Enter Date(YYYY-MM-DD): ")   # get the date from the user

    try:  #get the amount from the user and convert it to float
        amount = float(input("Enter Amount: "))   # get the amount from the user and convert it to float
    except ValueError:   # if the user enters an invalid amount
        print("❌ Invalid Amount")   # print invalid amount message
        return   #return from the function
    
    category = input("Enter Category\n(Food / Travel / Medical / Others): ").capitalize()   # get the categoty from the user and capitalize the first letter
    if category not in ["Food", "Medical", "Travel", "Others"]:
        category = "Others"   # if the category not in the list set it to others
    
    note = input("Enter Note (Optional): ")   # get the note from the user

    expense = {   # create a new expense dictionary
        "Date" : date,
        "Amount" : amount,
        "Category" : category,
        "Note" : note
    }
    expenses.append(expense)   # append the new expense to the expenses list
    print("✅ The Expense Add Successfully")   # print the success message

    save_expenses(expenses)   # save the expenses to the csv file

# view expenses
def view_expenses(expenses):   # view all expenses from the expenses list
    print("\n---View all Expenses---")   # print the view expenses header
    if not expenses:   # check if the expenses list is empty
        print("NO Expenses Found")   # print no expenses found message for empty list
        return   # return from the function
    
    print("Date       Amount     Category     Note")   # print the headerfor the expenses table
    print("---------------------------------------")
    for exp in expenses:   # iterate through each exp from the expenses list
        print(f"{exp['Date']}  {exp['Amount']}  {exp['Category']}  {exp['Note']} ")   # print the expense detsils

# view total expense
def view_total(expenses):   #view total expense from the expenses list
    print("---View Total Expense---")   # print the biew total expense header
    if not expenses:   # check if the expenses list is empty
        print("NO Expenses Found")   #print no expenses found message for empty list
        return   # return from the function
    
    total = sum(exp["Amount"] for exp in expenses)   # calculate the total expense by summing up the amount of each expense in the expenses list
    print(f"\n💰 Total Expense: {total}")   # print the total expense

# category-wise summary
def category_wise_summary(expenses):   # view category wise summary from the expenses list
    print("---Category-wise Summary---")   # print header
    if not expenses:   # check if teh expenses list is empty
        print("NO Expenses Found")
        return
    
    summary = {   # create a summery dictionary to store the total amount for each category
        "Food" : 0,
        "Travel" : 0,
        "Medical" : 0,
        "Others" : 0
    }

    for exp in expenses:   # iterate through each expense in the expenses list
        summary[exp["Category"]] += exp["Amount"]    # add the amount to the respective category in the summery dictionary

    for cat, amt in summary.items():   # iterate through each category and amount in the summery dictionary
        print(f"{cat} : {amt}")   # print the category and amount

# main program loop
expenses = load_expenses()   # load the expenses from the csv file

while True:   # main program loop
    print("""
          --- Expense Tracker Menu (Choose Number Only) ---
          "1. Add Expense
          "2. View all Expenses
          "3. View Total Expense
          "4. Category-wise Summary
          "5. Exit
          """)   # print the menu options

    choice = input("Enter Choice: ")   # get the choice from the user

    if choice == "1":
        add_expense(expenses)  # add new expense
    elif choice == "2":
        view_expenses(expenses)   # view all expenses
    elif choice == "3":
        view_total(expenses)   # view total expense
    elif choice == "4":
        category_wise_summary(expenses)   # view category wise summary
    elif choice == "5":
        save_expenses(expenses)   # save expenses to the csv file
        print("""
              📁 Expenses saved successfully.
              Exiting Expense Tracker. Goodbye!
              """)    # print save and exit message
        break   # exit the program
    else:
        print("❌ Invalid choice! Please select 1 to 5.")   #print invalid choice message for wrong input