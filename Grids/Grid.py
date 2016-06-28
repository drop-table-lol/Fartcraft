import pygame
from Displays import Display
import random
import Sprites


class Grid:
	def __init__(self):
		self.lengthTiles = 21 
		self.widthTiles = 21
		self.grid = []
		self.initialize()
		

	
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
		
	def updateObjects(self):
		for i in xrange(0, self.lengthTiles): #Need to use length and width tiles, because we're updating EVERYTHING, not just what's seen
			for j in xrange(0, self.widthTiles):
				if self.grid[i][j].object is not "empty": #Check each tile for an object
					if self.grid[i][j].objectCanMove(): #See if it is can move
						print "Moving from %s, %s" % (i, j)
						self.grid[i][j].moveObject(self) #Then move it
						
						#######TODO #####
						"""ADD Combat checks, as well as checks for vision and maybe towers/structures that don't move"""

						
	"""Here we reset all moved objects to a non-moved state, so that they may move again next turn.
	This could easily be adapted with a counter in the Minion class to have effects which last longer than 
	one turn, and can even be per-object, allowing some to move once every two turns or the like"""
	def resetObjects(self):
		for i in xrange(0, self.lengthTiles): #Need to use length and width tiles, because we're updating EVERYTHING, not just what's seen
			for j in xrange(0, self.widthTiles):
				if self.grid[i][j].object is not "empty": #Check each tile for an object	
					self.grid[i][j].object.moved(False)	
					
					
					
	def scroll(self, direction):
		for i in xrange(0, self.lengthTiles): #Need to use length and width tiles, because we're updating EVERYTHING, not just what's seen
			for j in xrange(0, self.widthTiles):
				if self.grid[i][j].object is not "empty": #Check each tile for an object	
					self.grid[i][j].object.scroll(direction)		
					
					
					
					
class Tile:
	def __init__(self, sprite, x, y, collision):
	
		self.sprite = sprite
		self.x = x
		self.y = y
		self.collision = collision
		self.rect = pygame.Rect(self.x*Display.TILE_SIZE, self.y*Display.TILE_SIZE, Display.TILE_SIZE, Display.TILE_SIZE)
		self.text = pygame.font.SysFont("monospace", 12).render("(" + str(x) + "," + str(y) + ")", 1, (0,0,0))
		self.object = "empty" #This will contain the unit, structure, or whatever that goes on this tile.
		#self.objects is a list, so that we don't have to have hasObject() as a function, instead we can say, if "tile.objects[]:"
	
	def draw(self, displayX, displayY):
		drawRect = pygame.Rect(displayX*Display.TILE_SIZE, displayY*Display.TILE_SIZE, Display.TILE_SIZE, Display.TILE_SIZE)
		Display.CANVAS.blit(self.sprite, drawRect)
		Display.CANVAS.blit(self.text, (displayX*Display.TILE_SIZE, displayY*Display.TILE_SIZE))
		if self.object is not "empty":
			self.object.draw()
		
	
	"""This eliminates reaching into other's lists, (interface),
	as well as an ability for the map or others to spawn stuff"""
	def recieveObject(self, Obj): 
		self.object = Obj
	
	def objectCanMove(self):
		if self.object.getSpeed() > 0:
			return True #And then call moveObject()
		
	def moveObject(self, owner): #In this case, the owner is the grid
		speed = self.object.getSpeed() #To see how many tiles we need to check
		direction = self.object.direction #To see in what direction
		moved = self.object.hasMoved() #To ensure we move at least once. (But not more)
		
		#Movement Logic:
		
		#RIGHT
		if direction == "RIGHT" and self.object.hasMoved() is False: #Check x+1 through x+speed    TODO ----
			if self.x+speed < owner.widthTiles: 
				if owner.tileIsWalkable(self.x+speed, self.y):
					self.object.moved(True)
					self.object.moveRight()
					owner.grid[self.x+speed][self.y].recieveObject(self.object) #Send the object on it's way
					self.object = "empty" # Remove the object that is no longer occupying the space
					print "right"
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
					owner.grid[self.x-speed][self.y].recieveObject(self.object) #Send the object on it's way
					self.object = "empty" # Remove the object that is no longer occupying the space
					print "left"

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
					owner.grid[self.x][self.y+speed].recieveObject(self.object) #Send the object on it's way
					self.object = "empty" # Remove the object that is no longer occupying the space
					print "down"
					
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
					owner.grid[self.x][self.y-speed].recieveObject(self.object) #Send the object on it's way
					self.object = "empty" # Remove the object that is no longer occupying the space
					print "up"
					
				else: #Up didn't work due to collision (OR EDGE OF MAP)
					self.object.getRandomDirection() #Collision
			else:
				self.object.getRandomDirection()#Edge of world
					
				