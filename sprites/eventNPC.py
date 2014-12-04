import pygame 
import obstacle
import utils.soundplayer
import utils.messagemanager
import utils.message
import player
import math
import gamesprite
class eventNPC(gamesprite.GameSprite):

    def __init__(self, filename, position, world_dim, rectangle, *groups):

	super(eventNPC, self).__init__(filename, position, world_dim, rectangle, *groups)
        self.hasplayer = False
        self.msgs = []
        self.setMsg()
        
    def setMsg(self):
        self.msgs.append("You need to go to the right to kill things.")
	self.msgs.append("I like appending things.")
        self.msgRect = pygame.Rect(450,600,800,100)
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
    def displayMsg(self):
        lines = self.msgs
        temprect = self.msgRect
        tempmessagebox = utils.messagemanager.createmessage(lines, temprect)
        tempmessage = utils.message.Message(tempmessagebox,temprect)
        utils.messagemanager.addabsolutemessage("traveler message",tempmessage)
    def update(self,game_sprites,soundplayer):
        if not self.hasplayer:
            self.playercharacter = self.getPlayer(game_sprites)
        self.centerx = self.rect.x + self.rect.width/2
        self.centery = self.rect.y + self.rect.height/2
        self.playercenterx = self.playercharacter.rect.x + self.playercharacter.rect.width/2
        self.playercentery = self.playercharacter.rect.y + self.playercharacter.rect.height/2
        if abs(self.centerx - self.playercenterx) <= 500:
            self.displayMsg()
