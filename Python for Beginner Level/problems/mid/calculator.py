"""

1. Add
2. Subtract
3. Multiply
4. Division
5. Power
6. Exit
Enter you Choice 5
Enter First Number 2
Enter Second Number 3

Ouput 8 

1. Add
2. Subtract
3. Multiply
4. Division
5. Power
6. Exit
Enter you Choice 4
Enter First Number 2
Enter Second Number 4
Output 0.5

1. Add
2. Subtract
3. Multiply
4. Division
5. Power
6. Exit
Enter you Choice 6

"""

while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Division")
    print("5. Power")
    print("6. EXit")
    
    choice = int(input("Enter your Choice"))
    if choice!= 6 and choice >=1 and choice<= 5: 
        num1 = int(input("Enter First Number"))
        num2 = int(input("Enter Second Number"))
        
    if choice == 1:
        print(num1 + num2)
    elif choice == 2:
        print(num1 - num2)
    elif choice == 3:
        print(num1 * num2)
    elif choice == 4:
        print(num1 / num2)
    elif choice == 5:
        print(num1 ** num2)
    elif choice == 6:
        break
    else:
        print("Enter Correct Choice")