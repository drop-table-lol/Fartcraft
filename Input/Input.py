""" User input handling """

import pygame
from pygame.locals import *
import sys

from Displays import Display
import ClickPlacement #For building shiz on the fly...
from Structures import Wall

class Input:

	def __init__(self, screenObj, gridObj):
	
		self.screenObj = screenObj
		self.gridObj = gridObj
		self.xScroll = 0
		self.yScroll = 0 	#These two vars should allow us to keep track of the number of scrolls,
							#Allowing us to then pass the param to build-to-click stuff, 
							#Which will allow us to calculate the tile intended for building shit on.
	def update(self):
		""" Input event handler """
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_a and self.screenObj.canScroll("LEFT"):
					self.screenObj.scroll("LEFT");
					self.gridObj.scroll("LEFT")
					self.xScroll -= 1
				elif event.key == K_s and self.screenObj.canScroll("DOWN"): 
					self.screenObj.scroll("DOWN");
					self.gridObj.scroll("DOWN")
					self.yScroll += 1
				elif event.key == K_d and self.screenObj.canScroll("RIGHT"):
					self.screenObj.scroll("RIGHT");
					self.gridObj.scroll("RIGHT")
					self.xScroll += 1
				elif event.key == K_w and self.screenObj.canScroll("UP"):
					self.screenObj.scroll("UP");
					self.gridObj.scroll("UP")
					self.yScroll -= 1
				if event.key == K_ESCAPE:
					return True
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = ClickPlacement.calculateTile(self.xScroll, self.yScroll)
				if self.gridObj.grid[pos[2]][pos[3]].object is not "empty":
					if self.gridObj.grid[pos[2]][pos[3]].object.handle is "wall":
						self.gridObj.grid[pos[2]][pos[3]].object = "empty"
				else:				
					self.gridObj.grid[pos[2]][pos[3]].recieveObject(Wall.Wall(pos[2], pos[3], pos[0], pos[1], 0))
	
			
		return False
		
		