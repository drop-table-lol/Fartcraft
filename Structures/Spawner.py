"""Spawner class"""
import pygame
import Sprites
from Displays import Display
from Minions import Minion

BASE_HEALTH = 5

class Spawner:
	
	def __init__(self, x, y, team, gridObj):
		self.handle = "spawner"
		self.team = team
		self.x = x
		self.y = y
		self.screenX = x
		self.screenY = y
		self.size = Display.TILE_SIZE
		self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
		self.sprite = Sprites.spr_crabSpawner
		self.gridObj = gridObj #Needed to know where to spawn our minions
		self.turns = 0
		
		self.health = BASE_HEALTH
		self.speed = 0
		self.initiative = 0
		self.defense = 2
		self.attacks = 0
		self.damage = 0
		self.isDead = False
		
		
		
	#DRAWING-----------------------------------------
	def draw(self):
		self.updateRect()
		Display.CANVAS.blit(self.sprite, self.rect)

		
	def updateRect(self):
		self.rect = pygame.Rect(self.screenX*Display.TILE_SIZE, self.screenY*Display.TILE_SIZE, self.size, self.size)

	def update(self):
		pass
		
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
		print "SHITE, spawner down!"
		self.isDead = True
		
	def buff(self, x,y,z):
		pass #TODO, CAN WE BUFF Structures?
		
	def debuff(self,x,y,z):
		pass
		
		
		
		
	#SPAWNING--------------------------------------------
	def spawnMinion(self):
		if self.team is 0: #Red Demon
			print "team 1 spawns at %s, %s" % (self.x+1, self.y)
			M = Minion.Minion(self.x+1, self.y, self.x-self.gridObj.scrollX+1, self.y+self.gridObj.scrollY, self.team)
			self.gridObj.receiveObject(M)
		elif self.team is 1: #Blue Demon
			print "team 2 spawsn at %s, %s" % (self.x-1, self.y)
			M = Minion.Minion(self.x-1, self.y, self.x-self.gridObj.scrollX-1, self.y+self.gridObj.scrollY, self.team)
			self.gridObj.receiveObject(M)
		
		if self.team is 2: #Crab
			print "team 3 spawns at %s, %s" % (self.x+1, self.y)
			M = Minion.Minion(self.x+1, self.y, self.x-self.gridObj.scrollX+1, self.y+self.gridObj.scrollY, self.team)
			self.gridObj.receiveObject(M)
			
		if self.team is 3: #Slug
			print "team 4 spawns at %s, %s" % (self.x-1, self.y)
			M = Minion.Minion(self.x-1, self.y, self.x-self.gridObj.scrollX-1, self.y+self.gridObj.scrollY, self.team)
			self.gridObj.receiveObject(M)
			
			
		