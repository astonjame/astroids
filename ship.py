from polygon import Polygon
from bullet import Bullet
class Ship(Polygon):
    def __init__(self,x,y,world_width,world_height):
        super().__init__(x,y,0,0,0,world_width,world_height)
        
        self.setPolygon([(10,0),(-10,10),(0,0),(-10,-10)])
        self.active = True
    
    def evolve(self,dt):
        self.move(dt)
    def isActive(self):
        return self.active

    def setInactive(self):
        self.active = False
        
    def fire(self):
        bullet_start_point = self.rotateAndTranslatePoint(*self.getPolygon()[0])
        bullet = Bullet(*bullet_start_point, self.getDX(), self.getDY(), self.getRotation(), self.getWorldWidth(), self.getWorldHeight())
        return bullet
