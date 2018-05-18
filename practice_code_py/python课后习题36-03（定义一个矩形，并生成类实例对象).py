'''定义一个矩形，并生成类实例对象'''
class Rectangle():
    length = 5
    width = 4

    def setRect(self):
        print('请输入矩形的长和宽')
        self.length = float(input('长：'))
        self.width = float(input('宽：'))
    def getRect(self):
        print('矩形的长:%.2f,矩形的宽：%.2f'%(self.length,self.width))
    def getArea(self):
        return (self.length*self.width)
    
        
    
    
