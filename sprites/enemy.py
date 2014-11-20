import pygame 
import gamesprite
import obstacle
import collisionsprite
import player
import math
import healthsprite
import utils.soundplayer
import animationsprite
class Enemy(collisionsprite.CollisionSprite, animationsprite.AnimationSprite, healthsprite.HealthSprite):

    ''' Simple object that moves left and right across the screen '''

    def __init__(self, filename, position, world_dim, ssinfo, fps, rectangle, level, *groups):

        ''' Initializes the obstacle sprite '''

        super(Enemy, self).__init__(filename, position, world_dim, rectangle, *groups)
        animationsprite.AnimationSprite.__init__(self,filename,position,world_dim,rectangle,ssinfo,fps,*groups)
        healthsprite.HealthSprite.__init__(self,50*level)
        self.hasplayer = False
        self.attackdistance = 500
        self.level = level
        self.attack = 0.1*level
        self.speed = 2.5
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
    def update(self,game_sprites,soundplayer):
        
        self.animationTick()
        self.previous = self.rect.copy()
        if not self.hasplayer:
            self.playercharacter = self.getPlayer(game_sprites)
        self.centerx = self.rect.x + self.rect.width/2
        self.centery = self.rect.y + self.rect.height/2
        self.playercenterx = self.playercharacter.rect.x + self.playercharacter.rect.width/2
        self.playercentery = self.playercharacter.rect.y + self.playercharacter.rect.height/2
        if self.distance(self.centerx,self.playercenterx,self.centery,self.playercentery) <= 500:
            if self.centerx < self.playercenterx:
                self.rect.x += self.speed
            elif self.centerx > self.playercenterx:
                self.rect.x -= self.speed
            else:
                pass
            if self.centery < self.playercentery:
                self.rect.y += self.speed
            elif self.centery > self.playercentery:
                self.rect.y -= self.speed
            else:
                pass
            self.rotateForDirection(self.previous,self.rect,180)
            self.checkEdgeCollisions()
            self.checkCollisions(game_sprites,[obstacle.Obstacle,Enemy])
            self.fixImage()
            self.centerx = self.rect.x + self.rect.width/2
            self.centery = self.rect.y + self.rect.height/2
            if self.distance(self.centerx,self.playercenterx,self.centery,self.playercentery) <= self.rect.width/2+self.playercharacter.rect.width/2:
                self.playercharacter.damage(self.attack)
        ''' Changes the direction of the sprite if it hits the edge of the screen '''

