'''有两辆车，A到B地'''
class Vehicle:
    def __init__(self,speed):
        self.speed = speed
        
    def drive(self,distance):
        print('need %f hour(s)'%(distance/self.speed))

class Bike(Vehicle):
    pass

class Car(Vehicle):
    def __init__(self,speed,fuel):
        Vehicle._init_(self,speed)
        self.fuel = fuel

    def drive(self,distance):
        Vehile.drive(self,distance)
        print('need %f fuels'%(distance*self.fuel))

    b = Bike(15.0)
    c = Car(80.0,0.012)
    b.drive(100.0)
    c.drive(100.0)
    
        
    
