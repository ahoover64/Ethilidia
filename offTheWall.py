import pygame
import sprites.player
import sprites.obstacle
import sprites.healthsprite
import utils.gamedata
import utils.camera as camera
import utils.soundplayer

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
        self.game_data = utils.gamedata.GameData(filename, self.sprite_group)
        self.game_data_obj = self.game_data.dictToObjects()
        self.player = self.game_data.player
        self.generatescreen()
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
        self.soundplayer.playmusic("utils/Sounds/testsound.wav")
    def main(self, screen):

        ''' Main function for the game '''

        self.generatemap('gamedata/level1.json')
        
        self.setupsounds()
        clock = pygame.time.Clock()
        basicfont = pygame.font.SysFont(None, 48)



        while 1:
            clock.tick(self.game_data.getGameGlobals()['fps'])
            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    return
                if event.type is pygame.KEYDOWN and event.key is pygame.K_ESCAPE:
                    return
                if event.type is pygame.KEYDOWN:
                    if event.key is pygame.K_1:
                        self.generatemap('gamedata/level1.json')
                    if event.key is pygame.K_2:
                        self.generatemap('gamedata/level2.json')

            self.sprite_group.update(self.sprite_group,self.soundplayer)
            self.checkdeath()
            self.screen_camera.update(self.player)
            self.screen.blit(self.background,self.screen_camera.apply(pygame.Rect(0,0,self.background.get_width(),self.background.get_height())))
            for e in self.sprite_group.sprites():
                self.screen.blit(e.image,self.screen_camera.apply(e.imagerect))
            for e in self.sprite_group.sprites():
                self.drawhealth(e)
            pygame.display.flip()

if __name__ == '__main__':

    pygame.init()
    
    game = OffTheWall()
    screen = game.screen
    OffTheWall().main(screen)
