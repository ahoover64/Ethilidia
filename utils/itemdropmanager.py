import pygame
import sprites.item
import sprites.sword
import sprites.itemdrop
import random
import math
HEALTH_DROP_RATE = 10
ITEM_DROP_RATE = 15
HEALTH_DROP_INCREASE = 50
MAX_LEVEL = 10
def randomize(percent):
    rnum = random.random()*100
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
def dropitem(rect,maxRarity,maprect,sprite_group,level):
    if randomize(HEALTH_DROP_RATE):
        item = sprites.itemdrop.ItemDrop(level,maxRarity,0,"gamedata/pictures/health.png",(rect.x,rect.y),maprect,(50,50),sprite_group)
    if randomize(ITEM_DROP_RATE):
        if randomize(50):
            item = sprites.itemdrop.ItemDrop(level,maxRarity,1,"gamedata/pictures/chest.png",(rect.x,rect.y),maprect,(50,50),sprite_group)
        else:
            item = sprites.itemdrop.ItemDrop(level,maxRarity,2,"gamedata/pictures/chest.png",(rect.x,rect.y),maprect,(50,50),sprite_group)
def pickupitem(itemdrop, player):
    if itemdrop.itemtype == 0:
        player.heal(HEALTH_DROP_INCREASE)
    elif itemdrop.itemtype == 1:
        level = randomizeLevel(itemdrop.level)
        rarity = generateRarity(itemdrop.maxRarity)
        wdamage, wrange, wattackspeed, description = generateWeapon(level,rarity)
        tempsword = sprites.sword.Sword("Pickup Sword", generateWeaponImage(), description, wdamage, wrange, wattackspeed, rarity, level)
        player.inventory.addItem(tempsword)
    else:
        level = randomizeLevel(itemdrop.level)
        rarity = generateRarity(itemdrop.maxRarity)
        health,reduction,movement,description = generateArmor(level,rarity)
        temparmor = sprites.armor.Armor("Pickup Armor", generateArmorImage(), description, health, reduction, movement, rarity, level)
        player.inventory.addItem(temparmor)
def generateWeapon(level,rarity):
    rnum = random.randrange(100)
    description = []
    if rnum < 50:
        wdamage = ((int)(random.randrange(2))+6)*(level+rarity)
        wrange = 100
        wattackspeed = round(random.random()+4.0,1)+0.1*rarity
        description.append("Long range with Low Damage")
    else:
        wdamage = ((int)(random.randrange(3))+15)*(level+rarity)
        wrange = 40
        wattackspeed = round(random.random()+6.0,1)+0.2*rarity
        description.append("Short range with High Damage")
    return wdamage,wrange,wattackspeed,description
def generateArmor(level,rarity):
    rnum = random.randrange(100)
    description = []
    if rnum < 50:
        health = ((int)(random.randrange(2))+8)*(level+rarity)
        reduction = ((int)(random.randrange(2))+8)*(1+rarity)
        movement = -round((random.random()*0.1+0.4)*(3-rarity),1)
        description.append("Heavy Armor with Movement Reduction")
    else:
        health = ((int)(random.randrange(1))+4)*(level+rarity)
        reduction = ((int)(random.randrange(1))+4)*(1+rarity)
        movement = 0
        description.append("Light Armor")
    return health,reduction,movement,description
def generateArmorImage():
    names = ["Knight Basic"]
    randomIndex = random.randint(0,len(names)-1)
    name = names[randomIndex]
    name = "gamedata/pictures/" + name + ".png"
    return name
def generateWeaponImage():
    names = ["ancientBlade","energySword","heavyBlade","heavySteelSword","ironSword","legendaryBlade","lightsaber","standardSword"]
    randomIndex = random.randint(0,len(names)-1)
    name = names[randomIndex]
    name = "gamedata/pictures/" + name + ".png"
    return name
        





