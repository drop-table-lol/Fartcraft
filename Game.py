""" Main game logic. Where the magic happens. """

import pygame
from Displays import Display
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
	
		
		#Game Loop follows
		screenObj.update()
		pygame.display.update()
		done = False
		turns = 1
		sac = Sprites.spr_cursor
		while not done:
		
			done = inputObj.update()
			screenObj.update()
			gridObj.updateObjects()
			done = inputObj.update()
			
			gridObj.resetObjects()
			turns += 1
			gridObj.corpseCleanup()
			Jdogg.draw()
			

			
			
			#Cursor shit
			cursor = pygame.mouse.get_pos()
			sweetAssCursor = pygame.Rect(cursor[0], cursor[1], Display.TILE_SIZE, Display.TILE_SIZE)
			Display.CANVAS.blit(sac, sweetAssCursor)
			
			#Screen shit
			pygame.display.update()
			Display.FPSCLOCK.tick(Display.FPS)
	

 
if __name__ == '__main__':
	""" For non-networked gameplay """
	game = Game()
	game.run()
