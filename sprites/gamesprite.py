import pygame 
import math
class GameSprite(pygame.sprite.Sprite):

    ''' Simple player class which allows you to move
        a sprite across the screen with the arrow keys
    '''

    def __init__(self, filename, position, world_dim, rectangle, *groups):

        ''' Initializes the player sprite '''
        super(GameSprite, self).__init__(*groups)
        self.world_dim = world_dim
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, rectangle)
        self.originalimage = self.image
        self.rect = pygame.rect.Rect(position, self.image.get_size())
    def rotateImageTo(self,degrees):
        
        self.image = pygame.transform.scale(self.originalimage, (self.rect.width,self.rect.height))
        self.image = pygame.transform.rotate(self.image,degrees)
        '''self.image.scroll((int)(-(self.image.get_width()-self.rect.width)/2),(int)(-(self.image.get_height()-self.rect.height)/2))'''
    def rotateForDirection(self,previous,current,offset):
        if (previous.x == current.x and previous.y == current.y):
            pass
        else:
            xchange = previous.x - current.x
            ychange = previous.y - current.y
            self.rotateImageTo(math.atan2(xchange,ychange)*180/math.pi+offset)
