import pygame 
import gamesprite
import spritesheet
import math
import utils.camera
import utils.soundplayer
class AnimationSprite(object):

    ''' Simple player class which allows you to move
        a sprite across the screen with the arrow keys
    '''

    def __init__(self, filename, position, world_dim, size, ssinfo, fps, *groups):

        ''' Initializes the player sprite '''
        ss = spritesheet.spritesheet(filename)
        startx,starty,rows,cols,width,height,bufferwidth,bufferheight = ssinfo
        self.images = []
	self.images = self.spritesheetToImages(ss,startx, starty, rows,cols,width,height,bufferwidth,bufferheight)
        self.image = self.images[0]
        self.originalimage = self.image
        self.image = pygame.transform.scale(self.image, size)
        self.i = 0
        self.maxi = len(self.images)
        self.ticks = fps/self.maxi
        self.ticki = 0
        
    def spritesheetToImages(self, tempss, startx, starty, rows, cols, width, height,bufferwidth,bufferheight):
        self.tempimages = []
        for y in range(0,rows):
            for x in range(0,cols):
                self.tempimages.append(tempss.image_at((startx + x*(width+bufferwidth), starty + y*(height+bufferheight), width, height),(0,0,0)))
        return self.tempimages
    def next(self):
        self.i += 1
        if(self.i == self.maxi):
            self.i = 0
        self.originalimage = self.images[self.i]
    def animationTick(self):
        self.ticki += 1
        if(self.ticki==self.ticks):
            self.ticki = 0
            self.next()
    
    def update(self, game_sprites,soundplayer):

        ''' Moves the player sprite across the screen
            with arrow keys
        '''
        pass
        
            

