import pygame
class SoundPlayer(object):

    def __init__(self):
        pygame.mixer.pre_init(22050, 16, 2, 4096)
        self.player = pygame.mixer.init()
        self.sounds = {}
        pass
    def addsound(self,filename,soundname):
        self.sounds[soundname] = pygame.mixer.Sound(filename)
        pass
    def playsound(self,name):
        self.sounds[name].play()
        pass
    def playmusic(self,filename):
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play(-1)
        pass
    def stopmusic(self):
        pygame.mixer.music.stop()
        pass
