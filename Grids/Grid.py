import pygame
import random

from Displays import Display
from Combat import Combat
from Pathing import Pathing
import Sprites


class Grid:
	def __init__(self):
		self.lengthTiles = 21 
		self.widthTiles = 21
		self.grid = []
		self.initialize()
		self.scrollX = 0
		self.scrollY = 0
		

	
	def initialize(self):
		for x in xrange(0, self.widthTiles):
			tempList = []
			for y in xrange(0, self.lengthTiles):
				tempList.append(Tile(Sprites.GROUND_SPRITES[random.randint(0, len(Sprites.GROUND_SPRITES) - 1)], x, y, True))
				
			self.grid.append(tempList)
				
				
	def draw(self, x, y, width, height):
		for i in xrange(x, width):
			for j in xrange(y, height):
				self.grid[i][j].draw(i - x, j - y)
				
			
	
	def tileIsWalkable(self, x, y):
		if self.grid[x][y].object is not "empty":
				return False
		else:
			return True
		
	def updateObjects(self): # if dontMoveThisObject is passed, then dont allow it to move
		for i in xrange(0, self.lengthTiles): #Need to use length and width tiles, because we're updating EVERYTHING, not just what's seen
			for j in xrange(0, self.widthTiles):
				self.grid[i][j].update()
				if self.grid[i][j].object is not "empty": #Check each tile for an object
					if self.grid[i][j].objectCanMove() and self.grid[i][j].object.didMove is False: #See if it is can move and if it is their turn
						self.grid[i][j].moveObject(self) #Then move it
						"""TODO update structures seperately"""
						
	def spawnMinion(self, team):
		for i in xrange(0, self.lengthTiles):
			for j in xrange(0, self.widthTiles):
				if self.grid[i][j].object is not "empty":
					if self.grid[i][j].object.handle is "spawner":
						if self.grid[i][j].object.team == team:
							self.grid[i][j].object.update()
						
				

						
	"""Here we reset all moved objects to a non-moved state, so that they may move again next turn.
	This could easily be adapted with a counter in the Minion class to have effects which last longer than 
	one turn, and can even be per-object, allowing some to move once every two turns or the like"""
	def resetObjects(self):
		for i in xrange(0, self.lengthTiles): #Need to use length and width tiles, because we're updating EVERYTHING, not just what's seen
			for j in xrange(0, self.widthTiles):
				if self.grid[i][j].object is not "empty": #Check each tile for an object	
					self.grid[i][j].object.moved(False)	
					
	"""Rather a macabre thing, but exactly what it sounds like. Remove dead units from the field."""
	def corpseCleanup(self):
		for i in xrange(0, self.lengthTiles): #Need to use length and width tiles, because we're updating EVERYTHING, not just what's seen
			for j in xrange(0, self.widthTiles):
				if self.grid[i][j].object is not "empty": #Check each tile for an object	
					if self.grid[i][j].object.isDead is True:
						self.grid[i][j].object = "empty" #CLEAN up those nasty corpses before they get more nasty
					

				if self.grid[i][j].animation is not "empty":
					if self.grid[i][j].animation.isActive is False:
						self.grid[i][j].animation = "empty"

					
	def scroll(self, direction):
		for i in xrange(0, self.lengthTiles): #Need to use length and width tiles, because we're updating EVERYTHING, not just what's seen
			for j in xrange(0, self.widthTiles):
				if self.grid[i][j].object is not "empty": #Check each tile for an object	
					self.grid[i][j].object.scroll(direction)	
		if direction is "RIGHT":
			self.scrollX += 1
		elif direction is "LEFT":
			self.scrollX -= 1
		elif direction is "DOWN":
			self.scrollY += 1
		elif direction is "UP":
			self.scrollY -= 1
			"""TODO: add a scroll function for animations"""
					
					
					
	def receiveObject(self, obj):
		if self.grid[obj.x][obj.y].object is "empty":
			self.grid[obj.x][obj.y].receiveObject(obj)
		else:
			Combat.meleeCombat(obj, self.grid[obj.x][obj.y].object, self)
			if obj.isDead:
				pass
			else:
				self.grid[obj.x][obj.y].receiveObject(obj)
				
				
	def receiveAnim(self, anim):
		#if self.grid[anim.x][anim.y].animation is "empty":
		self.grid[anim.x][anim.y].receiveAnim(anim)
			
			
					
					
					
