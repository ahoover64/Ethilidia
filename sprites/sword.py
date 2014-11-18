import pygame
import item
class Sword(item.Item):


    def __init__(self, name, imagename, description, damage, wrange):
        self.damage = damage
        self.wrange = wrange
        super(Sword, self).__init__(name, imagename, description)
    def createMessage(self):
        lines = []
        lines.append(self.name)
        lines.append("Damage: " + str(self.damage))
        lines.append("Range: " + str(self.wrange))
        lines.append(self.description)
        return lines

