'''尝试一个新的函数int_input(),当用户输入整数
的时候正常返回，否则提示出错并要求重新输入'''
def int_input(a=''):
    while True:
        try:
            int(input(a))
            break
        except ValueError:
            print('输入错误，不是整数，请重新输入！')
            
int_input('请输入一个整数：')

    
