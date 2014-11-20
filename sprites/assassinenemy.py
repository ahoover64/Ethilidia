import pygame 
import gamesprite
import obstacle
import collisionsprite
import player
import math
import healthsprite
import utils.soundplayer
import animationsprite
import enemy

class AssassinEnemy(enemy.Enemy):

	def __init__(self, filename, position, world_dim, ssinfo, fps, rectangle, level, *groups):

		super(AssassinEnemy, self).__init__(filename, position, world_dim, ssinfo, fps, rectangle, level, *groups)

		healthsprite.HealthSprite.__init__(self,25*level)
		self.attack = 0.15*level
		self.speed = 7.5
