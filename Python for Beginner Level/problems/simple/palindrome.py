"""
Input: 131
Ouput : Yes

Input : 32
Ouput: No

Input: 6336
Output: Yes
"""
num = 12321
tem_num = num
rev_num = 0

while num > 0:
    digit = num % 10
    rev_num = rev_num* 10 + digit # 3
    
    num = num // 10

if rev_num == tem_num:
    print("YES")
else:
    print("No")