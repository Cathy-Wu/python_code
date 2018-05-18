import random

secret = random.randint(1,10)
try:
    temp = input('请猜猜我现在心里想的是哪个数：')
    guess = int(temp)
except (ValueError,EOFError,KeyboardInterrupt):
    print('输入错误！')
    guess = secret
while guess != secret:
    temp = input('猜错了请重新输入吧：')
    guess = int(temp)
    if guess == secret:
        print('猜对了！')
        print('不过木有奖励啦啦啦啦！')
    else:
        if guess > secret:
            print('大了大了')
        else:
            print('小小小了小了')
print('结束，game over!')


            
    
