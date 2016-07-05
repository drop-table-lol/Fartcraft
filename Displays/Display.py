import pygame
import random

SCREEN_WIDTH = 768
SCREEN_LENGTH = 768
TILE_SIZE = 64

HEIGHT_TILES = SCREEN_LENGTH/TILE_SIZE
WIDTH_TILES = SCREEN_WIDTH/TILE_SIZE



# colors
RED = (255, 0, 0)
ORANGE = (255, 153, 153)
YELLOW = (255, 255, 0)
GREEN = (22, 226, 15)
BLUE = (0, 0, 255)
TEAL = (0, 255, 255)
PURPLE = (153, 0, 153)
WHITE = (255, 255, 255)
BROWN = (210, 105, 30)
BLACK = (0, 0, 0)
GREY = (93, 95, 96)
GOLD = (246, 255, 0)
GRASS_GREEN = (73, 170, 16)

ALL_COLORS = [RED, ORANGE, YELLOW, GREEN, BLUE, TEAL, PURPLE, WHITE, BROWN, BLACK, GREY, GOLD]

pygame.init()
FPS = 30 # Frames Per Second
FPSCLOCK = pygame.time.Clock()

CANVAS = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_LENGTH))


class Screen:
	def __init__(self, gridObj):
		self.x = 0
		self.y = 0
		self.width = WIDTH_TILES
		self.height = HEIGHT_TILES
		self.gridObj = gridObj
		
	def update(self):
		CANVAS.fill(GRASS_GREEN)
		self.gridObj.draw(self.x, self.y, self.x + self.width, self.y + self.height)
	
	def scroll(self, direction):
		print "Scrolling..."
		if direction == "UP" and self.y  - 1>= 0:
			self.y -= 1
		elif direction == "DOWN"and self.y + self.height <= self.gridObj.lengthTiles - 1:
			self.y += 1
		elif direction == "RIGHT"and self.x + self.width <= self.gridObj.widthTiles - 1:
			self.x += 1
		elif direction == "LEFT"and self.x - 1 >= 0:
			self.x -= 1
		
			
	def canScroll(self, direction):
		if(direction == "UP" and self.y  - 1 >= 0 or
		direction == "DOWN"and self.y + self.height <= self.gridObj.lengthTiles - 1 or
		direction == "RIGHT"and self.x + self.width <= self.gridObj.widthTiles - 1 or
		direction == "LEFT"and self.x - 1 >= 0):
			return True
		else:
			return False
			
			
			
		
def returnRandomColor():
	randNum = random.randint(0, len(ALL_COLORS) - 1)
	return ALL_COLORS[randNum]