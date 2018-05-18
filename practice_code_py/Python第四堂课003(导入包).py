import random
secret = random.randint(1,10)
print('......再来一次......')
temp=input('猜是哪个数：')
guess=int(temp)
while guess !=secret :
    guess=int(temp)
    if guess ==secret:
        print('对的，你猜对了！')
        print('猜对了也木有奖励的')
    else:
        if guess>secret:
            print('哥哥，大了大了')
            temp=input('猜错了请重新输入吧：')
        else:
            print('小了小了')
            temp=input('猜错了请重新输入吧：')
print('游戏结束，game')
