import pygame 
import item
class Inventory(object):


    def __init__(self, screensize):
        self.open = False
        self.rows = 6
        self.cols = 10
        self.squareside = 100
        self.squareedge = 5
        self.rect = pygame.Rect((screensize[0]-self.cols*self.squareside)/2,(screensize[1]-self.rows*self.squareside)/2,self.cols*self.squareside,self.rows*self.squareside)
        
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
            temprect = pygame.Rect(0,0,self.squareside-self.squareedge*2, self.squareside-self.squareedge*2)
            for r in range(self.rows):
                for c in range(self.cols):
                    temprect.x = c*self.squareside+self.squareedge+self.rect.x
                    temprect.y = r*self.squareside+self.squareedge+self.rect.y
                    pygame.draw.rect(screen, (0,0,255), temprect)
