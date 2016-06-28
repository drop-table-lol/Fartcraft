""" Main game logic. Where the magic happens. """

import pygame
from Displays import Display
from Grids import Grid
from Input import Input
from Player import Player
from Minions import Minion
from Structures import Spawner
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
		inputObj = Input.Input(screenObj, gridObj)
		pygame.mouse.set_visible(False)#Cause we want our own sweet image...
		
		
		#Actually Setting up the game
		Minny = Minion.Minion(0, 0, 0)
		NotMinny = Minion.Minion(20, 20, 1)
		gridObj.grid[0][0].recieveObject(Minny)
		gridObj.grid[20][20].recieveObject(NotMinny)
		SPW = Spawner.Spawner(0, gridObj.widthTiles/2, 0)
		NotSPW = Spawner.Spawner(gridObj.lengthTiles-1, gridObj.widthTiles/2, 1)
		gridObj.grid[0][gridObj.widthTiles/2].recieveObject(SPW)
		gridObj.grid[gridObj.lengthTiles-1][gridObj.widthTiles/2].recieveObject(NotSPW)
		
		#Game Loop follows
		screenObj.update()
		pygame.display.update()
		done = False
		turns = 1
		sac = Sprites.spr_cursor
		while not done:
		
			print "Turn %s" % (turns)
			gridObj.resetObjects()
			gridObj.updateObjects()
			done = inputObj.update()
			screenObj.update()
			turns += 1
			
			#Cursor shit
			cursor = pygame.mouse.get_pos()
			sweetAssCursor = pygame.Rect(cursor[0], cursor[1], Display.TILE_SIZE, Display.TILE_SIZE)
			Display.CANVAS.blit(sac, sweetAssCursor)
			
			pygame.display.update()
			Display.FPSCLOCK.tick(Display.FPS)
	

 
if __name__ == '__main__':
	""" For non-networked gameplay """
	game = Game()
	game.run()
