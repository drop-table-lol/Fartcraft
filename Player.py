import pygame
import Display

spr_player = pygame.image.load('spr_player.png')

class Player:
	
	def __init__(self, screenObj, gridObj):
		self.x = 0
		self.y = 0
		
		self.gridObj = gridObj
		self.screenObj = screenObj
		self.size = Display.TILE_SIZE
		self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
		self.moveUp = False
		self.moveDown = False
		self.moveLeft = False
		self.moveRight = False
		self.direction = 'right'
		self.color = (249, 66, 4)
		self.sprite = spr_player
	
	def update(self):
		self.movePlayer()
		self.draw()
		
	def draw(self):
		Display.CANVAS.blit(self.sprite, self.rect)
	
	def updateRect(self):
		self.rect = pygame.Rect(self.x*Display.TILE_SIZE, self.y*Display.TILE_SIZE, self.size, self.size)
	
	def movePlayer(self):
		if self.moveUp or self.moveDown or self.moveLeft or self.moveRight:	
			if self.moveUp and self.y - 1 >= 0 and self.gridObj.tileIsWalkable(self.x, self.y - 1):
				self.y -= 1
				self.moveUp = False
				if self.y - 1 == 0:
					self.screenObj.scroll("UP")
			elif self.moveDown and self.y < Display.HEIGHT_TILES - 1 and self.gridObj.tileIsWalkable(self.x, self.y + 1):
				self.y += 1
				self.moveDown = False
				if self.y + 1 == Display.SCREEN_LENGTH - 1:
					self.screenObj.scroll("DOWN")
			elif self.moveLeft and self.x - 1 >= 0 and self.gridObj.tileIsWalkable(self.x - 1, self.y):
				self.x -= 1
				self.moveLeft = False
				if self.x - 1 == 0:
					self.screenObj.scroll("LEFT")
			elif self.moveRight and self.x < Display.WIDTH_TILES - 1 and self.gridObj.tileIsWalkable(self.x + 1, self.y):
				self.x += 1
				self.moveRight = False
				if self.x + 1 == Display.SCREEN_WIDTH - 1:
					self.screenObj.scroll("RIGHT")
			self.updateRect()