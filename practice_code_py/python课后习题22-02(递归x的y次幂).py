'''用递归写个power()模拟内建函数power(),既power(x,y)为计算并返回x的y次幂的值
def power(x,y):
    return x**y'''

def power(x,y):
    if (y-1) == 1:
        return x * x
    elif y == 1:
        return x
    elif y == 0:
        return 1 
    else:
        return x * power(x,y-1)

a = int(input('请输入一个x正整数：'))
b = int(input('请输入一个y正整数：'))
result = power(a,b)
print('%d的%d次幂是：%d'%(a,b,result))

    


    
