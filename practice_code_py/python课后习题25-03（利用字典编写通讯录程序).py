'利用字典特性编写一个通讯录程序'
print('--欢迎进入通讯录程序--')
print('--1：查询联系人资料--')
print('--2：插入新的联系人--')
print('--3：删除已有联系人--')
print('--4：退出通讯录程序--')

contacts = dict()
while True:
    code = int(input('请输入相关的指令代码：'))
    if code == 1:
        name = input('请输入联系人姓名：')
        if name in contacts:
            print(name,':',contacts[name])
        else:
            print('您输入的联系人不存在！')

    elif code == 2:
        name = input('请输入联系人姓名：')
        if name in contacts:
            print('您输入的姓名在通讯录中已存在--》',name,':',contacts[name])
            m = input('是否修改用户资料(YES/NO)：')
            if m == 'YES':
                contacts[name] = input('请输入联系人的电话号码：')
            else:
                print(name,':',contacts[name])
        else:
            print('您输入的联系人不存在！')
            contacts[name] = input('请输入联系人的电话号码：')

    elif code == 3:
        name = input('请输入联系人姓名：')
        if name in contacts:
            contacts.pop(name)
        else:
            print('您输入的联系人不存在！')
            
    else:
        break
    
print('--退出通讯录程序！--')
    
                
        
        
