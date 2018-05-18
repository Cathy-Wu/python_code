'''尝试编写一个用户登录程序（尝试将功能封装成函数）'''
print('---新建用户:N/n---')
print('---登录账号：E/e---')
print('---退出程序:Q/q---')

log = dict()
while True:
    n = 3
    code = input('请输入指令代码：')
    if (code == 'N') or (code == 'n'):        
        name = input('请输入用户名：')
        if name in log:
            name = input('此用户名已被使用，请重新输入：')
            continue
        else:
            log[name] = input('请输入密码：')
            print('注册成功，赶紧登录试试吧！')

    elif (code == 'E') or (code == 'e'):
        name = input('请输入用户名：')
        if name in log:
            code = input('请输入密码：')
            while n >= 0:
                if code == log[name]:
                    print('欢迎进入福贝金福系统！')
                else:
                    code = input('密码错误，请重新输入:')
                    n -= 1
                break   
            print('密码错误！！！！)                            
                        
        else:
            name = input('您输入的用户名不存在，请重新输入：')
            continue
           
    elif (code == 'Q') or (code == 'q'):
        break
    
print('--退出登录程序！--')

            
            
            
            
            
            
            
            
