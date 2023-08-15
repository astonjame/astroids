from circle import Circle
import random
class Star(Circle):

    def __init__(self, x, y, world_width, world_height):
        super().__init__(x, y, 0, 0, 0, 2, world_width, world_height)
        self.mBrightness = random.randint(0, 255)
        self.setColor((self.mBrightness, self.mBrightness, self.mBrightness))
        self.mActive = True
    def setInactive(self):
        self.mActive = False

    def isActive(self):
        return self.mActive



    def setBrightness(self, brightness):
        if 0 <= brightness <= 255:
            self.mBrightness = brightness
            self.setColor((self.mBrightness, self.mBrightness, self.mBrightness))
    def getBrightness(self):
        return self.mBrightness

    def evolve(self, dt):
        change = random.choice([-10, 0, 10])
        new_brightness = self.mBrightness + change
        if 0 <= new_brightness <= 255:
            self.setBrightness(new_brightness)