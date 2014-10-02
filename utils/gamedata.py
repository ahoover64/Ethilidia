import sys
import json
import pygame
import sprites.player
import sprites.obstacle
from collections import defaultdict

class GameData():

    ''' Loads scene file '''

    class __GameData:

        def __init__(self, scene_file, sprite_group):
            self.game_globals = dict()
            # open the scene file
            try:
                self.scene_file = open(scene_file, 'r')

            except:
                print "Oops!  Cannot load scene file '" + scene_file + "'!"
                sys.exit(0)

            self.json_scene = json.load(self.scene_file)
            self.sprite_group = sprite_group

        def __getGameClassNames__(self):
            return self.json_scene.keys()

        def __getGameGlobals__(self):
            return self.game_globals

        def __dictToObjects__(self):

            ''' return objects from json data '''
            objects = defaultdict(list)


            for entry in self.json_scene:
                if entry == "gameglobals":
                    for i in range(0,len(self.json_scene[entry])):
                        print self.json_scene[entry][i]
                        for gglobal in self.json_scene[entry][i]:
                            print self.json_scene[entry][i][gglobal]
                            self.game_globals[gglobal] = self.json_scene[entry][i][gglobal]

            for entry in self.json_scene:
              if entry != "gameglobals":
                    for i in range(0,len(self.json_scene[entry])):
                        try:
                            if self.json_scene[entry][i]['type'] == "sprites.player":
                                p = sprites.player.Player(self.json_scene[entry][i]['image'],
                                                        self.json_scene[entry][i]['position'],
                                                        self.game_globals['resolution'],
                                                        self.sprite_group)
                                new_obj = {entry:p}
                                objects[entry].append(p)

                            elif self.json_scene[entry][i]['type'] == "sprites.obstacle":
                                o = sprites.obstacle.Obstacle(self.json_scene[entry][i]['image'],
                                                        self.json_scene[entry][i]['position'],
                                                        self.game_globals['resolution'],
                                                        self.json_scene[entry][i]['size'],
                                                        self.sprite_group)
                                new_obj = {entry:o}
                                objects[entry].append(o)

                        except:
                            pass

            return objects

    instance = None

    def __init__(self, arg, sprite_group):
        if not GameData.instance:
            GameData.instance = GameData.__GameData(arg, sprite_group)
        else:
            GameData.instance.val = arg

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
