"""
1. What are functions?
2. Creating a Function. 
3. Calling a functions.
4. Parameters vs Arguments.
5. Number of arguments 
6. * args
7. keyword arguments.
8. *kwargs
9. Return Values
10. Pass
11. Built-In Vs User Defined Functions
"""
# Function is a piece of code that does not run until it is called.
# Function is a block of code that needs to be ran on multiple locations.

def print_func(): # function definition empty function
    print("Insidei from a Function") 

numbers = [3,4,5,6,7]


for item in numbers:
    print(item)

names = ["CArry", " RakaZone", "Tanamy"]

for item in names:
    print(item)
    
print_func() # calling a function

# Parameters and Arguments
def print_list( list_name: list): # parameters list_name: list
    """_summary_

    Args:
        list_name (list): _description_
    """
    for item in list_name:
        print(item)

print_list( names ) # arguments names
print_list(numbers) # argument numbers

def multiple_parameters(name:str, age:int):
    age+= 10
    print(f"{name} , {age}")
    

multiple_parameters("Yash", 35)

multiple_parameters(name="Yash", age=45)
multiple_parameters(age=55, name="Yash")

def multiple_parameters( *args): # args can take multiple input and will be a tuple
    print(type(args))
    for item in args:
        print(item)

multiple_parameters("Yash", 35)
multiple_parameters("Yash", 35, 5.6)
multiple_parameters("Yash", 35,5.6, "BAngalore")

def multiple_kwargs( ** kwargs): # keywords arguments
    print(kwargs)
    print(type(kwargs))
    
multiple_kwargs(name="Yash")
multiple_kwargs(name="Yash", age=35)
multiple_kwargs(name="Yash", age=35,height=5.6)

# how to return a value from a function
def return_func(age: int) -> int:
    age+= 10
    return age

age = return_func( age=34 ) 
print(age)


def print_func():
    pass

