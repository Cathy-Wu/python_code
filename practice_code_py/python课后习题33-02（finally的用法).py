'''错误-finally的用法'''
try:
    f = open('my_file.txt')
    print(f.read())
except OSError as reason:
    print('出错啦：'+ str(reason))
finally:
    if 'f' in locals():
        f.close()
