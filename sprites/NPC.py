import pygame 
import obstacle
import utils.soundplayer
class NPC(obstacle.Obstacle):

	def __init__(self, filename, position, world_dim, rectangle, *groups):

		super(NPC, self).__init__(filename, position, world_dim, rectangle, *groups)

	def update(self, game_sprites, soundplayer):
		
		pass
