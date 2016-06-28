""" User input handling """

import pygame
from pygame.locals import *
from Displays import Display
import sys

class Input:

	def __init__(self, screenObj):
		#self.playerHandlerObj = playerHandlerObj
	
		self.screenObj = screenObj
		
	def update(self):
		""" Input event handler """
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				#Selector.openMenu()
				pass
			if event.type == KEYDOWN:
				if event.key == K_LEFT:
					self.playerHandlerObj.move("LEFT")
				elif event.key == K_RIGHT:
					self.playerHandlerObj.move("RIGHT")
				elif event.key == K_DOWN:
					self.playerHandlerObj.move("DOWN")
				elif event.key == K_UP:
					self.playerHandlerObj.move("UP")
				elif event.key == K_a and self.screenObj.canScroll("LEFT"):
					self.screenObj.scroll("LEFT");
					self.playerHandlerObj.scroll("LEFT")
					#self.minionHandlerObj.scroll("LEFT")
				elif event.key == K_s and self.screenObj.canScroll("DOWN"): 
					self.screenObj.scroll("DOWN");
					self.playerHandlerObj.scroll("DOWN")
					#self.minionHandlerObj.scroll("DOWN")
				elif event.key == K_d and self.screenObj.canScroll("RIGHT"):
					self.screenObj.scroll("RIGHT");
					self.playerHandlerObj.scroll("RIGHT")
					#self.minionHandlerObj.scroll("RIGHT")
				elif event.key == K_w and self.screenObj.canScroll("UP"):
					self.screenObj.scroll("UP");
					self.playerHandlerObj.scroll("UP")
					#self.minionHandlerObj.scroll("UP")
				if event.key == K_ESCAPE:
					return True
			elif event.type == KEYUP: # stop moving the player
				'''
				if event.key == K_LEFT:
					self.playerHandlerObj.moveLeft= False
				if event.key == K_RIGHT:
					self.playerHandlerObj.moveRight= False
				if event.key == K_DOWN:
					self.playerHandlerObj.moveDown= False
				if event.key == K_UP:
					self.playerHandlerObj.moveUp= False
				'''
		return False