"""
输入M和N计算C(M,N)

Version: 0.1
Author: 骆昊
"""
# m = int(input('m = '))
# n = int(input('n = '))
# fm = 1
# for num in range(1, m + 1):
#     fm *= num
# fn = 1
# for num in range(1, n + 1):
#     fn *= num
# fm_n = 1
# for num in range(1, m - n + 1):
#     fm_n *= num
# print(fm // fn // fm_n)


# def fac(x):
#     result = 1
#     for n in range( 1, x + 1):
#         result *= n
#     return result

# m = int(input('m = '))
# n = int(input('n = '))


# print(fac(m) // fac(n) // fac(m-n))


# !在参数名前面的*表示args是一个可变参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total


# 在调用add函数时可以传入0个或多个参数
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))

name  = 'wsn'
age = 22

print('我是%s , 今年%d岁' %(name, age))
print(f'我是{name} , 今年{age}岁')

def gcd(x, y):
    """求最大公约数"""
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x, y):
    """求最小公倍数"""
    return x * y // gcd(x, y)

if __name__ == "__main__":
        a = int(input("a = "))
        b = int(input("b = "))
        c = gcd(a, b)
        print(c)
        c = lcm(a, b)
        print(c)



""" def is_prime(num):
    判断一个数是不是
    for factor in range(2, int(num ** 0.5) + 1):
        if num % factor == 0:
            return False
    return True if num != 1 else False

def main():
    a = int(input("输入一个数"))
    b = is_prime(a)
    print(b)


if __name__ == "__main__":

    main() """



