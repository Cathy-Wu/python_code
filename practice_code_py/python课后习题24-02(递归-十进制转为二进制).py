'''使用递归编写一个十进制转为二进制的函数
（要求采用’取2取余‘的方式，结果与调用bin()一样返回字符串形式）'''
def dec2bin(dec):
    result = ''

    if dec:
        result = dec2bin(dec//2)
        return result + str(dec%2)
    else:
        return result

b = int(input('请输入一个整数：'))
a = dec2bin(b)
print('二进制数是:',a)
