import pygame
import item
class Sword(item.Item):


    def __init__(self, name, imagename, description, damage, wrange, rarity, level):
        self.damage = damage
        self.wrange = wrange
        super(Sword, self).__init__(name, imagename, description, rarity, level)
    def createMessage(self):
        lines = []
        lines.append(self.name)
        lines.append('Lvl ' + str(self.level) + ' ' + str(self.giveRarity()))
        lines.append("Damage: " + str(self.damage))
        lines.append("Range: " + str(self.wrange))
        lines.append(self.description)
        return lines
    

