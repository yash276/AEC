marks = 745

first_division = 650
second_division = 500
thrid_division = 350


# if condition :
# condition greater than >
# condition less than <
# condition greater than and equal to >=
# condition less than and equal to <=
# condition equal ==
# condition not equal !=
#   excute code
if marks >= first_division :        
    print("First Division")
else :
    print("Not First Division")


if marks>=first_division:
    print("First Divsion")
elif marks>=second_division:
    print("Second Divsion")
else:
    print("Third Division")

# short hand notations
if marks>=first_division : print("First Division")
print("First division") if marks>=first_division else print("Not firdst Divsion") 


# and , or
# condition1 and condition2 

a =500
b = 330
c= 500

if a>c and a<b:
    print("A Wins")

if a>c or  a<b :
    print("A Wins")

# Print largest nnumber and second largest
# 5000 is the largest nuber
# 500 is the second largest number
# 33 is the third largest number

if a>b and a>c:
    print(f'{a} is the largest number')
    # nested if
    if b>c:
        print(f'{b} is the second largest number')
        print(f'{c} is the third largest number')
    else:
        print(f'{c} is the second largest number')
        print(f'{b} is the third largest number')
elif b>a and b>c:
    print(f'{b} is the largest number')    
    if a>c:
        print(f'{a} is the second largest number')
        print(f'{c} is the third largest number')
    else:
        print(f'{c} is the second largest number')
        print(f'{a} is the third largest number')
else:
    print(f'{c} is the largest number')
    if a>b:
        print(f'{a} is the second largest number')
        print(f'{b} is the third largest number')
    else:
        print(f'{b} is the second largest number')
        print(f'{a} is the third largest number')

# not operator
if not a>b:
    print("A<B")
else:
    print("A>B")