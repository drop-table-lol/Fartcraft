"""Tower.py
	TODO add fighting info. RANGED :o 
	Otherwise, basic structure (might wanna make that a superclass, eh?)
"""
"""Spawner class"""
import pygame
import Sprites
from Displays import Display

BASE_HEALTH = 6
BASE_SPEED = 0 #Tiles per turn
BASE_ATTACKS = 2 #Number of attacks per turn
BASE_DAMAGE = 6 #number of d6 dice rolled per attack
BASE_DEFENSE = 1 #number of BASE_ARMOR dice rolled per defense
BASE_ARMOR = 3 #m sided dice is rolled for defense
BASE_INITIATIVE = 1 #Determines who gets to go first

class Tower:
	
	def __init__(self, x, y, team):
		self.handle = "tower"
		self.team = team
		self.x = x
		self.y = y
		self.screenX = x
		self.screenY = y
		self.size = Display.TILE_SIZE
		self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
		self.screenX = x
		self.screenY = y
		self.sprite = Sprites.spr_tower0
		
		self.health = BASE_HEALTH
		self.speed = BASE_SPEED
		self.initiative = BASE_INITIATIVE
		self.defense = BASE_DEFENSE
		self.attacks = BASE_ATTACKS
		self.damage = BASE_DAMAGE
		self.armor = BASE_ARMOR
		self.isDead = False
		
		
		
	#DRAWING-----------------------------------------
	def draw(self):
		self.updateRect()
		Display.CANVAS.blit(self.sprite, self.rect)
		
	def updateRect(self):
		self.rect = pygame.Rect(self.screenX*Display.TILE_SIZE, self.screenY*Display.TILE_SIZE, self.size, self.size)
		
	def update(self):
		self.draw()
		#Check for combat!
		
	def moved(self, bool):
		pass
	
	def getSpeed(self):
		return self.speed
		
		
	#SCROLLING--------------------------------------	
	def scroll(self, dir):
		if dir == "RIGHT":
			self.scrollRight()
		elif dir == "LEFT":
			self.scrollLeft()
		elif dir == "UP":
			self.scrollUp()
		elif dir == "DOWN":
			self.scrollDown()
		
	def scrollRight(self):
		self.screenX -= 1
	def scrollLeft(self):
		self.screenX += 1
	def scrollUp(self):
		self.screenY += 1
	def scrollDown(self):
		self.screenY -= 1
		
	#COMBAT----------------------------------------------
	def death(self):
		print "oh no! Tower down!"
		self.isDead = True
		
	def buff(self, x,y,z):
		pass #TODO, CAN WE BUFF Structures?
		
	def debuff(self,x,y,z):
		pass
		
		
		
		
		
		
		