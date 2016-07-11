""" Main game logic. Where the magic happens. """

import pygame
from Displays import Display
from Displays import Console
from Grids import Grid
from Input import Input
from Player import Player
from Minions import Minion
from Minions import Hero
from Structures import Spawner
from Structures import Wall
from Structures import Tower
from Animations import Animation
import Sprites #For sweet ass cursor

from pygame.locals import *
import sys

class Game:
	def __init__(self):
		pygame.init()
		
	def run(self):
		# Run the game
		gameNotOver = True
		while gameNotOver:
			gameNotOver = self.runGame()

	def runGame(self):
		#Pre-initializations
		ConsoleObj = Console.Console() #For player input and commands not radial menu for now... ): 
		gridObj = Grid.Grid()
		screenObj = Display.Screen(gridObj)
		Jdogg = Hero.Hero(1, 1, 1, 1, 0)
		inputObj = Input.Input(screenObj, gridObj, Jdogg)
		pygame.mouse.set_visible(False)#Cause we want our own dank image...
		
		
		#Actually Setting up the game
		#DopeAssTower = Tower.Tower(0, 0, 0)
		
		#SPW = Spawner.Spawner(0, 0, 0, gridObj)
		SlugSPW = Spawner.Spawner(20, 0, 3, gridObj)
		CrabSpawner = Spawner.Spawner(0, 0, 2, gridObj)
		#gridObj.receiveObject(SPW)
		gridObj.receiveObject(SlugSPW)
		gridObj.receiveObject(Jdogg)
		gridObj.receiveObject(CrabSpawner)
		
		#gridObj.receiveObject(DopeAssTower)
	
		# list of objects
		allObjects = ["minion", "hero","spawner", "tower", "wall"]
		
		#Game Loop follows
		screenObj.update()
		ConsoleObj.draw()
		done = False
		turns = 1
		sac = Sprites.spr_cursor
		ticker = 0
		while not done:
		
			
			
			if ticker % 60 is 0:  # all things update. all things move
				done = inputObj.update()
				screenObj.update()
				pygame.display.update()
				ConsoleObj.draw()
				gridObj.updateObjects()
				done = inputObj.update()
				gridObj.resetObjects()
				turns += 1
				gridObj.corpseCleanup()
				Jdogg.draw()
			elif ticker % 30 is 0 : # all things update. all things move except minions
				done = inputObj.update()
				screenObj.update()
				pygame.display.update()
				ConsoleObj.draw()
				gridObj.updateObjects("minion")
				done = inputObj.update()
				gridObj.resetObjects()
				turns += 1
				gridObj.corpseCleanup()
				Jdogg.draw()
			else:					# only graphics update
				screenObj.update()
				ConsoleObj.draw()
				pygame.display.update()
				done = inputObj.update()
				Jdogg.draw()
									#If either of the spawners is dead, the game is over
			if SlugSPW.isDead or CrabSpawner.isDead:
				done = True
				
			#Cursor shit
			cursor = pygame.mouse.get_pos()
			sweetAssCursor = pygame.Rect(cursor[0], cursor[1], Display.TILE_SIZE, Display.TILE_SIZE)
			Display.CANVAS.blit(sac, sweetAssCursor)
			
			#Screen shit
			pygame.display.update()
			Display.FPSCLOCK.tick(Display.FPS)
			ticker += 1
	

 
if __name__ == '__main__':
	""" For non-networked gameplay """
	game = Game()
	game.run()
