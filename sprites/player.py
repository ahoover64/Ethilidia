import pygame 
import gamesprite
import spritesheet
import collisionsprite
import healthsprite
import math
import utils.camera
import utils.soundplayer
import animationsprite
class Player(collisionsprite.CollisionSprite, animationsprite.AnimationSprite, healthsprite.HealthSprite):

    ''' Simple player class which allows you to move
        a sprite across the screen with the arrow keys
    '''

    def __init__(self, filename, position, world_dim, ssinfo, fps, *groups):

        ''' Initializes the player sprite '''
        super(Player, self).__init__(filename, position, world_dim,(50,50), *groups)
        animationsprite.AnimationSprite.__init__(self,filename,position,world_dim,(50,50),ssinfo,fps,*groups)
        healthsprite.HealthSprite.__init__(self,100)
        self.clicking = False

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
        rect = pygame.Rect(normx*50-25,normy*50-25,50,50)
        rect.x += self.rect.x+self.rect.width/2
        rect.y += self.rect.y+self.rect.height/2
        hit = False
        for cell in game_sprites:
            if isinstance(cell,healthsprite.HealthSprite) and not cell == self:
                if (rect.x + rect.width > cell.rect.x) and (rect.x < cell.rect.x + cell.rect.width) and (rect.y + rect.height > cell.rect.y) and (rect.y < cell.rect.y + cell.rect.height):
                    cell.damage(20)
                    hit = True
        return hit
    def update(self, game_sprites,soundplayer):

        ''' Moves the player sprite across the screen
            with arrow keys
        '''
        self.previous = self.rect.copy()
        self.animationTick()
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            self.rect.x -= 10
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.rect.x += 10
        if key[pygame.K_UP] or key[pygame.K_w]:
            self.rect.y -= 10
        if key[pygame.K_DOWN] or key[pygame.K_s]:
            self.rect.y += 10

        self.rotateForDirection(self.previous,self.rect,0)
        m1,_,_ = pygame.mouse.get_pressed()
        mx,my = pygame.mouse.get_pos()
        hit = False
        if m1:
            if self.clicking == False:
                hit = self.swingatmouse(mx,my,game_sprites)
            self.clicking = True
        else:
            self.clicking = False
        if hit:
            soundplayer.playsound("hit")
        else:
            pass
        self.checkEdgeCollisions()
        self.checkCollisions(game_sprites)
        
            

