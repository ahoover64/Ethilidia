import pygame 

class Player(pygame.sprite.Sprite):

    ''' Simple player class which allows you to move
        a sprite across the screen with the arrow keys
    '''

    def __init__(self, filename, position, *groups):

        ''' Initializes the player sprite '''

        super(Player, self).__init__(*groups)
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = pygame.rect.Rect(position, self.image.get_size())

    def update(self):

        ''' Moves the player sprite across the screen
            with arrow keys
        '''

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= 10
        if key[pygame.K_RIGHT]:
            self.rect.x += 10
        if key[pygame.K_UP]:
            self.rect.y -= 10
        if key[pygame.K_DOWN]:
            self.rect.y += 10
