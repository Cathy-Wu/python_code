def save_file(boy,girl,count):
    boy_file = open('C:/Users/Administrator/Desktop/file_name_boy.txt','w')
    girl_file = open('C:/Users/Administrator/Desktop/file_name_girl.txt','w')

    file_name_boy = 'boy' + str(count) + '.txt'
    file_name_girl = 'girl' + str(count) + '.txt'

    boy_file.writelines(boy)
    girl_file.writelines(girl)

    boy_file.close()
    girl_file.close()

def split_file(file_name):    
    f = open('C:/Users/Administrator/Desktop/hello.txt')
    boy = []
    girl = []
    count = 1
    for each_line in f:
        if each_line[:6] != '======':
            (role,line_spoken) = each_line.split(':',1)
            if role == '小甲鱼':
                boy.append(line_spoken)
            if role == '鱼鱼':
                girl.append(line_spoken)
        else:
            save_file(boy,girl,count)

            boy = []
            girl = []
            count += 1
            
    save_file(boy,girl,count)


    f.close()
split_file('C:/Users/Administrator/Desktop/hello.txt')
