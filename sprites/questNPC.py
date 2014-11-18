import pygame 
import obstacle
import utils.soundplayer
import utils.messagemanager
import utils.message
import player
import math
import NPC
class quest_NPC(NPC.NPC):

    def __init__(self, filename, position, world_dim, rectangle, *groups):

	super(quest_NPC, self).__init__(filename, position, world_dim, rectangle, *groups)
    def setMsg(self):
        self.msgs.append("Please Destroy The Bad Guys")
        self.msgRect = pygame.Rect(self.rect.centerx-150,self.rect.y-75,300,50)
