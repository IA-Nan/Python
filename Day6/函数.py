""" def testA():
 print('---- testA start----')
 testB()
 print('---- testA end----')

def testB():
 print('---- testB start----')
 print('这⾥是testB函数执⾏的代码...(省略)...')
 print('---- testB end----')

testA() """

#打印多条横线

# def print_line():
#     print('-' * 5)
# def print_lines(a):
#     for i in range(a):
#         print_line()

# print_lines(5)

#1. 求三个数之和

def sum_num(x, y ,z):
    return x + y + z

# sum = sum_num(1 , 2 ,3)
# print(sum)
#2. 求三个数平均值

def average_num(a , b , c):
    return sum_num(a , b ,c) / 3
    
print(average_num(3 , 6 , 9))






