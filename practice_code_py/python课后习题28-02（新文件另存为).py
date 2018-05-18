'''尝试将文件（OpenMe.mp3）打印到屏幕上
f = open('C:/Users/Administrator/Desktop/hello.txt')
for line in f:
    print(line,end = ' ')
f.close()
---将其保存为新文件（openme.txt）'''

f1 = open('C:/Users/Administrator/Desktop/hello.txt')
f2 = open('C:/Users/Administrator/Desktop/hello.mp3','x')
f2.write(f1.read())
f2.close()
f1.close()
