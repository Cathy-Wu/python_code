'''编写程序，统计下边这个长字符串中各个字符出现的次数并找到cathy送给大家的一句话'''
'''str1 =  i am cthy'''
'''list1 = []
count = 0

for each in str1:
    if each not in list1:
        if each == '\n':
            print('\\n',str1,count(each))
        else:
            print(each,str1,count(each))
        list1.append(each)'''

str1 = '''i am cathy'''
countA = 0
countB = 0
countC = 0
length = len(str1)
for i in range(length):
    if str1[i] == '\n':
        continue
    if str1[i].isupper():
        if conutB ==1:
            countC += 1
            countA = 0
        else:
            countA += 1
        continue
    if str[i].islower() and countA == 3:
        countB = 1
        countA = 0
        target = i
        continue
    if str1[i].islower() and countC ==3:
        print(str[target],end='')

    countA = 0
    countB = 0
    countC = 0

    
