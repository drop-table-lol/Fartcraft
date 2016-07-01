"""Sprites.py"""
import os
import pygame


#TERRAIN ------------------------------------------------------
#Grounds
spr_ground1 = pygame.image.load('PNG'+ os.sep+'spr_ground1.png')
spr_ground2 = pygame.image.load('PNG'+ os.sep+'spr_ground2.png')
spr_ground3 = pygame.image.load('PNG'+ os.sep+'spr_ground3.png')
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
spr_minion = pygame.image.load('PNG'+ os.sep+'spr_minion.png')
spr_minion1 = pygame.image.load('PNG'+ os.sep+'spr_minion1.png')


#GUI-----------------------------------------------------------
#Menu
spr_menu = pygame.image.load('PNG'+ os.sep+'Menu.png')
#SweetCursorofgoodness...
spr_cursor = pygame.image.load('PNG'+os.sep+'Cursor.png')