'''写个函数get_digits(n),将参数n分解出每个位的数字并按顺序存放在列表中，
举例：get_digits(12345)==>[1,2,3,4,5]

result = []
def get_digits(n):
    if n > 0:
        result.insert(0,n%10)
        get_digits(n//10)

get_digits(12345)
print(result)'''


def get_digits(n):
    result = []
    if n > 0:
        result.insert(0,n%10)
        get_digits (n//10)
        

a = int(input('请输入一个数：'))
b = get_digits(a)
print(result)
