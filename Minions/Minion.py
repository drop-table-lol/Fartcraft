import pygame
from Displays import Display
import random
import Sprites



class Minion:
	
	def __init__(self, x, y, sprite):
		self.x = x
		self.y = y
		self.screenX = x
		self.screenY = y
		self.size = Display.TILE_SIZE
		self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
		self.moveUp = False
		self.moveDown = False
		self.moveLeft = False
		self.moveRight = False
		self.sprite = sprite
		self.direction = "UP"
	
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
			if self.moveDown:
				self.y += 1
				self.screenY += 1
				self.moveDown = False
			if self.moveLeft:
				self.x -= 1
				self.screenX -= 1
				self.moveLeft = False
			if self.moveRight:
				self.x += 1
				self.screenX += 1
				self.moveRight = False

			
class MinionHandler:
	def __init__(self, gridObj, screenObj, numMinions):
		self.gridObj = gridObj
		self.screenObj = screenObj
		self.listMinions = []
		for x in range(numMinions):
			self.listMinions.append(Minion(3, 3, Sprites.spr_minion))
	
	def update(self):
		for minion in self.listMinions:
			if not self.move(minion, minion.direction):
				minion.direction = self.getRandomDirection()
			minion.update()
	
	def move(self, minion, direction):
		if direction == "UP" and minion.y - 1 >= 0 and self.gridObj.tileIsWalkable(minion.x, minion.y - 1):
			minion.moveUp = True
		elif direction == "DOWN" and minion.y < self.gridObj.lengthTiles - 1 and self.gridObj.tileIsWalkable(minion.x, minion.y + 1):
			minion.moveDown = True
		elif direction == "LEFT" and minion.x - 1 >= 0 and self.gridObj.tileIsWalkable(minion.x - 1, minion.y):
			minion.moveLeft = True
		elif direction == "RIGHT" and minion.x < self.gridObj.widthTiles - 1 and self.gridObj.tileIsWalkable(minion.x + 1, minion.y):
			minion.moveRight = True
		else:
			return False
		return True
	
	def scroll(self, direction):
		if direction == "UP":
			for minion in self.listMinions:
				minion.screenY += 1
		if direction == "DOWN":
			for minion in self.listMinions:
				minion.screenY -= 1
		if direction == "LEFT":
			for minion in self.listMinions:
				minion.screenX += 1
		if direction == "RIGHT":
			for minion in self.listMinions:
				minion.screenX -= 1
	
	def getRandomDirection(self):
		randNum = random.randint(0, 4)
		if randNum == 0:
			return "UP"
		elif randNum == 1:
			return "DOWN"
		elif randNum == 2:
			return "LEFT"
		elif randNum == 3:
			return "RIGHT"
			