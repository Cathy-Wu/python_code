'''递归，利用欧几里算法求最大公约数,gcd(x,y)的返回值为想x,y的最大公约数'''
def gcd(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(1,smaller + 1):
        if (x % i == 0) and (y % i == 0):
            result = i

    return result
            

a = int(input('请输入一个正整数：'))
b = int(input('请输入一个正整数：'))
result = gcd(a,b)
print('%d和%d的最大公约数为：%d'%(a,b,result))



'''
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b, remainder(a, b))

def gcd_1(a,b):
    while(b>0):
        rem = remainder(a,b)
        a = b
        b = rem
    return a

def remainder(x,y):
    return x%y

if __name__=='__main__':
    a = int(input("请输入一个数字:"))
    b = int(input("请输入另外一个数字:"))
    print("最大公约数：",gcd(a,b))'''

        
        

    
