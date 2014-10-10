import pygame 
import gamesprite
import spritesheet
class Player(gamesprite.GameSprite):

    ''' Simple player class which allows you to move
        a sprite across the screen with the arrow keys
    '''

    def __init__(self, filename, position, world_dim, *groups):

        ''' Initializes the player sprite '''
        super(Player, self).__init__(filename, position, world_dim,(100,100), *groups)
        self.ss = spritesheet.spritesheet("sprites/../gamedata/images/spritesheet.jpg")
        self.rows = 2
        self.cols = 4
        self.width = 125
        self.height = 125
        self.images = []
	self.images = self.spritesheetToImages(self.ss,self.rows,self.cols,self.width,self.height)
        self.image = self.images[0]
        self.image = pygame.transform.scale(self.image, (100,100))
        self.i = 0
        self.maxi = len(self.images)
        self.ticks = 60/self.maxi
        self.ticki = 0
    def spritesheetToImages(self, tempss, rows, cols, width, height):
        self.tempimages = []
        for y in range(0,rows):
            for x in range(0,cols):
                self.tempimages.append(tempss.image_at((x*width, y*height, width, height)))
        return self.tempimages
    def next(self):
        self.i += 1
        if(self.i == self.maxi):
            self.i = 0
        self.image = self.images[self.i]
        self.image = pygame.transform.scale(self.image, (100,100))
    def update(self, game_sprites):

        ''' Moves the player sprite across the screen
            with arrow keys
        '''
        self.previous = self.rect.copy()
        self.ticki += 1
        if(self.ticki==self.ticks):
            self.ticki = 0
            self.next()

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= 10
        if key[pygame.K_RIGHT]:
            self.rect.x += 10
        if key[pygame.K_UP]:
            self.rect.y -= 10
        if key[pygame.K_DOWN]:
            self.rect.y += 10

        if self.rect.x + self.rect.width > self.world_dim[0]:
            self.rect.x = self.world_dim[0] - self.rect.width
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y + self.rect.height > self.world_dim[1]:           
            self.rect.y = self.world_dim[1] - self.rect.height
        if self.rect.y < 0:
            self.rect.y = 0

        other_sprites = game_sprites.copy()
        if other_sprites.has(self):
            other_sprites.remove(self)
        for cell in pygame.sprite.spritecollide(self,other_sprites,False):
            if self.previous.x + self.previous.width <= cell.rect.x:
                self.rect.x = self.previous.x
            if self.previous.y + self.previous.height <= cell.rect.y:
                self.rect.y = self.previous.y
            if self.previous.x >= cell.rect.x + cell.rect.width:
                self.rect.x = self.previous.x
            if self.previous.y >= cell.rect.y + cell.rect.height:
                self.rect.y = self.previous.y
        if len(pygame.sprite.spritecollide(self,other_sprites,False)) > 0:
            self.rect = self.previous

            