class Tile:
	def __init__(self, sprite, x, y, collision):
	
		self.sprite = sprite
		self.x = x
		self.y = y
		self.collision = collision
		self.rect = pygame.Rect(self.x*Display.TILE_SIZE, self.y*Display.TILE_SIZE, Display.TILE_SIZE, Display.TILE_SIZE)
		self.text = pygame.font.SysFont("monospace", 12).render("(" + str(x) + "," + str(y) + ")", 1, (0,0,0))
		self.object = "empty" #This will contain the unit, structure, or whatever that goes on this tile.
		self.animation = "empty"
		self.ticker = 0
		
	
	def draw(self, displayX, displayY):
		drawRect = pygame.Rect(displayX*Display.TILE_SIZE, displayY*Display.TILE_SIZE, Display.TILE_SIZE, Display.TILE_SIZE)
		Display.CANVAS.blit(self.sprite, drawRect)
		Display.CANVAS.blit(self.text, (displayX*Display.TILE_SIZE, displayY*Display.TILE_SIZE))
		if self.object is not "empty":
			self.object.draw()
		if self.animation is not "empty":
			self.animation.draw()
			
	def update(self):
		if self.object is "empty":
			pass
		else:
			if self.object.handle is not "spawner":
				self.object.update()
		
	
	"""This eliminates reaching into other's lists, (interface),
	as well as an ability for the map or others to spawn stuff"""
	def receiveObject(self, Obj): 
		self.object = Obj
		
	def receiveAnim(self, Anim):
		self.animation = Anim
	
	def objectCanMove(self):
		if self.object.getSpeed() > 0:
			return True #And then call moveObject()
		else:
			return False
		
	def moveObject(self, owner): #In this case, the owner is the grid
		speed = self.object.getSpeed() #To see how many tiles we need to check
		direction = self.object.direction #To see in what direction
		moved = self.object.hasMoved() #To ensure we move at least once. (But not more)
		if self.object.handle is not "hero":
			#RIGHT
			if direction == "RIGHT" and self.object.hasMoved() is False: #Check x+1 through x+speed    TODO ----
				if self.x+speed < owner.widthTiles: 
					if owner.tileIsWalkable(self.x+speed, self.y):
						self.object.moved(True)
						self.object.moveRight()
						owner.receiveObject(self.object) #Send the object on it's way
						self.object = "empty" # Remove the object that is no longer occupying the space
						
					elif not owner.tileIsWalkable(self.x+speed, self.y) and owner.grid[self.x+speed][self.y].object.team is not self.object.team:#We couldn't move there, but can we attack it?
						Combat.meleeCombat(self.object, owner.grid[self.x+speed][self.y].object, owner)
					else: #Right didn't work, due to collision or edge of map
						self.object.getRandomDirection() #Collision
				else:
					self.object.getRandomDirection()#Edge of world
			
			
			#LEFT
			elif direction == "LEFT" and self.object.hasMoved() is False:
				if self.x-speed >= 0:
					if owner.tileIsWalkable(self.x-speed, self.y):
						self.object.moved(True)
						self.object.moveLeft()#Update XorY value
						owner.receiveObject(self.object) #Send the object on it's way
						self.object = "empty" # Remove the object that is no longer occupying the space
						
					elif not owner.tileIsWalkable(self.x-speed, self.y) and owner.grid[self.x-speed][self.y].object.team is not self.object.team:#We couldn't move there, but can we attack it?
						Combat.meleeCombat(self.object, owner.grid[self.x-speed][self.y].object, owner)

					else: #Left didn't work, due to collision or edge of map 
						self.object.getRandomDirection() #Collision
				else:
					self.object.getRandomDirection() #Edge of world
					
					
			#DOWN		
			elif direction == "DOWN" and self.object.hasMoved() is False:
				if self.y + speed < owner.lengthTiles:
					if owner.tileIsWalkable(self.x, self.y+speed):
						self.object.moved(True)
						self.object.moveDown()#Update XorY value
						owner.receiveObject(self.object) #Send the object on it's way
						self.object = "empty" # Remove the object that is no longer occupying the space
						
					elif not owner.tileIsWalkable(self.x, self.y+speed) and owner.grid[self.x][self.y+speed].object.team is not self.object.team:#We couldn't move there, but can we attack it?
						Combat.meleeCombat(self.object, owner.grid[self.x][self.y+speed].object, owner)
						
					else: #Down didn't work, due to collision or edge of map 
						self.object.getRandomDirection() #Collision
				else:
					self.object.getRandomDirection() #Edge of world
						
						
			#UP			
			elif direction == "UP" and self.object.hasMoved() is False:
				if self.y-speed >= 0:
					if owner.tileIsWalkable(self.x, self.y-speed):
						self.object.moved(True)
						self.object.moveUp()#Update XorY value
						owner.receiveObject(self.object) #Send the object on it's way
						self.object = "empty" # Remove the object that is no longer occupying the space
						
					elif not owner.tileIsWalkable(self.x, self.y-speed) and owner.grid[self.x][self.y-speed].object.team is not self.object.team:#We couldn't move there, but can we attack it?
						Combat.meleeCombat(self.object, owner.grid[self.x][self.y-speed].object, owner)
						
					else: #Up didn't work due to collision (OR EDGE OF MAP)
						self.object.getRandomDirection() #Collision
				else:
					self.object.getRandomDirection()#Edge of world	
		
		else:
			pass
			