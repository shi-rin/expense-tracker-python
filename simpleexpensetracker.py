#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Start by greeting the user
print("Welcome to Shirin's Simple Expense Tracker 💸")

#This file will save your income & expenses
filename = "transactions.txt"

#Function to add a transaction
def add_transaction():
    type = input("Enter type (income/expense): ").strip().lower()
    amount = float(input("Enter amount (e.g., 1000): "))
    note = input("Write a short note (optional): ")

    with open(filename, "a") as file:
        file.write(f"{type},{amount},{note}\n")
    
    print("✅ Saved!")

#Function to view all entries and total
def show_summary():
    income = 0
    expense = 0
    print("\n--- 📃 Transaction Summary ---")
    
    try:2
        2
        with open(filename, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == "income":
                    income += float(data[1])
                elif data[0] == "expense":
                    expense += float(data[1])
                print(f"{data[0].title():<10} | ₹{data[1]} | {data[2]}")
    except FileNotFoundError:
        print("No transactions found.")

    print(f"\nTotal Income: ₹{income}")
    print(f"Total Expenses: ₹{expense}")
    print(f"🟢 Balance: ₹{income - expense}")

#Main program loop
while True:
    print("\nChoose an option:")
    print("1. Add Income/Expense")
    print("2. Show Summary")
    print("3. Exit")

    choice = input("Enter choice (1/2/3): ")
    
    if choice == "1":
        add_transaction()
    elif choice == "2":
        show_summary()
    elif choice == "3":
        print("Thank you for using the tracker. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")

