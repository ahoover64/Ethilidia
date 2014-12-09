import enemy
import pygame
import collisionsprite
import math
import random
import utils.soundplayer

class Boss(enemy.Enemy):
    def __init__(self, filename, position, world_dim, ssinfo, fps, rectangle, level, *groups):
        super(Boss, self).__init__(self, filename, position, world_dim, ssinfo, fps, rectangle, level, *groups)
        self.attackdistance = 600
        self.level = level
        self.attack = 0
        self.speed = 2.0
        self.maxRarityDrop = 3
        self.enemydropchance = 0.005

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
            self.checkCollisions(game_sprites,[obstacle.Obstacle,Enemy])
            self.fixImage()
            self.centerx = self.rect.x + self.rect.width/2
            self.centery = self.rect.y + self.rect.height/2
            if self.distance(self.centerx,self.playercenterx,self.centery,self.playercentery) <= self.rect.width/2+self.playercharacter.rect.width/2:
                self.playercharacter.damage(self.attack)
        if random.uniform(0,1) < self.enemydropschance:
            # ADD RANDOM ENEMY TO THE FIELD
