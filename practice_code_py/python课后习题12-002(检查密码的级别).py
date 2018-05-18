symbols='!~@#$%^&*()_+=-'
chars='qwertyuioplkjhgfdsazxcvbnm'
nums='1234567890'
passwd=input('请输入需要检查的密码组合：')
flag_con = 0
length=len(passwd)
if length <=8:
    flag_len=1
elif 8 < length < 16:
    flag_len=2
else:
    flag_len=3

for i in passwd:
    if i in symbols:
        flag_con += 1
        break

for i in passwd:
    if i in chars:
        flag_con += 1
        break

for i in passwd:
    if i in nums:
        flag_con += 1
        break
while 1:
    print('您的密码级别鉴定为：',end='')
    if flag_len==1 or flag_con==1:
        print('低')
    elif flag_len== 2 or flag_con ==2:
        print('中')
    else:
        print('高')
        print('请继续保持!')
        break

    print("请按以下方式提升您的密码安全级别：\n\
    \t1. 密码必须由数字、字母及特殊字符三种组合\n\
    \t2. 密码只能由字母开头\n\
    \t3. 密码长度不能低于16位")
    break
