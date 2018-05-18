'''求阶层：非递归版本
def recur(n):
    result = n
    for i in range(1,n):
        result *= i
        
    return result

number = int(input('请输入一个正整数：'))
result = recur(number)
print('%d的阶乘是：%d'%(number,result))'''


'''求阶层：递归版本'''
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
number = int(input('请输入一个正整数：'))
result = factorial(number)
print('%d的阶乘是：%d'%(number,result))
