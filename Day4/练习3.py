
#?CRAPS赌博游戏

#! CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。该游戏使用两粒骰子，
#! 玩家通过摇两粒骰子获得点数进行游戏。简单的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
#! 玩家第一次如果摇出2点、3点或12点，庄家胜；
#! 其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
#! 如果玩家摇出了第一次摇的点数，玩家胜；其他点数，玩家继续要骰子，直到分出胜负。


"""
*Craps赌博游戏
*我们设定玩家开始游戏时有1000元的赌注
*游戏结束的条件是玩家输光所有的赌注
"""

""" 
from random import randint

moner = 1000
while moner > 0:
    print("您有%d元" %moner)
    a = float(input("请下注"))
    if  a < 0 or a > moner :
        print("下注错误")
        continue
    while True:
        b = randint(1, 6) + randint(1, 6)
        print("摇出了%d"%b)
        if b == 2 or  b == 3 or  b == 12:
            moner -= a
            break
        elif b == 7 or  b == 11:
            moner += a
            break

print("您输光了") 

"""

"""
Craps赌博游戏
我们设定玩家开始游戏时有1000元的赌注
游戏结束的条件是玩家输光所有的赌注

Version: 0.1
Author: 骆昊
"""
from random import randint

money = 1000
while money > 0:
    print('你的总资产为:', money)
    needs_go_on = False
    while True:
        debt = int(input('请下注: '))
        if 0 < debt <= money:
            break
    first = randint(1, 6) + randint(1, 6)
    print('玩家摇出了%d点' % first)
    if first == 7 or first == 11:
        print('玩家胜!')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜!')
        money -= debt
    else:
        needs_go_on = True
    while needs_go_on:
        needs_go_on = False
        current = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % current)
        if current == 7:
            print('庄家胜')
            money -= debt
        elif current == first:
            print('玩家胜')
            money += debt
        else:
            needs_go_on = True
print('你破产了, 游戏结束!')
            
    

