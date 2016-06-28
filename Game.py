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
		inputObj = Input.Input(screenObj)
		
		#Actually Setting up the game
		Minny = Minion.Minion(0, 0)
		gridObj.grid[0][0].recieveObject(Minny)
		
		#Game Loop follows
		screenObj.update()
		pygame.display.update()
		done = False
		turns = 1
		counter = 0
		while not done:
		
			print "Turn %s" % (turns)
			gridObj.resetObjects()
			gridObj.updateObjects()
			done = inputObj.update()
			screenObj.update()
			input = raw_input()
			turns += 1
			
			
			
			
			pygame.display.update()
			Display.FPSCLOCK.tick(Display.FPS)
	

 
if __name__ == '__main__':
	""" For non-networked gameplay """
	game = Game()
	game.run()
