from polygon import Polygon
from random import uniform, randrange
import math

class Rock( Polygon ):
    
    def __init__(self, x,y,world_width,world_height):
        super().__init__(x,y,0,0,uniform(0, 359.9),world_width,world_height)
        
        self.mSpinRate = uniform(-90, 90)
        
        self.active = True
        radius = uniform(25, 40)
        number_of_points = randrange(5, 9)
        self.setPolygon(self.createRandomPolygon(radius,number_of_points))
        
        self.accelerate(uniform(10, 20))
        
    def getSpinRate(self):
        return self.mSpinRate
    
    def setSpinRate(self,spin_rate):
        self.mSpinRate = spin_rate


    def isActive(self):
        return self.active

    def setInactive(self):
        self.active = False
        
    def createRandomPolygon(self, radius, number_of_points):
        plist = []
        
        theta = (2 * math.pi) / number_of_points
        
        for i in range(number_of_points):
            r = uniform(radius*.7,radius*1.3)
            x = r * math.cos(theta*i)
            y = r * math.sin(theta*i)
            plist.append((x,y))
        return plist
    
    def evolve(self, dt):
        self.rotate(self.mSpinRate * dt)
        self.move(dt)