"""

Initial Balance 100000
1. Withdraw
2. Deposit
3. Balance Check
4. EXit
Enter Choice
"""

initial_balance = 100000
balance = initial_balance

while True:
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Balance Check")
    print("4. Exit")
    
    choice = int(input("Enter your Choice"))
        
    if choice == 1:
        withdraw = int(input("Enter the amount you want to withdraw"))
        if withdraw > balance:
            print(" Not Sufficient Balance") 
        else:
            balance = balance - withdraw
            print(f"Remaning Balance in the Account {balance}")
    elif choice == 2:
        deposit = int(input("Enter the amount you want to deposit"))
        balance = balance + deposit
        print(f"Remaning Balance in the Account {balance}")
    elif choice == 3:
        print(f"Remaning Balance in the Account {balance}")
    elif choice == 4:
        break
    else:
        print("Enter Correct Choice")