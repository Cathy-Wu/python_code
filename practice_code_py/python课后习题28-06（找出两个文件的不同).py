'''编写一个程序，比较用户输入的两个文件，如果不同，
显示出所有不同处的行号与第一个不同字符的位置，程序实现如下


def compare(*n):    
    file1 = open('C:/Users/Administrator/Desktop/hello.txt','r')
    file2 = open('C:/Users/Administrator/Desktop/hello1.txt','r')
    count = 0
    row = 0
    
    for (fa,fb) in zip(file1,file2):        
        row += 1
         
        if fa != fb:
            count += 1           
            print('第'+ str(row)+'行不一样')                      
        else:
            pass
                   
    file1.close()
    file2.close()


file1 = input('请输入需要比较的头一个文件名：')
file2 = input('请输入需要比较的另一个文件名：')
compare(file1,file2)'''


def file_compare(file1,file2):
    f1 = open('C:/Users/Administrator/Desktop/hello.txt','r')
    f2 = open('C:/Users/Administrator/Desktop/hello1.txt','r')
    count = 0
    differ = []

    for line1 in f1:
        line2 = f2.readline()
        count += 1
        if line1 != line2:
            differ.append(count)


    f1.close()
    f2.close()
    return differ

file1 = input('请输入需要比较的头一个文件名：')
file2 = input('请输入需要比较的另一个文件名：')

differ = file_compare(file1,file2)

if len(differ) == 0:
    print('两文件完全一样！')

else:
    print('两文件共有【%d】处不同:'%len(differ))
    for each in differ:
        print('第%d行不一样'%each)





        

