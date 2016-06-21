""" User input handling """

import pygame
from pygame.locals import *
import Display
import sys

class Input:

	def __init__(self):
		pass
		
	def update(self, playerObj):
		""" Input event handler """
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_LEFT:
					playerObj.moveLeft= True
					playerObj.direction = 'left'
				elif event.key == K_RIGHT:
					playerObj.moveRight= True
					playerObj.direction = 'right'
				elif event.key == K_DOWN:
					playerObj.moveDown= True
					playerObj.direction = 'down'
				elif event.key == K_UP:
					playerObj.moveUp= True
					playerObj.direction = 'up'
				if event.key == K_ESCAPE:
					return True
			elif event.type == KEYUP: # stop moving the player
				if event.key == K_LEFT:
					playerObj.moveLeft= False
				if event.key == K_RIGHT:
					playerObj.moveRight= False
				if event.key == K_DOWN:
					playerObj.moveDown= False
				if event.key == K_UP:
					playerObj.moveUp= False
		return False