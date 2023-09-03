"""
Problem statement
Given a number x, determine whether the given number is Armstrong number or not. A positive integer of n digits is called an Armstrong number of order n (order is number of digits) if.

abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + .... 
Input : 153
Output : Yes
153 is an Armstrong number.
1*1*1 + 5*5*5 + 3*3*3 = 153

Input : 120
Output : No
120 is not a Armstrong number.
1*1*1 + 2*2*2 + 0*0*0 = 9
"""

num = 1634
temp_num = num
power = 0
addition = 0

while temp_num > 0:
    temp_num = temp_num // 10 #floor division 0 num / 10
    power+= 1

temp_num = num

while temp_num > 0: 
    digit = temp_num % 10 # 1
    temp_num = temp_num // 10  # 0
    addition = addition + (digit ** power)
    
if addition == num:
    print("Armstong")
else:
    print("NOT")