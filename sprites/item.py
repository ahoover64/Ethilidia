import pygame 
class Item(object):


    def __init__(self, name, imagename, description, rarity):
        self.name = name
        self.imagename = imagename
        self.description = description
        self.rarity = rarity
        if (imagename == None):
            self.image = pygame.Surface((100,100))
            pygame.draw.rect(self.image,(255,255,255),(0,0,100,100))
            pygame.draw.line(self.image, (0,0,0), (50,10), (50,90), 5)
            pygame.draw.line(self.image, (0,0,0), (40,70), (60,70), 5)
        else:
            tempimage = pygame.image.load(imagename)
            tempimage = pygame.transform.scale(tempimage, (100,100))
            self.image = pygame.Surface((100,100))
            self.image.fill((255,255,255))
            self.image.blit(tempimage,pygame.Rect(0,0,100,100))
        self.stats = self.createMessage()
    def createMessage(self):
        lines = []
        lines.append(self.name)
        lines.append(self.description)
        return lines
    def giveRarity(self):
        if self.rarity == 0:
            rarityName = "Common"
        elif self.rarity == 1:
            rarityName = "Uncommon"
        elif self.rarity == 2:
            rarityName = "Rare"
        elif self.rarity == 3:
            rarityName = "Legendary"
        return rarityName

