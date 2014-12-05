import pygame
import item
class Sword(item.Item):


    def __init__(self, name, imagename, description, damage, wrange, attackspeed, rarity, level):
        self.damage = damage
        self.wrange = wrange
        self.attackspeed = attackspeed
        super(Sword, self).__init__(name, imagename, description, rarity, level)
    def createMessage(self):
        lines = []
        lines.append(self.name)
        lines.append('Lvl ' + str(self.level) + ' ' + str(self.giveRarity()))
        lines.append("Damage: " + str(self.damage))
        lines.append("Attack Speed: " + str(self.attackspeed))
        lines.append("Range: " + str(self.wrange))
        for line in self.description:
            lines.append(line)
        self.linenum = len(lines)
        return lines
    

