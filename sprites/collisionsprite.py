import pygame 
import gamesprite
import obstacle
class CollisionSprite(gamesprite.GameSprite):

    ''' Simple object that moves left and right across the screen '''

    def __init__(self, filename, position, world_dim, rectangle, *groups):

        ''' Initializes the obstacle sprite '''

        super(CollisionSprite, self).__init__(filename, position, world_dim, rectangle, *groups)
    def listInstance(self,cell,instances):
            for classdata in instances:
                if isinstance(cell,classdata):
                    return True
            return False
    def checkEdgeCollisions(self):
        if self.rect.x + self.rect.width > self.world_dim[0]:
            self.rect.x = self.world_dim[0] - self.rect.width
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y + self.rect.height > self.world_dim[1]:           
            self.rect.y = self.world_dim[1] - self.rect.height
        if self.rect.y < 0:
            self.rect.y = 0
    def checkCollisions(self, game_sprites, collisionlist=[obstacle.Obstacle]):
        other_sprites = game_sprites.copy()
        if other_sprites.has(self):
            other_sprites.remove(self)
        for cell in pygame.sprite.spritecollide(self,other_sprites,False):
            if self.listInstance(cell,collisionlist):
                if self.previous.x + self.previous.width <= cell.rect.x:
                    self.rect.x = self.previous.x
                if self.previous.y + self.previous.height <= cell.rect.y:
                    self.rect.y = self.previous.y
                if self.previous.x >= cell.rect.x + cell.rect.width:
                    self.rect.x = self.previous.x
                if self.previous.y >= cell.rect.y + cell.rect.height:
                    self.rect.y = self.previous.y
        for cell in pygame.sprite.spritecollide(self,other_sprites,False):
            if isinstance(cell,obstacle.Obstacle):
                self.rect = self.previous     
    def update(self,game_sprites):
        pass
        ''' Changes the direction of the sprite if it hits the edge of the screen '''

