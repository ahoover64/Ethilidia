import pygame
import sprites.player
import sprites.obstacle
import sprites.healthsprite
import utils.gamedata
import utils.camera as camera
import utils.soundplayer
import utils.messagemanager
import utils.message
import sprites.NPC
import sprites.questNPC
import random
import sprites.itemdrop
class OffTheWall(object):

    ''' OffTheWall is a simple python game
        that features a player sprite as well
        as obstacles that move across the screen
    '''

    def __init__(self):

        ''' Initialize game data '''

        self.screen = None 

    def generatemap(self, filename):
        self.sprite_group = pygame.sprite.Group()
        self.game_data = utils.gamedata.GameData(filename, self.sprite_group, self.level)
        self.game_data_obj = self.game_data.dictToObjects()
        self.player = self.game_data.player
        self.generatescreen()
        self.player.world_dim = self.game_data.getGameGlobals()['maprect']
        self.player.createcamera(self.game_data.getGameGlobals()['resolution'][0],self.game_data.getGameGlobals()['resolution'][1])
    def generatescreen(self):
        self.screen = pygame.display.set_mode(self.game_data.getGameGlobals()['resolution'])
        FULL_MAP_WIDTH = self.game_data.getGameGlobals()['maprect'][0]
        FULL_MAP_HEIGHT = self.game_data.getGameGlobals()['maprect'][1]
        WIN_WIDTH = self.game_data.getGameGlobals()['resolution'][0]
        WIN_HEIGHT = self.game_data.getGameGlobals()['resolution'][1]
        self.screen_camera = camera.Camera(camera.complex_camera,FULL_MAP_WIDTH,FULL_MAP_HEIGHT,WIN_WIDTH,WIN_HEIGHT)
        self.background = pygame.transform.scale(pygame.image.load(self.game_data.getGameGlobals()['backgroundimage']), self.game_data.getGameGlobals()['maprect'])
        self.player.createcamera(WIN_WIDTH,WIN_HEIGHT)
    def checkdeath(self):
        for cell in self.sprite_group:
            if isinstance(cell,sprites.healthsprite.HealthSprite):
                if cell.dead:
                    self.sprite_group.remove(cell)
                    self.soundplayer.playsound("death")
                    self.dropitem(cell.rect)
    def dropitem(self,rect):
        rnum = random.randrange(100)
        if rnum < 50:
            item = sprites.itemdrop.ItemDrop(self.level,1,None,(rect.x,rect.y),self.game_data.getGameGlobals()['maprect'],(50,50),self.sprite_group)
    def drawhealth(self,cell):
        if isinstance(cell,sprites.healthsprite.HealthSprite):
            temprect = pygame.Rect(cell.rect.x,cell.rect.y-15,cell.rect.width,10)
            temprect2 = pygame.Rect(cell.rect.x,cell.rect.y-15,cell.rect.width*cell.health/cell.maxhealth,10)
            colorvalue = cell.health*255/cell.maxhealth
            
            pygame.draw.rect(self.screen,(255-colorvalue,colorvalue,0),self.screen_camera.apply(temprect2))
            pygame.draw.rect(self.screen,(0,0,0),self.screen_camera.apply(temprect),2)
    def setupsounds(self):
        self.soundplayer = utils.soundplayer.SoundPlayer()
        self.soundplayer.addsound("utils/Sounds/hit.wav","hit")
        self.soundplayer.addsound("utils/Sounds/deathsound.wav","death")
        self.soundplayer.stopmusic()
        self.soundplayer.playmusic(self.game_data.getGameGlobals()['gamemusic'])
    def enemiesLeft(self):
        enemyNum = 0
        for cell in self.sprite_group:
            if isinstance(cell,sprites.enemy.Enemy):
                enemyNum += 1
        return enemyNum
    def nextLevel(self):
        self.level += 1
        if self.level > self.maxLevel:
            self.level = self.maxLevel
        elif self.level > self.currentMaxLevel:
            self.level = self.currentMaxLevel
        elif self.level == self.currentMaxLevel:
            self.loadMessage()
            self.generatemap('gamedata/uncompleted.json')
            self.player.rect.x = 10
        else:
            self.loadMessage()
            self.generatemap('gamedata/completed.json')
            self.player.rect.x = 10
    def previousLevel(self):
        self.level -= 1
        if self.level < 1:
            self.level = 1
        elif self.level == 1:
            self.loadMessage()
            self.generatemap('gamedata/town.json')
            self.player.rect.x = self.game_data.getGameGlobals()['maprect'][0]-self.player.rect.width-10
            if self.currentMaxLevel > self.maxLevel:
                lines = []
                lines.append("Thank You Traveler")
                self.changeNPCMsg(lines,sprites.NPC.NPC)
                lines2 = []
                lines2.append("You Defeated All of the Enemies")
                self.changeNPCMsg(lines2,sprites.questNPC.quest_NPC)
        else:
            self.loadMessage()
            self.generatemap('gamedata/completed.json')
            self.player.rect.x = self.game_data.getGameGlobals()['maprect'][0]-self.player.rect.width-10
    def checkPlayerShift(self):
        if self.player.rect.x <= 0:
            self.previousLevel()
        elif self.player.rect.x >= self.game_data.getGameGlobals()['maprect'][0]-self.player.rect.width:
            self.nextLevel()
    def loadMessage(self):
        lines = []
        lines.append("Loading...")
        temprect = pygame.Rect(self.game_data.getGameGlobals()['resolution'][0]-100,self.game_data.getGameGlobals()['resolution'][1]-25,100,25)
        tempmessagebox = utils.messagemanager.createmessage(lines, temprect)
        tempmessage = utils.message.Message(tempmessagebox,temprect)
        self.screen.blit(tempmessage.messagebox,tempmessage.rect)
        pygame.display.flip()
    def changeNPCMsg(self,lines,NPCType):
        for cell in self.sprite_group.sprites():
            if isinstance(cell,NPCType):
                cell.msgs = lines
    def main(self, screen):

        ''' Main function for the game '''
        self.level = 1
        self.currentMaxLevel = 1
        self.maxLevel = 10
        self.generatemap('gamedata/town.json')
        
        self.setupsounds()
        clock = pygame.time.Clock()
        basicfont = pygame.font.SysFont(None, 48)
        
        '''Testing Stuff(remove when finished)'''

        '''End of Testing Stuff'''
        
        while 1:
            clock.tick(self.game_data.getGameGlobals()['fps'])
            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    return
                if event.type is pygame.KEYDOWN and event.key is pygame.K_ESCAPE:
                    return
                if event.type is pygame.KEYDOWN:
                    pass
            
            self.sprite_group.update(self.sprite_group,self.soundplayer)
            self.checkdeath()
            
            self.screen_camera.update(self.player)
            self.screen.blit(self.background,self.screen_camera.apply(pygame.Rect(0,0,self.background.get_width(),self.background.get_height())))
            for e in self.sprite_group.sprites():
                self.screen.blit(e.image,self.screen_camera.apply(e.imagerect))
            for e in self.sprite_group.sprites():
                self.drawhealth(e)
            self.player.inventory.displayInventory(self.screen)

            for message in utils.messagemanager.absolutemessages:
                self.screen.blit(message.messagebox,message.rect)
            for message in utils.messagemanager.nonabsolutemessages:
                self.screen.blit(message.messagebox,self.screen_camera.apply(message.rect))
            utils.messagemanager.resetmessages()
            pygame.display.flip()


            enemies = self.enemiesLeft()
            if enemies == 0 and self.level == self.currentMaxLevel:
                self.currentMaxLevel += 1
                '''play sound'''
            self.checkPlayerShift()
            

if __name__ == '__main__':

    pygame.init()
    
    game = OffTheWall()
    screen = game.screen
    OffTheWall().main(screen)
