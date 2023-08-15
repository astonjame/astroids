from movable import Movable
import math

class Rotatable(Movable):
    def __init__(self,x,y,dx,dy,rotation,world_width,world_height):
        super().__init__(x,y,dx,dy,world_width,world_height)
        self.mRotation = rotation
        
    def getRotation(self):
        return self.mRotation
    
    
    def rotate(self,delta_rotation):
        self.mRotation += delta_rotation
        
        self.mRotation %= 360
    
    def splitDeltaVIntoXAndY(self,rotation,delta_velocity):
        
        degrees = math.radians(rotation)
        
        delta_v_x = delta_velocity * math.cos(degrees)
        delta_v_y = delta_velocity * math.sin(degrees)

        return delta_v_x, delta_v_y
            
        
    def accelerate(self,delta_velocity):
        dX,dY = self.splitDeltaVIntoXAndY(self.getRotation(),delta_velocity)
        self.mDX += dX
        self.mDY += dY
        
        
    def rotatePoint(self,x,y):
        radians = math.radians(self.mRotation)
        cos = math.cos(radians)
        sin = math.sin(radians)
        x_new = x * cos - y * sin
        y_new = x * sin + y * cos
        return x_new, y_new
       
    def translatePoint(self,x,y):
        return x + self.getX(), y + self.getY()
    def rotateAndTranslatePoint(self,x,y):
        x_new, y_new = self.rotatePoint(x, y)
        return self.translatePoint(x_new, y_new)
    
    def rotateAndTranslatePointList(self,point_list):
        
        return [self.rotateAndTranslatePoint(x,y) for x,y in point_list]