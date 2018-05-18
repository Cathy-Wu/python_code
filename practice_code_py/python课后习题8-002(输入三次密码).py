count=3
password='cathy'
while count>0:
    passwd=input('请输入密码：')
    if passwd==password:
        print('恭喜你，密码正确')
        break
    elif '*' in passwd:
        print('密码错误，不能包含"*"，还有',count,'次机会')
        continue
    else:
        print('密码错误，还有',count-1,'次机会',end=' ')
        count=count-1
        continue
        
        
        
    

