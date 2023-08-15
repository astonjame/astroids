from rotatable import Rotatable
import pygame

class Circle(Rotatable):
    
    def __init__(self, x, y, dx, dy, rotation, radius, world_width, world_height):
        super().__init__(x, y, dx, dy, rotation, world_width, world_height)
        self.mRadius = radius
        self.mColor = (255, 255, 255)
        
    def setRadius(self, new_radius):
        if new_radius >= 1:
            self.mRadius = new_radius
    
    def getRadius(self):
        return self.mRadius
    
    def setColor(self, new_color):
        self.mColor = new_color
        
    def getColor(self):
        return self.mColor
    
    def draw(self, surface):
        position = (int(self.mX), int(self.mY))
        pygame.draw.circle(surface, self.mColor, position, int(self.mRadius))
