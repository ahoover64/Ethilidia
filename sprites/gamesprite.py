import pygame 

class GameSprite(pygame.sprite.Sprite):

    ''' Simple player class which allows you to move
        a sprite across the screen with the arrow keys
    '''

    def __init__(self, filename, position, world_dim, *groups):

        ''' Initializes the player sprite '''
        super(GameSprite, self).__init__(*groups)
        self.world_dim = world_dim
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = pygame.rect.Rect(position, self.image.get_size())
