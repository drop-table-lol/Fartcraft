"""Sprites.py"""
import os
import pygame


#Grounds
spr_ground1 = pygame.image.load('PNG'+ os.sep+'spr_ground1.png')
spr_ground2 = pygame.image.load('PNG'+ os.sep+'spr_ground2.png')
spr_ground3 = pygame.image.load('PNG'+ os.sep+'spr_ground3.png')
GROUND_SPRITES = [spr_ground1, spr_ground2, spr_ground3]

#Walls
spr_wall = pygame.image.load('PNG'+ os.sep+'spr_wall.png')

#Heros
spr_player = pygame.image.load('PNG'+ os.sep+'spr_player.png')

#Minions
spr_minion = pygame.image.load('PNG'+ os.sep+'spr_minion.png')

#Menu
spr_menu = pygame.image.load('PNG'+ os.sep+'Menu.png')


#Spawners
spr_crabSpawner = spr_menu = pygame.image.load('PNG'+ os.sep+'CrabSpawner.png')