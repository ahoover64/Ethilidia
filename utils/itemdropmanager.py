import pygame
import sprites.item
import sprites.sword
import sprites.itemdrop
import random
import math
HEALTH_DROP_RATE = 10
SWORD_DROP_RATE = 15
HEALTH_DROP_INCREASE = 50
MAX_LEVEL = 10
def randomize(percent):
    rnum = random.randrange(100)
    if rnum < percent:
        return True
    return False
def randomizeLevel(currentLvl):
    if randomize(20):
        lvl = currentLvl + 1
    elif randomize(50):
        lvl = currentLvl
    elif randomize(50):
        lvl = currentLvl - 1
    else:
        lvl = currentLvl - 2
    if lvl < 1:
        lvl = 1
    if lvl > MAX_LEVEL:
        lvl = maxLvl
    return lvl
        
def generateRarity(maxRarity):
    '''each rarity level is twice as likely as the rarity level one higher'''
    rnum = random.randrange(100)
    raritySectionNum = 100/(math.pow(2,maxRarity)-1)
    raritySection = int(rnum/raritySectionNum)
    topSection = 0
    for i in range(maxRarity):
        topSection += math.pow(2,maxRarity-(i+1))
        if (raritySection < topSection):
            return (i)
def dropitem(rect,maprect,sprite_group,level):
    if randomize(HEALTH_DROP_RATE):
        item = sprites.itemdrop.ItemDrop(level,0,"gamedata/pictures/health.png",(rect.x,rect.y),maprect,(50,50),sprite_group)
    if randomize(SWORD_DROP_RATE):
        item = sprites.itemdrop.ItemDrop(level,1,"gamedata/pictures/chest.png",(rect.x,rect.y),maprect,(50,50),sprite_group)
def pickupitem(itemdrop, player):
    if itemdrop.itemtype == 0:
        player.health += HEALTH_DROP_INCREASE
        if player.health > player.maxhealth:
            player.health = player.maxhealth
    else:
        level = randomizeLevel(itemdrop.level)
        rarity = generateRarity(3)
        wdamage, wrange = generateWeapon(level,rarity)
        tempsword = sprites.sword.Sword("Pickup Sword", generateWeaponImage(), "Sword from item Drops", wdamage, wrange, rarity, level)
        player.inventory.addItem(tempsword)
def generateWeapon(level,rarity):
    rnum = random.randrange(100)
    if rnum < 50:
        wdamage = ((int)(random.randrange(2))+6)*(level+rarity)
        wrange = 100
    else:
        wdamage = ((int)(random.randrange(3))+15)*(level+rarity)
        wrange = 40
    return wdamage,wrange
def generateWeaponImage():
    names = ["ancientBlade","energySword","heavyBlade","heavySteelSword","ironSword","legendaryBlade","lightsaber","standardSword"]
    randomIndex = random.randint(0,len(names)-1)
    name = names[randomIndex]
    name = "gamedata/pictures/" + name + ".png"
    return name
        





