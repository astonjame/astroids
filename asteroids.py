import pygame
from ship import Ship
from rock import Rock
from bullet import Bullet
from star import Star
from random import uniform

NUMER_OF_ROCKS = 10
MAX_BULLETS = 3

class Asteroids:
    def __init__(self, width, height):
        self.mWorldWidth = width
        self.mWorldHeight = height
        self.mShip = Ship(width/2, height/2, width, height)
        self.mRocks = [Rock(uniform(0, width), uniform(0, height), width, height) for _ in range(NUMER_OF_ROCKS)]
        self.mBullets = []
        self.mStars = [Star(uniform(0, width), uniform(0, height), width, height) for _ in range(20)]
        self.mObjects = [self.mShip] + self.mRocks + self.mBullets + self.mStars

    def getWorldWidth(self):
        return self.mWorldWidth

    def getWorldHeight(self):
        return self.mWorldHeight

    def getShip(self):
        return self.mShip

    def getRocks(self):
        return self.mRocks

    def getObjects(self):
        return self.mObjects

    def getStars(self):
        return self.mStars

    def getBullets(self):
        return self.mBullets

    def turnShipLeft(self, rotate_amount):
        self.mShip.rotate(-rotate_amount)

    def turnShipRight(self, rotate_amount):
        self.mShip.rotate(rotate_amount)

    def accelerateShip(self, acceleration_amount):
        self.mShip.accelerate(acceleration_amount)

    def fire(self):
        if len(self.mBullets) < MAX_BULLETS:
            bullet = self.mShip.fire()
            self.mBullets.append(bullet)
            self.mObjects.append(bullet)

    def evolveAllObjects(self, dt):
        for obj in self.mObjects:
            obj.evolve(dt)

    def collideShipAndBullets(self):
        for bullet in self.mBullets:
            if self.mShip.hits(bullet):
                self.mShip.setInactive()
                bullet.setInactive()

    def collideShipAndRocks(self):
        for rock in self.mRocks:
            if self.mShip.hits(rock):
                self.mShip.setInactive()

    def collideRocksAndBullets(self):
        for bullet in self.mBullets:
            for rock in self.mRocks:
                if bullet.hits(rock):
                    bullet.setInactive()
                    rock.setInactive()

    def removeInactiveObjects(self):
        self.mRocks = [rock for rock in self.mRocks if rock.isActive()]
        self.mBullets = [bullet for bullet in self.mBullets if bullet.isActive()]
        self.mObjects = [self.mShip] + self.mRocks + self.mBullets + self.mStars

    def evolve(self, dt):
        self.evolveAllObjects(dt)
        self.collideShipAndBullets()
        self.collideShipAndRocks()
        self.collideRocksAndBullets()
        self.removeInactiveObjects()

    def draw(self, surface):
        surface.fill((0, 0, 0))
        for obj in self.mObjects:
            if obj.isActive():
                obj.draw(surface)
