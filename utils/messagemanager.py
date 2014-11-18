import pygame
import message
absolutemessages = []
nonabsolutemessages = []
ROW_HEIGHT = 40
TOP_BUFFER = 5
LEFT_BUFFER = 5


def addabsolutemessage(messagename,message):
    absolutemessages.append(message)
def addnonabsolutemessage(messagename,message):
    nonabsolutemessages.append(message)
def resetmessages():
    del absolutemessages[:]
    del nonabsolutemessages[:]
def createmessage(lines,rect):
    basicfont = pygame.font.SysFont(None, 24)
    messagebox = pygame.Surface((rect.width,rect.height))
    messagebox.fill((255,255,255))
    pygame.draw.rect(messagebox,(0,0,0),pygame.Rect(0,0,rect.width,rect.height),5)
    row = 0
    for line in lines:
        text = basicfont.render(line, True, (0,0,0))
	textrect = text.get_rect()
	textrect.x = LEFT_BUFFER
	textrect.y = TOP_BUFFER+row*ROW_HEIGHT
        messagebox.blit(text, textrect)
        row += 1
    return messagebox
