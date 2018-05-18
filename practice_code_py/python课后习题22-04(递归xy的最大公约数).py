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
