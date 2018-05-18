'''编写一个函数，分别统计出传入子字符串参数（可能不只一个参数）
的英文字母、空格、数字和其他字符的个数'''
def count(*param):
    length = len(param)
    for i in range(length):
        letters = 0
        space = 0
        digit = 0
        others = 0
        for each in param[i]:
            if each.isalpha():
                letters += 1
                continue
        
            elif each ==' ':
                 space += 1
                 continue
            
            elif each.isdigit():
                digit += 1
                continue

            else:
                others += 1
                continue
        print('第%d个字符串共有：英文字符串%d个，空格%d个，数字%d个，其他字符%d个.'%(i+1,
letters,space,digit,others))
        
count('i love cathy,1315','i love home,home love me**','3.14,好的','多少个')
            
        
            
        
        
        
    

    
