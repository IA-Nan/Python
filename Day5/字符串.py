# a = """ab
# c"""
# b= 'abc'
# print(a)
# print(b)

# ?查找
#! find()
my_str = 'wo shi wsn ,wo shi yi ge nan sheng'
print(my_str.find('shi'))  # 3 下标
print(my_str.find('zzz'))  # -1

#! index()
print(my_str.index('wsn'))  # 7 下标
print(my_str.index('wsn'))  # 7 下标
# print(my_str.index('zzz'))   #!报错

#! count()
print(my_str.count('wo'))           # 2  次数
print(my_str.count('wo', 10, 20))    # 1次数


# ?修改

#! replace()
