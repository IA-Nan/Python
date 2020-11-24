

#? 练习1：英制单位英寸与公制单位厘#### 百分制成绩转换为等级制成绩。

#! 要求：   如果输入的成绩在
#!         90分以上（含90分）       输出A；
#!         80分-90分（不含90分）    输出B；
#!         70分-80分（不含80分）    输出C；
#!         60分-70分（不含70分）    输出D；
#!         60分以下输出E。米互换。

a = float(input('请输入成绩: '))


if a >= 90:
    print("成绩为A")
elif a >= 80:
    print("成绩为B")
elif a >= 70:
    print ("成绩为C")
elif a >= 60:
    print ("成绩为D")
else:
    print ("成绩为E")

''' 

答案

'''

score = float(input('请输入成绩: '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('对应的等级是:', grade)


