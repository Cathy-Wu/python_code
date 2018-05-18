print('编写一个进制转化程序')
q=1
while q:
    num = input('请输入一个整数：')
    if num != q:
        num = int(num)
        print('十进制->十六进制:%d -> 0x%x'%(num,num))
        print('十进制->八进制:%d -> 0o%o'%(num,num))
        print('十进制->二进制:%d ->'% num,bin(num))
    else:
        q=0
      
    
