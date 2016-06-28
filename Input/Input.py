""" User input handling """

import pygame
from pygame.locals import *
import sys

from Displays import Display

class Input:

	def __init__(self, screenObj, gridObj):
	
		self.screenObj = screenObj
		self.gridObj = gridObj
	def update(self):
		""" Input event handler """
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_a and self.screenObj.canScroll("LEFT"):
					self.screenObj.scroll("LEFT");
					self.gridObj.scroll("LEFT")
				elif event.key == K_s and self.screenObj.canScroll("DOWN"): 
					self.screenObj.scroll("DOWN");
					self.gridObj.scroll("DOWN")
				elif event.key == K_d and self.screenObj.canScroll("RIGHT"):
					self.screenObj.scroll("RIGHT");
					self.gridObj.scroll("RIGHT")
				elif event.key == K_w and self.screenObj.canScroll("UP"):
					self.screenObj.scroll("UP");
					self.gridObj.scroll("UP")
				if event.key == K_ESCAPE:
					return True
			
		return False
		
		