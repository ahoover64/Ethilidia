import pygame
import gamesprite
import spritesheet
import collisionsprite
import healthsprite
import math
import utils.camera
import utils.soundplayer
import animationsprite
import inventory
import sword
class Player(collisionsprite.CollisionSprite, animationsprite.AnimationSprite, healthsprite.HealthSprite):

    ''' Simple player class which allows you to move
        a sprite across the screen with the arrow keys
    '''

    def __init__(self, filename, position, world_dim, ssinfo, fps, screensize, *groups):

        ''' Initializes the player sprite '''
        super(Player, self).__init__(filename, position, world_dim,(50,50), *groups)
        animationsprite.AnimationSprite.__init__(self,filename,position,world_dim,(50,50),ssinfo,fps,*groups)
        healthsprite.HealthSprite.__init__(self,100)
        self.inventory = inventory.Inventory(screensize,self)
        startweapon = sword.Sword("Simple Sword", "gamedata/pictures/ancientBlade.png", {"Standard Sword"}, 10, 75, 6.0, 0, 0)
        self.inventory.equippedweapon = startweapon
        self.inventory.addItem(startweapon)
        self.ipressed = False
        self.speed = 5.0
        self.ticks_since_attack = 0
        self.fps = fps
    def createcamera(self,WIN_WIDTH,WIN_HEIGHT):
        self.screen_camera = utils.camera.Camera(utils.camera.complex_camera,self.world_dim[0],self.world_dim[1],WIN_WIDTH,WIN_HEIGHT)
    def swingatmouse(self,mx,my,game_sprites):
        self.ticks_since_attack = 0
        if self.inventory.equippedweapon == None:
            damage = 0
            wrange = 0
        else:
            damage = self.inventory.equippedweapon.damage
            wrange = self.inventory.equippedweapon.wrange
        self.screen_camera.update(self)
        shiftrect = pygame.Rect(mx,my,0,0)
        shiftrect = self.screen_camera.backapply(shiftrect)
        tempx = shiftrect.x-(self.rect.x+self.rect.width/2)
        tempy = shiftrect.y-(self.rect.y+self.rect.height/2)
        norm = math.sqrt(tempx*tempx+tempy*tempy)
        normx = tempx/norm
        normy = tempy/norm
        rect = pygame.Rect(normx*wrange/2-wrange/2,normy*wrange/2-wrange/2,wrange,wrange)
        rect.x += self.rect.x+self.rect.width/2
        rect.y += self.rect.y+self.rect.height/2
        hit = False
        for cell in game_sprites:
            if isinstance(cell,healthsprite.HealthSprite) and not cell == self:
                if (rect.x + rect.width > cell.rect.x) and (rect.x < cell.rect.x + cell.rect.width) and (rect.y + rect.height > cell.rect.y) and (rect.y < cell.rect.y + cell.rect.height):
                    cell.damage(damage)
                    hit = True
        return hit
    def canattack(self):
        return ((float)(self.ticks_since_attack)/self.fps)>=(1/self.inventory.equippedweapon.attackspeed)
    def update(self, game_sprites,soundplayer):

        ''' Moves the player sprite across the screen
            with arrow keys
        '''
        self.ticks_since_attack += 1
        self.previous = self.rect.copy()
        self.animationTick()
        key = pygame.key.get_pressed()
        if key[pygame.K_i]:
            if self.ipressed == False:
                self.inventory.open = not self.inventory.open
            self.ipressed = True
        else:
            self.ipressed = False

        if self.inventory.open:
            self.inventory.inventoryInteractions()
        precisex = self.rect.x
        precisey = self.rect.y
        if self.inventory.equippedarmor == None:
            currentSpeed = self.speed
        else:
            currentSpeed = self.speed+self.inventory.equippedarmor.movement
        if key[pygame.K_LSHIFT] or key[pygame.K_RSHIFT]:
            currentSpeed = currentSpeed*1.5
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            precisex -= currentSpeed
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            precisex += currentSpeed
        if key[pygame.K_UP] or key[pygame.K_w]:
            precisey -= currentSpeed
        if key[pygame.K_DOWN] or key[pygame.K_s]:
            precisey += currentSpeed

        self.rect.x = round(precisex,0)
        self.rect.y = round(precisey,0)
        self.rotateForDirection(self.previous,self.rect,180)
        m1,_,_ = pygame.mouse.get_pressed()
        mx,my = pygame.mouse.get_pos()
        hit = False
        if m1:
            if self.canattack():
                hit = self.swingatmouse(mx,my,game_sprites)
        if hit:
            soundplayer.playsound("hit")
        else:
            pass
        self.checkEdgeCollisions()
        self.checkCollisions(game_sprites)
        self.fixImage()
