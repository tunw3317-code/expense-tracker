expenses = []
def save_date():
    with open("expenses.txt", "w") as f:
        for item, amount in expenses:
            f.write(f"{item},{amount}\n")
def load_data():
    try:
        with open("expenses.txt", "r") as f:
            for line in f:
                item, amount = line.strip().split(",")
                expenses.append((item, float(amount)))
    except:
        pass
load_data()
while True:
    print("\n1===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Exit")
    choice = input("Choose: ")
    if choice =="1":
        item = input("Enter item name: ")
        amount = float(input("Enter amount: "))
        expenses.append((item, amount))
        save_date()
        print("Saved!")
    elif choice == "2":
        print("\n--- Expense List ---")
        total = 0
        for item, amount in expenses:
            print(item, "-", amount)
            total += amount
        print("Total =", total)
    elif choice == "3":
        print("Bye!")
        break
    else:
        print("Invalid choice")

