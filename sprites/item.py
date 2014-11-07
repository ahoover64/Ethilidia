import pygame 
class Item(object):


    def __init__(self, name, imagename, description):
        self.name = name
        self.imagename = imagename
        self.description = description
        self.image = pygame.Surface((100,100))
        pygame.draw.rect(self.image,(255,255,255),(0,0,100,100))
        pygame.draw.line(self.image, (0,0,0), (50,10), (50,90), 5)
        pygame.draw.line(self.image, (0,0,0), (40,70), (60,70), 5)



