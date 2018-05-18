'''编写一个程序，当用户输入文件名和行数N后，将该文件的前N行内容打印到屏幕上
def file_print(file,num):
    f = open('C:/Users/Administrator/Desktop/hello.txt','r')
    for i in range(num):
        print(f.readline())
    f.close()
    
file = input('请输入要打开的文件名：')
num = int(input('请输入前几行:'))
file_print(file,num)'''


'''根据需要，输入随意的行数并打印出来'''
def file_view(file_name,line_num):
    if line_num.strip() == ':':
        begin = '1'
        end = '-1'

        (begin,end) = line_num.split(':')

        if begin == '':
            begin = '1'
        if end == '':
            end = '-1'

        if begin == '1' and end == '-1':
            prompt = '的全文'
        elif begin == '1':
            prompt ='从开始到%s'%end
        elif end == '-1':
            prompt ='从%s到结束'%begin
        else:
            prompt ='从第%s行到第%行'%(begin,end)

        print('\n文件%s%s的内容如下:\n'%(file_name,prompt))

        begin = int(begin) -1
        end = int(end)
        lines = end - begin

        f = open(file_name)

        for i in range(begin):
            f.readline()

        if lines < 0:
            print(f.read())
        else:
            for j in range(lines):
                print(f.readline(),end='')

        f.close()

file_name = input(r'请输入要打开的文件:')
line_num = input('请输入需要显示的行数【格式如13:21或21：或：】:')
file_view(file_name,line_num)

        
   




