from circle import Circle
import math

class Bullet(Circle):
    def __init__(self, x, y, dx, dy, rotation, world_width, world_height):
        bullet_radius = 3
        
        # Pass attributes to the parent class in the correct order.
        super().__init__(x, y, dx, dy, rotation, bullet_radius, world_width, world_height)
        
        # Adjust the bullet's dx and dy based on the acceleration and rotation.
        self.mDX += 100.0 * math.cos(math.radians(rotation))
        self.mDY += 100.0 * math.sin(math.radians(rotation))
        
        # Set Bullet specific attributes
        self.mAge = 0
        
        # Adjust x and y based on new dx and dy for 0.1 seconds.
        self.move(0.1)
        
    def getAge(self):
        return self.mAge

    def setAge(self, age):
        self.mAge = age

    def setInactive(self):
        self.mActive = False

    def isActive(self):
        return self.mActive


    def evolve(self, dt):
        self.mAge += dt
        if self.mAge > 6:
            self.setInactive()
        self.move(dt)
