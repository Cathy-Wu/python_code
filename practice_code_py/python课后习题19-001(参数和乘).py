'''计算打印所有的参数的和乘以基数3的结果\
 如果最后一个参数为5，则基数为5，基数不参与求和计算\
def fun(*a):
    result = 0
    for each in a:
        result += each      

    if a ==5:
        b=(result-5)*5
        print('计算打印所有参数的和乘以基数5的结果：',b)
    else:
        print('计算打印所有参数的和乘以基数3的结果：',result*3)'''

def mfun(*a,base=3):
    result = 0
    for each in a:
        result += each
    result *= base

    print('结果是：',result)
