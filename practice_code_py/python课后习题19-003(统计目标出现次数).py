'''编写一个函数findstr(),该函数统计一个长度为2的子字符串在另一个字符串中出现的次数。
例如：输入'you cannot improve your past, but you can improve your future.
once time is wasted, life is wasted.',子字符串‘im’,函数执行后打印‘子字符串
在目标中共出现3次’'''
'''def findstr(destr,substr):
   num=destr.count(substr)

destr=str(input('请输入一串字符串：'))
substr=str(input('请输入目标字符串：'))
num= num=destr.count(substr)
print('子字符串在目标中出现的次数是：',num)'''

def findstr(destr,substr):
    count = 0
    length = len(destr)
    if substr not in destr:
        print('在目标中找不到字符串！')
    else:
        for each1 in range(length-1):
            if destr[each1] == substr[0]:
                if destr[each1+1] == substr[1]:
                    count += 1
        print('子字符串在目标字符串中共出现 %d 次'%count)

destr=str(input('请输入一串字符串：'))
substr=str(input('请输入目标字符串：'))
findstr(destr,substr)
        



 
    
    
    
