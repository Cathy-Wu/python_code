'''define a Point and Line, and use the getLen to get the length of the line'''

import math
class Point():
    def __init__(self,x=0,y=0):
         self.x = x
         self.y = y
         
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

class Line():
    def __init__(self,P1,P2):
        self.x = P1.getX()-P2.getX()
        self.y = P1.getY()-P2.getY()
        
        self.len = math.sqrt(self.x * self.x + self.y * self.y)

    def getLen(self):
        return self.len


