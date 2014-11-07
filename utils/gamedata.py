import sys
import json
import pygame
import random
import sprites.player
import sprites.obstacle
import sprites.enemy
from collections import defaultdict

class GameData():

    ''' Loads scene file '''

    class __GameData:

        def __init__(self, scene_file, sprite_group, level):
            self.loadFromJson(scene_file)
            self.sprite_group = sprite_group
            self.playerNotCreated = True
            self.level = level
        def loadFromJson(self, scene_file):
            self.game_globals = dict()
            # open the scene file
            try:
                self.scene_file = open(scene_file, 'r')

            except:
                print "Oops!  Cannot load scene file '" + scene_file + "'!"
                sys.exit(0)

            self.json_scene = json.load(self.scene_file)
            
        def __getGameClassNames__(self):
            return self.json_scene.keys()

        def __getGameGlobals__(self):
            return self.game_globals

	def randomPosition(self, rr, rs):
            rp = [0,0]
            if rr[2]-rr[0] == rs[0] and rr[3]-rr[1] == rs[1]:
	        rp[0] = rr[0]
                rp[1] = rr[1]
            else:
	        rp[0] = random.randrange(rr[0],rr[2]-rs[0],10)
	        rp[1] = random.randrange(rr[1],rr[3]-rs[1],10)
	    return rp
        def randomOpenPosition(self, rr, rs, sprite_group, ignored=[]):
            done = False
            while not done:
                randompos = self.randomPosition(rr,rs)
                tr = pygame.Rect(randompos[0],randompos[1],rs[0],rs[1])
                if not self.isColliding(tr,sprite_group,ignored):
                    done = True
            return randompos
        def isColliding(self,rect,sprite_group,ignored):
            for cell in sprite_group:
                if not self.listInstance(cell,ignored):
                    if (rect.x + rect.width > cell.rect.x) and (rect.x < cell.rect.x + cell.rect.width) and (rect.y + rect.height > cell.rect.y) and (rect.y < cell.rect.y + cell.rect.height):
                        return True
            return False
        def listInstance(self,cell,instances):
            for classdata in instances:
                if isinstance(cell,classdata):
                    return True
            return False
        def __dictToObjects__(self):

            ''' return objects from json data '''
            objects = defaultdict(list)


            for entry in self.json_scene:
                if entry == "gameglobals":
                    for i in range(0,len(self.json_scene[entry])):
                        for gglobal in self.json_scene[entry][i]:
                            self.game_globals[gglobal] = self.json_scene[entry][i][gglobal]

            for entry in self.json_scene:
              if entry != "gameglobals":
                    for i in range(0,len(self.json_scene[entry])):
                        try:
                            if self.json_scene[entry][i]['type'] == "sprites.player":
                                if self.playerNotCreated:
                                    p = sprites.player.Player(self.json_scene[entry][i]['image'],
                                                            self.json_scene[entry][i]['position'],
                                                            self.game_globals['maprect'],
                                                            self.json_scene[entry][i]['ssinfo'],
                                                            self.game_globals['fps'],
                                                            self.game_globals['resolution'],
                                                            self.sprite_group)
                                    self.player = p
                                    self.playerNotCreated = False
                                else:
                                    self.sprite_group.add(self.player)
                                objects[entry].append(self.player)
                                

                            elif self.json_scene[entry][i]['type'] == "sprites.obstacle":
                                for j in range(self.json_scene[entry][i]['number']):
                                    randomp = self.randomOpenPosition(self.json_scene[entry][i]['randomrect'],self.json_scene[entry][i]['size'],self.sprite_group,[sprites.obstacle.Obstacle])
                                    o = sprites.obstacle.Obstacle(self.json_scene[entry][i]['image'],
                                                        randomp,
                                                        self.game_globals['maprect'],
                                                        self.json_scene[entry][i]['size'],
                                                        self.sprite_group)
                                
                                    
                                    objects[entry].append(o)

                            elif self.json_scene[entry][i]['type'] == "sprites.enemy":
                                for j in range(self.json_scene[entry][i]['number']):
                                    randomp = self.randomOpenPosition(self.json_scene[entry][i]['randomrect'],self.json_scene[entry][i]['size'],self.sprite_group)
                                    e = sprites.enemy.Enemy(self.json_scene[entry][i]['image'],
                                                        randomp,
                                                        self.game_globals['maprect'],
                                                        self.json_scene[entry][i]['size'],
                                                        self.level,
                                                        self.sprite_group)
                                
                                    
                                    objects[entry].append(e)

                        except ValueError:
                            print ValueError
                            pass

            return objects

    instance = None

    

    def __init__(self, arg, sprite_group, level):
        if not GameData.instance:
            GameData.instance = GameData.__GameData(arg, sprite_group, level)
        else:
            GameData.instance.loadFromJson(arg)
            GameData.instance.sprite_group = sprite_group
            GameData.instance.level = level
        

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def getGameDataClassNames(self):

        ''' Returns the game data class names '''

        return GameData.instance.__getGameDataClassNames__()

    def dictToObjects(self):

        ''' converts the game data into objects '''

        return GameData.instance.__dictToObjects__()

    def getGameGlobals(self):

        ''' returns the global game data '''

        return GameData.instance.__getGameGlobals__()
