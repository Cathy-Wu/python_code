'''利用filter（）和lambda表达式快速求出100以内的所有3的倍数'''
list(filter(lambda x :not(x%3),range(1,100) ))
'''列表推导式'''
[i for i in range(1,100) if not(i%3)]
