""" User input handling """

import pygame
from pygame.locals import *
import Display
import sys

class Input:

	def __init__(self):
		pass
		
	def update(self, playerObj, displayObj):
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
				elif event.key == K_a and displayObj.canScroll("LEFT"):
					displayObj.scroll("LEFT");
					playerObj.screenX += 1
				elif event.key == K_s and displayObj.canScroll("DOWN"): 
					displayObj.scroll("DOWN");
					playerObj.screenY -= 1
				elif event.key == K_d and displayObj.canScroll("RIGHT"):
					displayObj.scroll("RIGHT");
					playerObj.screenX -= 1
				elif event.key == K_w and displayObj.canScroll("UP"):
					displayObj.scroll("UP");
					playerObj.screenY += 1
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