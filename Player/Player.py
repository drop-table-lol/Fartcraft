import pygame
from Displays import Display
import Sprites


class Player:
	
	def __init__(self, screenObj, gridObj, x, y, sprite):
		self.x = x
		self.y = y
		self.screenX = x
		self.screenY = y
		self.gridObj = gridObj
		self.screenObj = screenObj
		self.size = Display.TILE_SIZE
		self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
		self.moveUp = False
		self.moveDown = False
		self.moveLeft = False
		self.moveRight = False
		self.sprite = sprite
	
	def update(self):
		self.move()
		self.draw()
		
	def draw(self):
		self.updateRect()
		Display.CANVAS.blit(self.sprite, self.rect)
	
	def updateRect(self):
		self.rect = pygame.Rect(self.screenX*Display.TILE_SIZE, self.screenY*Display.TILE_SIZE, self.size, self.size)
	
	def move(self):
		if self.moveUp or self.moveDown or self.moveLeft or self.moveRight:	
			if self.moveUp:
				self.y -= 1
				self.screenY -= 1
				self.moveUp = False
			elif self.moveDown:
				self.y += 1
				self.screenY += 1
				self.moveDown = False
			elif self.moveLeft:
				self.x -= 1
				self.screenX -= 1
				self.moveLeft = False
			elif self.moveRight:
				self.x += 1
				self.screenX += 1
				self.moveRight = False
				
class PlayerHandler:
	def __init__(self, gridObj, screenObj):
		self.playerObj = Player(screenObj, gridObj, 0, 0, Sprites.spr_player)
		self.gridObj = gridObj
		self.screenObj = screenObj
		self.playerHasMoved = False
		
	
	def update(self):
		self.playerObj.update()
			
	def move(self, direction):
		if direction == "UP" and self.playerObj.y - 1 >= 0 and self.gridObj.tileIsWalkable(self.playerObj.x, self.playerObj.y - 1):
			self.playerObj.moveUp = True
		elif direction == "DOWN" and self.playerObj.y < self.gridObj.lengthTiles - 1 and self.gridObj.tileIsWalkable(self.playerObj.x, self.playerObj.y + 1):
			self.playerObj.moveDown = True
		elif direction == "LEFT" and self.playerObj.x - 1 >= 0 and self.gridObj.tileIsWalkable(self.playerObj.x - 1, self.playerObj.y):
			self.playerObj.moveLeft = True
		elif direction == "RIGHT" and self.playerObj.x < self.gridObj.widthTiles  - 1 and self.gridObj.tileIsWalkable(self.playerObj.x + 1, self.playerObj.y):
			self.playerObj.moveRight = True
		else:
			return False
		self.playerHasMoved = True
		return True
	
	def scroll(self, direction):
		if direction == "UP":
			self.playerObj.screenY += 1
		if direction == "DOWN":
			self.playerObj.screenY -= 1
		if direction == "LEFT":
			self.playerObj.screenX += 1
		if direction == "RIGHT":
			self.playerObj.screenX -= 1
	
	def returnPlayerObj(self):
		return self.playerObj
	
	def returnPlayerHasMoved(self):
		if self.playerHasMoved:
			self.playerHasMoved = False
			return True
		else:
			return False
			