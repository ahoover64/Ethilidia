import pygame 
import gamesprite
import spritesheet
import collisionsprite
import healthsprite
import math
import utils.camera
class Player(collisionsprite.CollisionSprite, healthsprite.HealthSprite):

    ''' Simple player class which allows you to move
        a sprite across the screen with the arrow keys
    '''

    def __init__(self, filename, position, world_dim, *groups):

        ''' Initializes the player sprite '''
        super(Player, self).__init__(filename, position, world_dim,(50,50), *groups)
        healthsprite.HealthSprite.__init__(self,100)
        self.ss = spritesheet.spritesheet("sprites/../gamedata/images/spritesheet.jpg")
        self.rows = 2
        self.cols = 4
        self.width = 125
        self.height = 125
        self.images = []
	self.images = self.spritesheetToImages(self.ss,self.rows,self.cols,self.width,self.height)
        self.image = self.images[0]
        self.image = pygame.transform.scale(self.image, (50,50))
        self.i = 0
        self.maxi = len(self.images)
        self.ticks = 60/self.maxi
        self.ticki = 0
        self.clicking = False
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
        self.image = pygame.transform.scale(self.image, (50,50))
    def createcamera(self,WIN_WIDTH,WIN_HEIGHT):
        self.screen_camera = utils.camera.Camera(utils.camera.complex_camera,self.world_dim[0],self.world_dim[1],WIN_WIDTH,WIN_HEIGHT)
    def swingatmouse(self,mx,my,game_sprites):
        self.screen_camera.update(self)
        shiftrect = pygame.Rect(mx,my,0,0)
        shiftrect = self.screen_camera.backapply(shiftrect)
        tempx = shiftrect.x-(self.rect.x+self.rect.width/2)
        tempy = shiftrect.y-(self.rect.y+self.rect.height/2)
        norm = math.sqrt(tempx*tempx+tempy*tempy)
        normx = tempx/norm
        normy = tempy/norm
        rect = pygame.Rect(normx*25-10,normy*25-10,20,20)
        rect.x += self.rect.x+self.rect.width/2
        rect.y += self.rect.y+self.rect.height/2
        for cell in game_sprites:
            if isinstance(cell,healthsprite.HealthSprite) and not cell == self:
                if (rect.x + rect.width > cell.rect.x) and (rect.x < cell.rect.x + cell.rect.width) and (rect.y + rect.height > cell.rect.y) and (rect.y < cell.rect.y + cell.rect.height):
                    cell.damage(20)
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
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            self.rect.x -= 10
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.rect.x += 10
        if key[pygame.K_UP] or key[pygame.K_w]:
            self.rect.y -= 10
        if key[pygame.K_DOWN] or key[pygame.K_s]:
            self.rect.y += 10

        m1,_,_ = pygame.mouse.get_pressed()
        mx,my = pygame.mouse.get_pos()
        if m1:
            if self.clicking == False:
                self.swingatmouse(mx,my,game_sprites)
            self.clicking = True
        else:
            self.clicking = False
        self.checkEdgeCollisions()
        self.checkCollisions(game_sprites)
        
            

