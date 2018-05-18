'''递归-汉诺塔'''
def hanuo(n,x,y,z):
    if n == 1:
        print(x,'-->',z)
    else:
        hanuo(n-1,x,z,y)
        print(x,'-->',z)
        hanuo(n-1,y,x,z)

n = int(input('请输入汉诺塔的层数：'))
hanuo(n,'x','y','z')
