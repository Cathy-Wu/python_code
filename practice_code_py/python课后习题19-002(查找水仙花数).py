'''如果一个3位数等于其各位数字的立方和，则称之为水仙花数。\
例如153 = 1^3+5^3+3^3,因此153是一个水仙花数，编写一个程序找出所有的水仙花数
def id1():        
    for i in range(100,1000):
        a=(i//100)**3
        b=((i//10)%10)**3
        c=(i%10)**3
        if i == (a+b+c):
             print('所有的水仙花数分别是：',end='')
        else:
             continue'''
def id2():
    for each in range(100,1000):
        temp = each
        sum =0
        while temp:
            sum =sum + (temp%10)**3
            temp = temp//10
        if sum == each:
            print(each,end='\t')
            
print('所有的水仙花数分别是：',end='')


                           
                   
