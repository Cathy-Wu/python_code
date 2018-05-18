'''使用递归,有5人坐在一起，问第五人多少岁？他比第四人大2岁，第四人比第三人大2岁，
   第三人比第二人大3岁，第二人比第一人大2岁，第一人有10 岁，问第五人多大'''
def age(n):
    age1 = 10
    if n == 1:
        return 10
    else:
        return age(n-1) + 2

number = int(input('请输入一个整数：'))
result = age(number)
print('是',result,'岁')


    
