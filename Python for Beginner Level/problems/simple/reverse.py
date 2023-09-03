"""
Input: 123
Output: 321

Input: 5678
Ouput: 8765
"""

num = 123234
rev_num = 0

while num > 0:
    digit = num % 10
    rev_num = rev_num* 10 + digit # 3
    
    num = num // 10

print(rev_num)