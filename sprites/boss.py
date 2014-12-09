import enemy
import pygame
import collisionsprite
import math
import random
import utils.soundplayer
import obstacle
import healthsprite
class Boss(enemy.Enemy):
    def __init__(self, filename, position, world_dim, ssinfo, fps, rectangle, level, *groups):
        super(Boss, self).__init__(filename, position, world_dim, ssinfo, fps, rectangle, level, *groups)
        healthsprite.HealthSprite.__init__(self,1500*level)
        self.attackdistance = 600
        self.level = level
        self.attack = 0
        self.speed = 2.0
        self.maxRarityDrop = 4
        self.enemydropchance = 0.01
        self.world_dim = world_dim
    def update(self,game_sprites,soundplayer):

        self.animationTick()
        self.previous = self.rect.copy()
        if not self.hasplayer:
            self.playercharacter = self.getPlayer(game_sprites)
        self.centerx = self.rect.x + self.rect.width/2
        self.centery = self.rect.y + self.rect.height/2
        self.playercenterx = self.playercharacter.rect.x + self.playercharacter.rect.width/2
        self.playercentery = self.playercharacter.rect.y + self.playercharacter.rect.height/2
        if self.distance(self.centerx,self.playercenterx,self.centery,self.playercentery) <= 650:
            if self.centerx < self.playercenterx:
                self.rect.x -= self.speed
            elif self.centerx > self.playercenterx:
                self.rect.x += self.speed
            else:
                pass
            if self.centery < self.playercentery:
                self.rect.y -= self.speed
            elif self.centery > self.playercentery:
                self.rect.y += self.speed
            else:
                pass
            self.rotateForDirection(self.previous,self.rect,180)
            self.checkEdgeCollisions()
            self.checkCollisions(game_sprites,[obstacle.Obstacle,enemy.Enemy])
            self.fixImage()
            self.centerx = self.rect.x + self.rect.width/2
            self.centery = self.rect.y + self.rect.height/2
            if self.distance(self.centerx,self.playercenterx,self.centery,self.playercentery) <= self.rect.width/2+self.playercharacter.rect.width/2:
                self.playercharacter.damage(self.attack)
        if random.uniform(0,1) < self.enemydropchance:
            if self.rect.centerx < self.world_dim[0]/2:
                position = [self.rect.x + self.rect.width + 10,self.rect.centery-25]
            else:
                position = [self.rect.x-60, self.rect.centery-25]
            tempenemy = enemy.Enemy("gamedata/pictures/Enemy Sprite Sheet.png", position, self.world_dim, [0,0,4,1,200,200,0,0], self.fps, [50,50], self.level, game_sprites)
            # ADD RANDOM ENEMY TO THE FIELD
