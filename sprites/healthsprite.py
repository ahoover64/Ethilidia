import pygame 
class HealthSprite(object):

    ''' Simple object that moves left and right across the screen '''

    def __init__(self, health):

        ''' Initializes the obstacle sprite '''

        self.health = health
        self.maxhealth = health
        self.dead = False
    def damage(self, damagetaken):
        self.health -= damagetaken
        if self.health <= 0:
            self.dead = True
    def heal(self,healing):
        self.health += healing
        if self.health > maxhealth:
            self.health = maxhealth
    def update(self):
        pass
        ''' Changes the direction of the sprite if it hits the edge of the screen '''

