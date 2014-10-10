import pygame
import sprites.player
import sprites.obstacle
import utils.gamedata
import utils.camera as camera
class OffTheWall(object):

    ''' OffTheWall is a simple python game
        that features a player sprite as well
        as obstacles that move across the screen
    '''

    def __init__(self):

        ''' Initialize game data '''

        self.screen = None 

    def main(self, screen):

        ''' Main function for the game '''

        sprite_group = pygame.sprite.Group()
        game_data = utils.gamedata.GameData('gamedata/level1.json', sprite_group)
        game_data_obj = game_data.dictToObjects()
        self.player = game_data.player
        

        
        
        self.screen = pygame.display.set_mode(game_data.getGameGlobals()['resolution'])
        FULL_MAP_WIDTH = game_data.getGameGlobals()['maprect'][0]
        FULL_MAP_HEIGHT = game_data.getGameGlobals()['maprect'][1]
        WIN_WIDTH = game_data.getGameGlobals()['resolution'][0]
        WIN_HEIGHT = game_data.getGameGlobals()['resolution'][1]
        screen_camera = camera.Camera(camera.complex_camera,FULL_MAP_WIDTH,FULL_MAP_HEIGHT,WIN_WIDTH,WIN_HEIGHT)
        clock = pygame.time.Clock()
        self.background = pygame.transform.scale(pygame.image.load(game_data.getGameGlobals()['backgroundimage']), game_data.getGameGlobals()['maprect'])
        basicfont = pygame.font.SysFont(None, 48)
        text = basicfont.render('Off The Wall!', True, (255,0,0))
        textrect = text.get_rect()
        textrect.centerx = self.screen.get_rect().centerx
        textrect.centery = 50
        fpsText = basicfont.render('FPS: ' + str(game_data.getGameGlobals()['fps']), True, (255,0,0))
        fpsTextRect = fpsText.get_rect()
        fpsTextRect.centerx = 60
        fpsTextRect.centery = 30

        while 1:
            clock.tick(game_data.getGameGlobals()['fps'])
            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    return
                if event.type is pygame.KEYDOWN and event.key is pygame.K_ESCAPE:
                    return

            timeText = basicfont.render('Time: ' + str(pygame.time.get_ticks()/1000), True, (255,0,0))
            timeTextRect = timeText.get_rect()
            timeTextRect.centerx = 60
            timeTextRect.centery = 80

            sprite_group.update(sprite_group)
            screen_camera.update(self.player)
            self.screen.blit(self.background,screen_camera.apply(pygame.Rect(0,0,self.background.get_width(),self.background.get_height())))
            for e in sprite_group.sprites():
                self.screen.blit(e.image,screen_camera.apply(e.rect))
            pygame.display.flip()

if __name__ == '__main__':

    pygame.init()
    
    game = OffTheWall()
    screen = game.screen
    OffTheWall().main(screen)
