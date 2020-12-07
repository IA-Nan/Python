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


