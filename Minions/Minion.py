import pygame
from Displays import Display
import random
import Sprites



class Minion:
	
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.screenX = x
		self.screenY = y
		self.size = Display.TILE_SIZE
		self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
		self.sprite = Sprites.spr_minion
		self.direction = "RIGHT"
		self.speed = 1
		self.didMove = False
	
	
	#DRAWING-----------------------------------------
		
	def draw(self):
		self.updateRect()
		print "drawing Minion(self) at %s, %s" % (self.screenX, self.screenY)
		Display.CANVAS.blit(self.sprite, self.rect)
	
	def updateRect(self):
		self.rect = pygame.Rect(self.screenX*Display.TILE_SIZE, self.screenY*Display.TILE_SIZE, self.size, self.size)
	
	#MOVEMENT-----------------------------------------
	def getSpeed(self):
		return self.speed
				
	def hasMoved(self):
		return self.didMove
		
	def moved(self, bool):
		self.didMove = bool
		
		
	def getRandomDirection(self):
		randNum = random.randint(0, 4)
		if randNum == 0:
			self.direction = "UP"
		elif randNum == 1:
			self.direction = "DOWN"
		elif randNum == 2:
			self.direction = "LEFT"
		elif randNum == 3:
			self.direction = "RIGHT"
			
	def moveDown(self):
		self.y += self.speed
		self.screenY += self.speed
		
	def moveUp(self):
		self.y -= self.speed
		self.screenY -= self.speed
		
	def moveLeft(self):
		self.x -= self.speed
		self.screenX -= self.speed
		
	def moveRight(self):
		self.x += self.speed 
		self.screenX += self.speed