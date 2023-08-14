"""
This files demonstrates the use of different
data types in python
"""
# integer int
age = 14 
# string str
first_name = "Yash "
last_name = "Agarwal"
# float 
height = 5.6

print(age)

age = 14.5
print(age)

str_datatype = "We can deifine entier sentences in a string variable"
str_datatype = 'We can deifine entier sentences in a string variable'
print(str_datatype)

# type casting
height_int = int(height)
age_str = str(age)
print(height_int)
print(type(age_str))

output = "Student age : " + age_str
output = f"Student age : {age}" 
print(output)

x = 10 
y = 5

# boolean variables
# bool()
outcome = False
print(type(outcome))

print(bool(age))
print(bool(first_name))
print(bool(height))

# any non-zero values is considered True
# any zero value is consideted as False
empty_str = ""
empty_float = 0.0
empty_int = 0
print(bool(empty_str))
print(bool(empty_float))
print(bool(empty_int))

empty = None
print(bool(empty))
