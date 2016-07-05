"""animation.py
contains different animations with timelines we wish to play, similar to sprites, 
though, we're using sprites as still images rather than sprite sheets, hence this file."""

import pygame
from Displays import Display
import Sprites

class Animation:
	def __init__(self, x,y, type, gridObj):
		self.x = x
		self.y = y
		self.counter = 0
		self.type = type
		self.isActive = True
		gridObj.receiveAnim(self)
		self.rect = pygame.Rect(self.x, self.y, Display.TILE_SIZE, Display.TILE_SIZE)
		if self.type is "slash":
			self.sprite = Sprites.spr_slash
		elif self.type is "arrows":
			self.sprite = Sprites.spr_arrows
		
		
	def draw(self):
		self.counter += 2
		if self.counter < 30:
			self.updateRect()
			Display.CANVAS.blit(self.sprite, self.rect)
		elif self.counter > 30:
			self.isActive = False
		
	
		
	
	def updateRect(self):
		 self.rect = pygame.Rect(self.x*Display.TILE_SIZE, self.y*Display.TILE_SIZE, Display.TILE_SIZE, Display.TILE_SIZE)
		
		
