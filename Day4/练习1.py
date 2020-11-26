
#?  寻找**水仙花数**。

#! 水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，
#! 该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$。

for i in range(100,1000):
    a = i % 10
    b = i // 10 %10
    c = i // 100
    if i == a**3+b**3+c**3:
        print(i)

"""
正整数的反转

Version: 0.1
Author: 骆昊
"""

num = int(input('num = '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)