#MySql based project
import mysql.connector                           # import mysql.connector for expense tracker project

myexp = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "expense_tracker"
)

mycursor = myexp.cursor()

#  add expense
def add_expense():                                    # add new expense to the expenses list
    print("\n---Add Expense---")                              # print the add expense header

    date = input("Enter Date(YYYY-MM-DD): ")                  # get the date from the user

    try:                                                      #get the amount from the user and convert it to float
        amount = float(input("Enter Amount: "))               # get the amount from the user and convert it to float
    except ValueError:                                        # if the user enters an invalid amount
        print("❌ Invalid Amount")                            # print invalid amount message
        return                                                #return from the function
    
    category = input(
        "Enter Category\n(Food / Travel / Medical / Others): "
        ).capitalize()                                        # get the categoty from the user and capitalize the first letter
    if category not in ["Food", "Medical", "Travel", "Others"]:
        category = "Others"                                   # if the category not in the list set it to others
    
    note = input("Enter Note (Optional): ")                   # get the note from the user

    exp = """    
    INSERT INTO expenses (date, amount, category, note)
    VALUES (%S, %S, %S, %S)
    """                                                       #insert the data for expenses database and assign the value using INSERT statement and injuction methed
    value = ("date", "amount", "category", "note")            #assign the user input values
    mycursor.execute(exp, value)                              #execute the mysql insert statement
    myexp.commit()                                            # save the data permanetly

    print("✅ The Expense Added Successfully")                # print the success message

# view expenses
def view_expenses():                                          # view all expenses from the database
    print("\n---View all Expenses---")                        # print the view expenses header

    mycursor.execute("SELECT date, amount, category, note FROM expenses")     #execute the mysql SELECT query 
    rows = mycursor.fetchall()                                #fetch all data thet means call all data and store the row

    if not rows:                                              # check the database for is an empty
        print("No Expenses Found")                            #if empty print no expenses found
        return                                                #if else stop the if stament and return the print statement
    
    print("Date       Amount     Category     Note")          # print the headerfor the expenses table
    print("---------------------------------------")
    for row in rows:                                          # iterate through each row from the rows list
        print(f"{row[0]}  {row[1]}  {row[2]}  {row[3]} ")     # print the expense detsils

# view total expense
def view_total():                                             #view total expense from the expenses table
    print("---View Total Expense---")                         # print the total expense header

    mycursor.execute("SELECT SUM(amount) FROM expenses")      #execute the select statement 
    total = mycursor.fetchone()[0]                            #fetch one line only and store in total variable

    if total is None:                           #if total is empty 
        print("No Expenses Found")              #print no expenses found
    else:                                       #if total is not empty
        print("Total Expense: {total}")         #print total expenses total

# category-wise summary
def category_wise_summary():                    # view category wise summary from the expenses table
    print("---Category-wise Summary---")        # print header

    mycursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")      #execute the select statement and sum the category in amount
    rows = mycursor.fetchall()                  #fetching all data in expenses table

    if not rows:                                # check if expenses table is empty
        print("NO Expenses Found")              # if empty when print no expenses found
        return                                  #exit the if statement and return the value

    for cat, amt in rows:                       # iterate through each category and amount in the rows
        print(f"{cat} : {amt}")                 # print the category and amount

# main program loop
while True:                                     # main program loop
    print("""
          --- Expense Tracker Menu (Choose Number Only) ---
          "1. Add Expense
          "2. View all Expenses
          "3. View Total Expense
          "4. Category-wise Summary
          "5. Exit
          """)                                 # print the menu options

    choice = input("Enter Choice: ")           # get the choice from the user

    if choice == "1":
        add_expense()                          # add new expense table
    elif choice == "2":
        view_expenses()                        # view all expensestable
    elif choice == "3":
        view_total()                           # view total expensetable
    elif choice == "4":
        category_wise_summary()                # view category wise summary
    elif choice == "5":
        print("""
              📁 Expenses saved successfully.
              Exiting Expense Tracker. Goodbye!
              """)                             # print save and exit message
        break                                  # exit the program
    else:
        print("❌ Invalid choice! Please select 1 to 5.")      #print invalid choice message for wrong input

mycursor.close()
myexp.close()