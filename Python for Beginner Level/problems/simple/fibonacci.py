"""
The Fibonacci numbers are the numbers in the following integer sequence. 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
F(n) = F(n-1) + F(n-2)

Input: 10
"""

count = int(input("Enter the number of elements in the series you want"))

# F(n-2)
first_number = 0
# F(n-1)
second_number = 1

while count > 0:
    
    next_number = second_number + first_number  # 3
    
    first_number = second_number # 1
    second_number = next_number # 2
    
    count-= 1
    print(next_number)