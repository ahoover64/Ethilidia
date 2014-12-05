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

class VeteranEnemy(enemy.Enemy):

	def __init__(self, filename, position, world_dim, ssinfo, fps, rectangle, level, *groups):

		super(VeteranEnemy, self).__init__(filename, position, world_dim, ssinfo, fps, rectangle, level, *groups)

		healthsprite.HealthSprite.__init__(self,75*level)
		self.attack = 0.2*level
                self.maxRarityDrop = 4
