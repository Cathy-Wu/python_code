print('求100~999之间的所有水仙花数，3位数等于各位数字的立方和')
for i in range(100,1000):
    sum=0
    temp=i
    while temp:
        sum=sum+(temp%10)**3
        temp//=10
    if sum ==i:
        print(i)
