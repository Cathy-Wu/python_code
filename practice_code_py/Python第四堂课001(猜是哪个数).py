print('......再来一次。。。')
temp=input('猜是那个数：')
guess=int(temp)
if guess ==8:
    print('对的，你猜对了！')
    print('猜对了也木有奖励的')
else:
    if guess>8:
        print('哥哥，大了大了')
    else:
        print('小了小了')
print('游戏结束，game')
