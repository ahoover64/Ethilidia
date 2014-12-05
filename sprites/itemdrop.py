import pygame 
import gamesprite
import player
import utils.itemdropmanager
class ItemDrop(gamesprite.GameSprite):

    def __init__(self, level, maxRarity, itemtype, imagename, position, world_dim, rectangle, *groups):
        super(ItemDrop, self).__init__(imagename, position, world_dim, rectangle, *groups)
        '''0 = health, 1 = weapon, 2 = armor'''
        self.itemtype = itemtype 
        self.level = level
        self.imagename = imagename
        self.maxRarity = maxRarity
    def createImage(self, position, rectangle, filename):
        if (filename == None):
            self.image = pygame.Surface((100,100))
            pygame.draw.rect(self.image,(255,255,255),(0,0,100,100))
            pygame.draw.line(self.image, (0,0,0), (50,10), (50,90), 5)
            pygame.draw.line(self.image, (0,0,0), (40,70), (60,70), 5)
        else:
            tempimage = pygame.image.load(filename)
            tempimage = pygame.transform.scale(tempimage, (100,100))
            self.image = pygame.Surface((100,100))
            self.image.fill((255,255,255))
            self.image.blit(tempimage,pygame.Rect(0,0,100,100))
        self.image = pygame.transform.scale(self.image, rectangle)
        self.originalimage = self.image
        self.rect = pygame.rect.Rect(position, self.image.get_size())
        self.imagerect = self.rect 
    def update(self, game_sprites,soundplayer):
        if self.checkPlayer(game_sprites):
            game_sprites.remove(self)
    def checkPlayer(self, game_sprites):
        other_sprites = game_sprites.copy()
        if other_sprites.has(self):
            other_sprites.remove(self)
        for cell in pygame.sprite.spritecollide(self,other_sprites,False):
            if isinstance(cell,player.Player):
                utils.itemdropmanager.pickupitem(self, cell)
                return True
        return False
