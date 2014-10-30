import pygame
import item
class Sword(item.Item):


    def __init__(self, name, imagename, description, damage, wrange):
        super(Sword, self).__init__(name, imagename, description)
        self.damage = damage
        self.wrange = wrange
