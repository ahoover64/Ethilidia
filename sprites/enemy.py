import pygame 
import gamesprite
import obstacle
import collisionsprite
import player
import math
import healthsprite
class Enemy(collisionsprite.CollisionSprite, healthsprite.HealthSprite):

    ''' Simple object that moves left and right across the screen '''

    def __init__(self, filename, position, world_dim, rectangle, *groups):

        ''' Initializes the obstacle sprite '''

        super(Enemy, self).__init__(filename, position, world_dim, rectangle, *groups)
        healthsprite.HealthSprite.__init__(self,100)
        self.hasplayer = False
        self.attackdistance = 500
    def getPlayer(self, game_sprites):
        for cell in game_sprites:
            if isinstance(cell,player.Player):
                self.hasplayer = True
                return cell
    def distance(self,x1,x2,y1,y2):
        dx = x1-x2
        dy = y1-y2
        d = math.sqrt(dx*dx+dy*dy)
        return d
    def update(self,game_sprites):
        
        
        self.previous = self.rect.copy()
        if not self.hasplayer:
            self.playercharacter = self.getPlayer(game_sprites)
        self.centerx = self.rect.x + self.rect.width/2
        self.centery = self.rect.y + self.rect.height/2
        self.playercenterx = self.playercharacter.rect.x + self.playercharacter.rect.width/2
        self.playercentery = self.playercharacter.rect.y + self.playercharacter.rect.height/2
        if self.distance(self.centerx,self.playercenterx,self.centery,self.playercentery) <= 500:
            if self.centerx < self.playercenterx:
                self.rect.x += 5
            else:
                self.rect.x -= 5
            if self.centery < self.playercentery:
                self.rect.y += 5
            else:
                self.rect.y -= 5
            self.checkEdgeCollisions()
            self.checkCollisions(game_sprites,[obstacle.Obstacle,Enemy])
        ''' Changes the direction of the sprite if it hits the edge of the screen '''

