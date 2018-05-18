user_date = {}

def new_user():
    prompt = '请输入用户名：'
    while True:
        name = input(prompt)
        if name in user_date:  
            prompt = '此用户已经被使用，请重新输入：' 
            continue
        else:
            break

    passwd =input('请输入密码：')
    user_date[name] = passwd
    print('注册成功，请登录！')

def old_user():
    prompt = '请输入用户名：'
    while True:
        name = input(prompt)
        if name not in user_date:
            prompt = '您输入的用户名不存在，请重新输入：'
            continue
        else:
            break
    passwd =input('请输入密码：')
    pwd = user_date.get(name)
    if passwd == pwd:
        print('欢迎进入xx系统，请点击右上角的x结束程序！')
    else:
        print('密码输入错误！')

def showmenu():
    prompt='''
|---新建用户：N/n---|

|---登录账号：E/e---|

|---退出程序：Q/q---|

|---请输入指令代码：'''

    while True:
        chosen = False
        while not chosen:
            choice = input(prompt)
            if choice not in 'NnEeQq':
                print('密码输入错误,请重新输入：')
            else:
                chosen = True

            if (choice == 'Q') or (choice == 'q'):
                break
            if (choice == 'N') or (choice == 'n'):
                new_user()
            if (choice == 'E') or (choice == 'e'):
                old_user()

showmenu()
                

    

        
        

    
            
    
        
        
