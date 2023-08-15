from rotatable import Rotatable
import pygame
import math
class Polygon(Rotatable):
    
    def __init__(self,x,y,dx,dy,rotation,world_width,world_height):
        super().__init__(x,y,dx,dy,rotation,world_width,world_height)
        self.mOriginalPolygon = []
        self.mColor = (255, 255, 255)
        
    def getPolygon(self):
        return self.mOriginalPolygon
    
    def getColor(self):
        return self.mColor
    
    def setPolygon(self, point_list):
        self.mOriginalPolygon = point_list
    
    def setColor(self, color):
        self.mColor = color
        
    def draw(self, surface):
        plist = self.mOriginalPolygon[::]
        plist = self.rotateAndTranslatePointList(plist)
        pygame.draw.polygon(surface, self.mColor, plist, 1)
    def getRadius(self):
        if not self.mOriginalPolygon:
            return 0
        distances = [math.sqrt(x**2 + y**2) for x, y in self.mOriginalPolygon]
        return sum(distances) / len(distances)