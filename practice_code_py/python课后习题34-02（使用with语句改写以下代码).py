'''使用with语句改写以下代码，让python去关心文件的打开与关闭'''
def file_compare(file1,file2):
    with open(file1) as f1,open(file2) as f2:
        count = 0
        differ = []

        for line1 in f1:
            line2 = f2.readline()
            count += 1
            if line1 != line2:
                differ.append(count)

        return differ

file1 = input('请输入需要比较的头一个文件名：')
file2 = input('请输入需要比较的另一个文件名：')

differ = file_compare(file1,file2)

if len(differ) == 0:
    print('两个文件完全一样！')
else:
    print('两个文件共有【%d】处不同：'%len(differ))
    for each in differ:
        print('第%d行不一样'%each)
             
