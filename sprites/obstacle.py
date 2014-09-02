import pygame 

class Obstacle(pygame.sprite.Sprite):

    ''' Simple object that moves left and right across the screen '''

    def __init__(self, filename, position, world_dim, *groups):

        ''' Initializes the obstacle sprite '''

        super(Obstacle, self).__init__(*groups)
        self.world_dim = world_dim
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = pygame.rect.Rect(position, self.image.get_size())
        self.offset_x = 10

         
    def update(self):

        ''' Changes the direction of the sprite if it hits the edge of the screen '''

        if self.rect.x + self.rect.width > self.world_dim[0] or self.rect.x < 0:
            self.offset_x *= -1

        self.rect.x += self.offset_x
