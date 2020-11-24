"""
输出乘法口诀表(九九表)

Version: 0.1
Author: 骆昊
"""

for i in range(1, 10): 
    for j in range(1, i + 1):
#        print(" %d * %d = %d " %(i , j , (i*j) ) )
        print(i,"*",j,"=",(i*j), end='\t')
    print()

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()


#? 练习1：输入一个正整数判断是不是素数。

#!  素数指的是只能被1和自身整除的大于1的整数。

from math import sqrt

num = int(input('请输入一个正整数: '))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)

