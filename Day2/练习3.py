

#?输入年份判断是不是闰年。

year = int(input("请输入年份："))

b = year % 4 == 0 and year % 100 != 0 or \
          year % 400 == 0

print("是闰年为True 不是为False \n%d 年为  %s " % (year,b))

1