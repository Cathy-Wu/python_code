print('十进制转化为二进制，采用’除2取余‘的方式，结果已字符串的形式返回')
def turn(x):
    list1 =[]
    result =''

    while x:
        a= x%2
        x= x//2
        list1.append(a)

    while list1:
        result += str(list1.pop())

    return result

    

