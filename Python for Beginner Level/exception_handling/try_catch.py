a = 4
b = 2

# normal flow 
# exception occured and code quit
try:
    x = a / b
except ZeroDivisionError:
    print(f"Value of Variable: 'b' cannot be Zero")   


# exception occured and quit continues
try:
    x = a / b
except ZeroDivisionError:
    print(f"Value of Variable: 'b' cannot be Zero")   
finally: 
    print("After Exception")

print("---")
# execute code only if exception does not occur
try:
    x = a / b
except ZeroDivisionError:
    print(f"Value of Variable: 'b' cannot be Zero")   
else: 
    y = 100 * b
    print(y)

# Type Error example
a = 8 
b = "YEah"
try:
    c = a + b
except TypeError:
    print("Addtion is not allwed between different types of data")
    
# File Not Found Error

try :
    with open("data.txt",'r') as file:
        data = file.read()
except FileNotFoundError:
    print("Sorry the file which you are trying to read does not exist")
