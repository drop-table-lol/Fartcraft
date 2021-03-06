"""Wall.py

	TODO:Update so that walls are attackable. Right now they are impossible to destory
	for pathing purposes. This is done in the Grid.py file in the Grids folder. 
	look for moveObject() function in the Tile class, and remove 
	{...and owner.grid[xvalue][yvalue].object.handle is "wall"} 
	for each direction when done testing.

	Otherwise, this wall will function as a structure, based on team play. It can be 
	attacked, upgraded (it is a tower with zero attack) and will be used to move minions,
	defend towers, etc. It will be built by the hero in T turns, based on the type of tower."""
	
	
"""Spawner class"""
import pygame
import Sprites
from Displays import Display

BASE_HEALTH = 8
BASE_SPEED = 0 #Tiles per turn
BASE_ATTACKS = 0 #Number of attacks per turn
BASE_DAMAGE = 0 #number of d6 dice rolled per attack
BASE_DEFENSE = 1 #number of BASE_ARMOR dice rolled per defense
BASE_ARMOR = 3 #m sided dice is rolled for defense
BASE_INITIATIVE = 0 #Determines who gets to go first
"""TODO: Add a txt file or xml or whatever formatted file to have base stats for structures
another one for minions, maybe one for heros, etc. This way, all of the BASE_CONSTS can be in one place"""

class Wall:
	
	def __init__(self, x, y, scrollX, scrollY, team):
		self.handle = "wall"
		self.team = team
		self.x = x
		self.y = y
		self.screenX = scrollX
		self.screenY = scrollY
		self.size = Display.TILE_SIZE
		self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
		self.sprite = Sprites.spr_wall
		
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
		print "oh no! wall down!"
		self.isDead = True
		
		
	def buff(self,x,y,z):
		pass #TODO, CAN WE BUFF Structures?
		
	def debuff(self,x,y,z):
		pass
		