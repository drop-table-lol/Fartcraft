"""Sprites.py"""
import os
import pygame


#TERRAIN ------------------------------------------------------
#Grounds
spr_ground1 = pygame.image.load('PNG'+ os.sep+'spr_ground1.png')
spr_ground2 = pygame.image.load('PNG'+ os.sep+'spr_ground2.png')
spr_ground3 = pygame.image.load('PNG'+ os.sep+'spr_ground3.png')
spr_corpse = pygame.image.load('PNG'+ os.sep+'spr_corpse.png')
GROUND_SPRITES = [spr_ground1, spr_ground2, spr_ground3]



#STRUCTURES----------------------------------------------------
#Walls
spr_wall = pygame.image.load('PNG'+ os.sep+'spr_wall.png')
#Spawners
spr_crabSpawner = pygame.image.load('PNG'+ os.sep+'CrabSpawner.png')
#Towers
spr_tower0 = pygame.image.load('PNG'+ os.sep+'spr_tower0.png')



#UNITS---------------------------------------------------------
#Heros
spr_player = pygame.image.load('PNG'+ os.sep+'spr_player.png')

#Minions

#HellSpawn
spr_minion = pygame.image.load('PNG'+ os.sep+'spr_minion.png')
spr_minion1 = pygame.image.load('PNG'+ os.sep+'spr_minion1.png')

#CrabSpawn
spr_crab = pygame.image.load('PNG'+ os.sep+'CrabMinion0.png')
spr_crab_left = pygame.transform.flip(spr_crab, True, False)
#Sin Sity Slugs
spr_slug = pygame.image.load('PNG'+ os.sep+'SlugMinion0.png')
spr_slug_left = pygame.transform.flip(spr_slug, True, False)

#GUI-----------------------------------------------------------
#Menu
spr_menu = pygame.image.load('PNG'+ os.sep+'Menu.png')
#SweetCursorofgoodness...
spr_cursor = pygame.image.load('PNG'+os.sep+'Cursor.png')


#Attacks--------------------------------------------------------
spr_slash = pygame.image.load('PNG'+os.sep+'spr_slash1.png')
spr_arrows = pygame.image.load('PNG'+os.sep+'spr_arrows.png')
