import pygame
from Displays import Display
import random
import Sprites

BASE_HEALTH = 1
BASE_SPEED = 1
BASE_ATTACKS = 1
BASE_DAMAGE = 1
BASE_DEFENSE = 1
BASE_INITIATIVE = 1
class Minion:
	
	def __init__(self, x, y, scrollX, scrollY, team):
		#DRAWING-----------------------------------------
		self.handle = "minion"
		self.x = x
		self.y = y
		self.screenX = scrollX
		self.screenY = scrollY
		self.size = Display.TILE_SIZE
		self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
		self.team = team
		if self.team is 0:
			self.sprite = Sprites.spr_minion
		if self.team is 1:
			self.sprite = Sprites.spr_minion1
		if self.team is 2:
			self.sprite = Sprites.spr_crab
		if self.team is 3:
			self.sprite = Sprites.spr_slug
		self.timer = 0
		
		#MOVEMENT-----------------------------------------
		if self.team is 0:
			self.direction = "RIGHT"
		elif self.team is 1:
			self.direction = "LEFT"
		elif self.team is 2:
			self.direction = "RIGHT"
		elif self.team is 3:
			self.direction = "LEFT"
		
		self.didMove = False
		
		#COMBAT------------------------------
		self.health = 1
		self.speed = 1
		self.attacks = 1
		self.damage = 1
		self.defense = 1
		self.initiative = 1
		self.buffsActive = False #Is the minion currently under a buff (or debuff)?
		self.turns = 0 #Increase this every turn, as a turn counter, useful for buffing and stuff per/turn
		self.activeBuffs = [] #In case we get more than one...
		self.buffTurns = [] #This correspondes to each buffs number of turns. Iterate down the list each update
		self.buffedAmmt = [] #This is the ammount each buff or debuff contained. Apply the opposite when buffTurns is 0
		self.isDead = False
	#DRAWING-----------------------------------------
		
	def draw(self):
		self.updateRect()
		Display.CANVAS.blit(self.sprite, self.rect)
	
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
	def getSpeed(self):
		return self.speed
				
	def hasMoved(self):
		return self.didMove
		
	def moved(self, bool):
		self.didMove = bool
		
		
	def getRandomDirection(self):
		oldDir = self.direction
		while oldDir == self.direction:
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
		
	#BUFFS/COMBAT------------------------------
	"""This applies a temporary change to a minions stats, (type) that lasts (numOfTurns) turns.
	It is used to debuff too, to avoid replicating all the code and changing to negative signs, so be
	sure to always hand it the number (pos or neg)you mean to. In other words, WATCH YOUR SIGNS +- """
	def buff(self, type, num, numOfTurns):
		print "ALRIGHT!! Buff time!"
		self.buffsActive = True
		if type == "speed":
			self.activeBuffs.append(type)
			self.speed += num
			self.buffTurns.append(numOfTurns) 
			self.buffedAmmt.append(num)
		if type == "attack":
			self.activeBuffs.append(type)
			self.attack += num
			self.buffTurns.append(numOfTurns) 
			self.buffedAmmt.append(num)
		if type == "defense":
			self.activeBuffs.append(type)
			self.defense += num
			self.buffTurns.append(numOfTurns) 
			self.buffedAmmt.append(num)
		if type == "initative":
			self.activeBuffs.append(type)
			self.initiative += num
			self.buffTurns.append(numOfTurns) 
			self.buffedAmmt.append(num)
				
	#SAME CODE AS BUFF, just for negative numbers
	def debuff(self, type, num, numOfTurns):
		print "OH NO! Acquired a debuff :("
		self.buffsActive = True
		if type == "speed":
			self.activeBuffs.append(type)
			self.speed += num
			self.buffTurns.append(numOfTurns) 
			self.buffedAmmt.append(num)
			if self.speed < 0:
				self.speed = 0
		if type == "attack":
			self.activeBuffs.append(type)
			self.attack += num
			self.buffTurns.append(numOfTurns) 
			self.buffedAmmt.append(num)
			if self.attack < 0:
				self.attack = 0
		if type == "defense":
			self.activeBuffs.append(type)
			self.defense += num
			self.buffTurns.append(numOfTurns) 
			self.buffedAmmt.append(num)
			if self.defense < 0:
				self.defense = 0
		if type == "initiative":
			self.activeBuffs.append(type)
			self.initiative += num
			self.buffTurns.append(numOfTurns) 
			self.buffedAmmt.append(num)
			if self.initiative < 0:
				self.initiative = 0
				
				
	def setToBaseStat(self, stat):
		if stat is "speed":
			self.speed = BASE_SPEED
		elif stat is "health":
			self.health = BASE_HEALTH
		elif stat is "attacks":
			self.attacks = BASE_ATTACKS
		elif stat is "damage":
			self.damage = BASE_DAMAGE
		elif stat is "defense":
			self.defense = BASE_DEFENSE
		elif stat is "initiative":
			self.initiative = BASE_INITIATIVE
					
				
	#LOGIC ------------------------------------------
	def update(self): #TODO continue work on buffs logic
		self.turns += 1
		if self.buffsActive:
			tmps = [] #For collecting all the numbers we need to remove (so we don't change the list as we iterate)
			for x in xrange(len(self.buffTurns)):
				stat = self.activeBuffs[x]
				self.buffTurns[x] -= 1 #Each turn, take a turn off of buffs/debuffs
				if self.buffTurns[x] is 0: #When it hits zero, undo the buff
					if stat is "speed":
						self.speed -= self.buffedAmmt[x]
						print "set speed to %s" % (self.speed)
					elif stat is "health":
						self.health -= self.buffedAmmt[x]
						print "set health to %s" % (self.speed)
					elif stat is "attacks":
						self.attacks -= self.buffedAmmt[x]
						print "set attacks to %s" % (self.speed)
					elif stat is "damage":
						self.damage -= self.buffedAmmt[x]
						print "set damage to %s" % (self.speed)
					elif stat is "defense":
						self.defense -= self.buffedAmmt[x]
						print "set defense to %s" % (self.speed)
					elif stat is "initiative":
						self.initiative -= self.buffedAmmt[x]
						print "set initiative to %s" % (self.speed)
					tmps.append(x) #Append each position to a list of nums
			
			for j in tmps: #Use that list of nums to remove all finished buffs from list
				del self.activeBuffs[j]
				del self.buffTurns[j]
				del self.buffedAmmt[j]

						
	def death(self):
		print "I DIED"
		self.isDead = True