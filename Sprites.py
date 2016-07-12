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

#HellSpawn
spr_minion = pygame.image.load('PNG'+ os.sep+'spr_minion.png')
spr_minion1 = pygame.image.load('PNG'+ os.sep+'spr_minion1.png')

#Crabtopia
spr_crab = pygame.image.load('PNG'+ os.sep+'CrabMinion0.png')
spr_crab_left = pygame.transform.flip(spr_crab, True, False)
#Sin Sity Slugers
spr_slug = pygame.image.load('PNG'+ os.sep+'SlugMinion0.png')
spr_slug_left = pygame.transform.flip(spr_slug, True, False)

#GUI-----------------------------------------------------------
#Menu
spr_console = pygame.image.load('PNG'+ os.sep+'Console.png')
#Commands
spr_build = pygame.image.load('PNG'+ os.sep+'Build.png')
spr_attack = pygame.image.load('PNG'+ os.sep+'Attack.png')
spr_spawnMinion = pygame.image.load('PNG'+ os.sep+'SpawnMinion.png')
spr_pass = pygame.image.load('PNG'+ os.sep+'Pass.png')
sprCommands = []
sprCommands.append(spr_build)
sprCommands.append(spr_attack)
sprCommands.append(spr_spawnMinion)
sprCommands.append(spr_pass)

#SweetCursorofgoodness...
spr_cursor = pygame.image.load('PNG'+os.sep+'Cursor.png')

#ANIMATIONS--------------------------------------------------------
#Attacks
spr_slash = pygame.image.load('PNG'+os.sep+'spr_slash1.png')
spr_arrows = pygame.image.load('PNG'+os.sep+'spr_arrows.png')

#Corpses
spr_corpse = pygame.image.load('PNG'+os.sep+'spr_corpse.png')
spr_rubble = pygame.image.load('PNG'+os.sep+'rubble.png')