import pygame 
import item
class Inventory(object):


    def __init__(self, screensize):
        self.open = False
        self.rect = (100,100,screensize[0]-200,screensize[1]-200)
        self.items = []
        '''self.image = pygame.image.load("filename")'''
        '''self.image = pygame.transform.scale(self.image, (self.rect.width,self.rect.height))'''
    def addItem(self, item):
        self.items.append(item)
    def removeItem(self, item):
        self.items.remove(item)
    def displayInventory(self, screen):
        if self.open:
            '''screen.blit(self.image,self.rect)'''
            pygame.draw.rect(screen, (255,0,0), self.rect)

