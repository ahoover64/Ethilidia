import pygame 
import item
class Inventory(object):


    def __init__(self, screensize):
        self.open = False
        self.rows = 6
        self.cols = 10
        self.squareside = 100
        self.squareedge = 5
        self.screensize = screensize
        self.rect = pygame.Rect((screensize[0]-self.cols*self.squareside)/2,(screensize[1]-self.rows*self.squareside)/2,self.cols*self.squareside,self.rows*self.squareside)
        
        self.items = []
        self.createImage()
        '''self.image = pygame.image.load("filename")'''
        '''self.image = pygame.transform.scale(self.image, (self.rect.width,self.rect.height))'''
    def addItem(self, item):
        self.items.append(item)
    def removeItem(self, item):
        self.items.remove(item)
    def displayInventory(self, screen):
        if self.open:
            screen.blit(self.image,self.rect)
    def createImage(self):
        temprect = pygame.Rect(0,0,self.squareside-self.squareedge*2, self.squareside-self.squareedge*2)
        self.image = pygame.Surface((self.rect.width,self.rect.height))
        pygame.draw.rect(self.image, (255,0,0), (0,0,self.rect.width,self.rect.height))
        '''self.image.blit(self.image,self.rect)'''
        for r in range(self.rows):
            for c in range(self.cols):
                temprect.x = c*self.squareside+self.squareedge
                temprect.y = r*self.squareside+self.squareedge
                pygame.draw.rect(self.image, (0,0,255), temprect)
