"""Hero.py

HEROS are the main characters per faction. They allow building of structures,
advanced unit tactics, and are excellent fighters. They provide a way to change
the course of battle through a single unit. 
Here, we are setting it up for the player-input."""

import pygame
from Displays import Display
import random
import Sprites


class Hero:
	
	def __init__(self, x, y, scrollX, scrollY, team):
		self.handle = "hero"
		self.x = x
		self.y = y
		self.screenX = scrollX
		self.screenY = scrollY
		self.size = Display.TILE_SIZE
		self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
		self.team = team
		self.sprite = Sprites.spr_player
		self.didMove = False
		self.direction = "RIGHT"
		

		
		#COMBAT------------------------------
		self.health = 5
		self.speed = 1
		self.attacks = 2
		self.damage = 1
		self.defense = 1
		self.initiative = 5
		self.buffsActive = False #Is the minion currently under a buff (or debuff)?
		self.turns = 0 #Increase this every turn, as a turn counter, useful for buffing and stuff per/turn
		self.buffTurns = 0 #How long the buff (or debuff) lasts
		self.activeBuffs = [] #In case we get more than one...
		self.isDead = False
		
		
		
#DRAWING-----------------------------------------
		
	def draw(self):
		self.updateRect()
		Display.CANVAS.blit(self.sprite, self.rect)
		self.turns += 1
	
	def updateRect(self):
		self.rect = pygame.Rect(self.screenX*Display.TILE_SIZE, self.screenY*Display.TILE_SIZE, self.size, self.size)
	
	

	
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
		
		
		
	#MOVEMENT-----------------------------------------
	def hasMoved(self):
		return self.didMove
	
	def moved(self, bool):
		self.didMove = bool
		
	def getSpeed(self):
		return self.speed
				
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
		
	#BUFFS/COMBAT------------------------------
	"""This applies a temporary change to a minions stats, (type) that lasts (numOfTurns) turns.
	It is used to debuff too, to avoid replicating all the code and changing to negative signs, so be
	sure to always hand it the number (pos or neg)you mean to. In other words, WATCH YOUR SIGNS +- """
	def buff(self, type, num, numOfTurns):
		print "ALRIGHT!! Buff time!"
		self.buffsActive = True
		self.buffTurns = numOfTurns
		if type == "speed":
			self.activeBuffs.append(type)
			self.speed += num
		if type == "attack":
			self.activeBuffs.append(type)
			self.attack += num
		if type == "defense":
			self.activeBuffs.append(type)
			self.defense += num
		if type == "initative":
			self.activeBuffs.append(type)
			self.initiative += num
				
	#SAME CODE AS BUFF, just for negative numbers
	def debuff(self, type, num, numOfTurns):
		print "OH NO! Acquired a debuff :("
		self.buffsActive = True
		self.buffTurns = numOfTurns
		if type == "speed":
			self.activeBuffs.append(type)
			self.speed += num
			if self.speed < 0:
				self.speed = 0
		if type == "attack":
			self.activeBuffs.append(type)
			self.attack += num
			if self.attack < 0:
				self.attack = 0
		if type == "defense":
			self.activeBuffs.append(type)
			self.defense += num
			if self.defense < 0:
				self.defense = 0
		if type == "initiative":
			self.activeBuffs.append(type)
			self.initiative += num
			if self.initiative < 0:
				self.initiative = 0
				
	#LOGIC ------------------------------------
	
	def update(self):
		pass #The player updates his heros. (though, not for the computer)
				
	def death(self):
		print "A hero has been slain..."
		self.isDead = True