'''定义一个person类并生成类实例对象'''
'''属性：姓名（默认姓名'小甲鱼'）
方法：打印姓名
属性：方法中对属性的引用形式需加上self,如self.name'''
class Person():
    name = '小甲鱼'

    def print_name(self):
        print(self.name)
        
