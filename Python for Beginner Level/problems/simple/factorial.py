"""
Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n. 

For example factorial of 6 is 6*5*4*3*2*1 which is 720.

Input: 6
Ouput: 720

Input: 10
Ouput: 3628800
"""

num = 10
factorial = 1

for index in range(1,num+1):
    factorial = factorial * index

print(factorial)