import pygame
class Camera(object):
    def __init__(self, camera_func, width, height, winwidth, winheight):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height)
        self.WIN_WIDTH = winwidth
        self.WIN_HEIGHT = winheight
        self.HALF_WIDTH = int(winwidth/2)
        self.HALF_HEIGHT = int(winheight/2)

    def apply(self, targetrect):
        return targetrect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect, self.WIN_WIDTH,self.WIN_HEIGHT,self.HALF_WIDTH,self.HALF_HEIGHT)

def simple_camera(camera, target_rect,WIN_WIDTH,WIN_HEIGHT,HALF_WIDTH,HALF_HEIGHT):
    l, t, rw, rh = target_rect
    _, _, w, h = camera
    return pygame.Rect(-l-rw/2+HALF_WIDTH, -t-rh/2+HALF_HEIGHT, w, h)

def complex_camera(camera, target_rect, WIN_WIDTH,WIN_HEIGHT,HALF_WIDTH,HALF_HEIGHT):
    l, t, rw, rh = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l-rw/2+HALF_WIDTH, -t-rh/2+HALF_HEIGHT, w, h

    l = min(0, l)                           # stop scrolling at the left edge
    l = max(-(camera.width-WIN_WIDTH), l)   # stop scrolling at the right edge
    t = max(-(camera.height-WIN_HEIGHT), t) # stop scrolling at the bottom
    t = min(0, t)                           # stop scrolling at the top
    return pygame.Rect(l, t, w, h)
