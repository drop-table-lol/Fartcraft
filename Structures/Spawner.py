"""Spawner class"""
import pygame
import Sprites
from Displays import Display
from Minions import Minion

BASE_HEALTH = 5

class Spawner:
	
	def __init__(self, team, x, y, screenX, screenY, gridObj, screenObj):
		self.team = team
		self.x = x
		self.y = y
		self.size = Display.TILE_SIZE
		self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
		self.screenX = screenX
		self.screenY = screenY
		self.sprite = Sprites.spr_crabSpawner
		self.grid = gridObj
		self.screen = screenObj
		
		self.health = BASE_HEALTH
		
		
	def drawSelf(self):
		self.updateRect()
		Display.CANVAS.blit(self.sprite, self.rect)
		
	def updateRect(self):
		self.rect = pygame.Rect(self.screenX*Display.TILE_SIZE, self.screenY*Display.TILE_SIZE, self.size, self.size)
		
	def update(self):
		self.drawSelf()
		
		
	
		
		