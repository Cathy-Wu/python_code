'''编写一个函数，判断传入的字符串参数是否为‘回文联’。即顺反都可以读'''
def fun1(temp):    
    rtemp=temp[::-1]
    if temp == rtemp:
        print('是回文联！')
    else:
        print('不是回文联！')

temp=str(input('请输入一句话：'))
fun1(temp)


def fun2(string):
    length=len(string)
    last=length-1
    length //= 2
    flag = 1
    for each in range(length):
        if string[each]!=string[last]:
            flag=0
        last-=1

    if flag == 1:
        return 1
    else:
        return 0

string = input('请输入一句话：')
if fun2(string) == 1:
    print('是回文联！')
else:
    print('不是回文联')


def pa(string):
    list1=list(string)
    list2=reversed(list1)
    if list1==list(list2):
        return'是回文联！'
    else:
        return'不是回文联！'
print(pa('上海的水来自海上'))
    
        
        




        
    
    







