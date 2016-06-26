import pygame
from Displays import Display
import random
import Sprites


class Grid:
	def __init__(self):
		self.lengthTiles = 20
		self.widthTiles = 20
		self.grid = []
		self.initialize()
		
	def update(self):
		pass
		#self.draw()
	
	def initialize(self):
		for x in xrange(0, self.widthTiles):
			#self.grid.append([])
			tempList = []
			for y in xrange(0, self.lengthTiles):
				#if random.randint(0, 3) > 0 or (x == 0 and y == 0) or (x == 1 and y == 0) or (x == 0 and y == 1):
				tempList.append(Tile(Sprites.GROUND_SPRITES[random.randint(0, len(Sprites.GROUND_SPRITES) - 1)], x, y, True))
				#else:
				#	tempList.append(Tile(Sprites.spr_wall, x, y, False))
			self.grid.append(tempList)
				
				
	def draw(self, x, y, width, height):
		for i in xrange(x, width):
			for j in xrange(y, height):
				self.grid[i][j].draw(i - x, j - y)
			
	
	def tileIsWalkable(self, x, y):
		return self.grid[x][y].collision
	
class Tile:
	def __init__(self, sprite, x, y, collision):
		self.sprite = sprite
		self.x = x
		self.y = y
		self.collision = collision
		self.rect = pygame.Rect(self.x*Display.TILE_SIZE, self.y*Display.TILE_SIZE, Display.TILE_SIZE, Display.TILE_SIZE)
		self.text = pygame.font.SysFont("monospace", 12).render("(" + str(x) + "," + str(y) + ")", 1, (0,0,0))	
	
	def draw(self, displayX, displayY):
		drawRect = pygame.Rect(displayX*Display.TILE_SIZE, displayY*Display.TILE_SIZE, Display.TILE_SIZE, Display.TILE_SIZE)
		Display.CANVAS.blit(self.sprite, drawRect)
		Display.CANVAS.blit(self.text, (displayX*Display.TILE_SIZE, displayY*Display.TILE_SIZE))
		