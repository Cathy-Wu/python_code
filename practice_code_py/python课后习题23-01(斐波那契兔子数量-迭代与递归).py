'''经历了20个月后，总共有多少只兔子
f(n)=f(n-1)+f(n-2) , n>2'''
'''
递归'''
def f(n):
    if (n == 1) or (n == 2):
        return 1
    elif n < 1:
        print('输入有误，需要输入正整数！')
    else:
        return f(n-1) + f(n-2)
        
a = int(input('请输入月份：'))
result = f(a)
print('经历了',a,'个月后，总共有',f(a),'只兔子出生')

'''迭代
def fa(n):
    n1 = 1
    n2 = 1
    
    if n < 0:
        print('请输入正整数！')
        return -1
    else:
        return 1
    while (n -2) >= 1:
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        n -= 1
        
    return n3
a = int(input('请输入月份：'))
result = fa(a)
if result != -1:
    print('总共有%d只兔子'%result)'''


         
        
    
    
        
