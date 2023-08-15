import math

class Movable:
    
    def __init__(self, x, y, dx, dy, world_width, world_height):
        self.mX = x
        self.mY = y
        self.mDX = dx
        self.mDY = dy
        self.mWorldWidth = world_width
        self.mWorldHeight = world_height
        self.mActive = True
    
    def getX(self):
        return self.mX
    
    def getY(self):
        return self.mY
    
    def getDX(self):
        return self.mDX
    
    def getDY(self):
        return self.mDY
    
    def getWorldWidth(self):
        return self.mWorldWidth
    
    def getWorldHeight(self):
        return self.mWorldHeight
    
    def move(self, dt):
        self.mX += self.mDX * dt
        self.mY += self.mDY * dt

        self.mX = self.mX % self.mWorldWidth
        self.mY = self.mY % self.mWorldHeight
    
    def getActive(self):
        return self.mActive
    
    def setActive(self, active_status):
        self.mActive = active_status
    
    def hits(self, other):
        distance = math.sqrt((self.mX - other.mX)**2 + (self.mY - other.mY)**2)
        return distance <= (self.getRadius() + other.getRadius())
    
    def getRadius(self):
        raise NotImplementedError
    
    def accelerate(self, delta_velocity):
        raise NotImplementedError
    
    def evolve(self, dt):
        raise NotImplementedError
    
    def draw(self, surface):
        raise NotImplementedError
