while(1):
    temp=input('请输入一个年份：')
    year=int(temp)
    if year%400==0:
        print(temp,'这是一个闰年!')
    elif year%4==0 and year%100!=0:
        print(temp,'这是一个闰年!')
    else:
        print(temp,'这不是一个闰年!')
