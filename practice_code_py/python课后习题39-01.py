'''def split_file(file_name):
    f = open('C:/Users/Administrator/Desktop/HTML.txt')
    meta = []
    for each_line in f:        
        if each_line[1:5] == 'meta':
            detail = each_line
            meta.append(detail)
    f.close()
    return meta'''

def split_file(file_name):
    f = open('C:/Users/Administrator/Desktop/HTML.txt')
    count = 0
    meta = {}
    for each_line in f:
        count += 1
        if each_line[1:5] == 'meta':
            print('第%d行是文本:'%(count),each_line)            
            detail = each_line
            meta[count] = each_line
        
            
    print('总共有{0}行'.format(len(meta)))
    f.close()
    return meta
file = input('请输入需要打开的文件名：')
meta = split_file('C:/Users/Administrator/Desktop/HTML.txt')





        
            
            
        
        
    
