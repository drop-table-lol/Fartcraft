""" Main game logic. Where the magic happens. """

import pygame
from Displays import Display
from Grids import Grid
from Input import Input
from Player import Player
from Minions import Minion
from Structures import Spawner

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
		
		#Actually Setting up the game
		Minny = Minion.Minion(1, 1)
		gridObj.grid[1][1].recieveObject(Minny)
		
		#Game Loop follows
		for x in xrange(0, 20):
			print "Turn %s" % (x)
			screenObj.update()
			gridObj.updateObjects()
			gridObj.resetObjects()
			input = raw_input(">")
			
			
			
			
			pygame.display.update()
			Display.FPSCLOCK.tick(Display.FPS)
	

 
if __name__ == '__main__':
	""" For non-networked gameplay """
	game = Game()
	game.run()
