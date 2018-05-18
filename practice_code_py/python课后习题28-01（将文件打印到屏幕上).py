'''尝试将文件（OpenMe.mp3）打印到屏幕上'''
f = open('C:/Users/Administrator/Desktop/hello.txt')
for line in f:
    print(line,end = ' ')
f.close()
