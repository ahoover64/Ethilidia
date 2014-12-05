import pygame
import item
class Armor(item.Item):


    def __init__(self, name, imagename, description, health, reduction, movement, rarity, level):
        self.health = health
        self.reduction = reduction
        self.movement = movement
        super(Armor, self).__init__(name, imagename, description, rarity, level)
    def createMessage(self):
        lines = []
        lines.append(self.name)
        lines.append('Lvl ' + str(self.level) + ' ' + str(self.giveRarity()))
        lines.append("Max Health Increase: " + str(self.health))
        lines.append("Damage Reduction: " + str(self.reduction) + '%')
        lines.append("Movement Speed Change: " + str(self.movement))
        for line in self.description:
            lines.append(line)
        self.linenum = len(lines)
        return lines
    

