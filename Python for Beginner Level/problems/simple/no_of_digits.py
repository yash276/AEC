"""
Problem Statement:
Give a positive Integer count the number of digits.

Input: 123
Output: 3

Input:5
Ouput:1

Input: 56789
Output: 5
"""

num = 123
digit = 0

while num > 0:
    num = num // 10 #floor division 0 num / 10
    digit+= 1

print(digit)
print(num)