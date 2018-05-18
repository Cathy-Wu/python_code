'''用pickle研制成不同文件'''
import pickle

def save_file(boy,girl,count):
    file_name_boy = 'boy' + str(count) + '.txt'
    file_name_girl = 'girl' + str(count) + '.txt'

    boy_file = open('C:/Users/Administrator/Desktop/file_name_boy.txt','wb')
    girl_file = open('C:/Users/Administrator/Desktop/file_name_girl.txt','wb')

    pickle.dump(boy,boy_file)
    pickle.dump(girl,girl_file)

    boy_file.close()
    girl_file.close()

def split_file(file_name):
    count = 1
    boy = []
    girl = []
    
    f =  open('C:/Users/Administrator/Desktop/hello.txt')
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



    

            

