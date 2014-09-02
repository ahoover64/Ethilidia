import pygame
import sprites.player
import sprites.obstacle
import utils.gamedata

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
        game_data = utils.gamedata.GameData('gamedata/game.json', sprite_group)
        game_data_obj = game_data.dictToObjects()
        self.player = game_data_obj['sprites.player']
        self.obstacle = game_data_obj['sprites.obstacle']

        self.screen = pygame.display.set_mode(game_data.getGameGlobals()['resolution'])
        clock = pygame.time.Clock()
        basicfont = pygame.font.SysFont(None, 48)
        text = basicfont.render('Off The Wall!', True, (255,0,0))
        textrect = text.get_rect()
        textrect.centerx = self.screen.get_rect().centerx
        textrect.centery = 50
        while 1:
            clock.tick(game_data.getGameGlobals()['fps'])
            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    return
                if event.type is pygame.KEYDOWN and event.key is pygame.K_ESCAPE:
                    return

            sprite_group.update()

            self.screen.fill((0,0,0))
            sprite_group.draw(self.screen)
            self.screen.blit(text, textrect)
            pygame.display.flip()

if __name__ == '__main__':

    pygame.init()
    
    game = OffTheWall()
    screen = game.screen
    OffTheWall().main(screen)
