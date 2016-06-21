import pygame
import Display
import random

spr_ground1 = pygame.image.load('spr_ground1.png')
spr_ground2 = pygame.image.load('spr_ground2.png')
spr_ground3 = pygame.image.load('spr_ground3.png')
GROUND_SPRITES = [spr_ground1, spr_ground2, spr_ground3]
spr_wall = pygame.image.load('spr_wall.png')

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
			self.grid.append([])
			for y in xrange(0, self.lengthTiles):
				if random.randint(0, 2) > 0 or (x == 0 and y == 0) or (x == 1 and y == 0) or (x == 0 and y == 1):
					self.grid[x].append(Tile(GROUND_SPRITES[random.randint(0, len(GROUND_SPRITES) - 1)], x, y, True))
				else:
					self.grid[x].append(Tile(spr_wall, x, y, False))
				
				
	def draw(self, x, y, width, height):
		for i in xrange(x, width):
			for j in xrange(y, height):
				self.grid[i][j].draw()
			
	
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
	
	def draw(self):
		Display.CANVAS.blit(self.sprite, self.rect)
		Display.CANVAS.blit(self.text, (self.x*Display.TILE_SIZE, self.y*Display.TILE_SIZE))
		
