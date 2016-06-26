""" Main game logic. Where the magic happens. """

import pygame
from Displays import Display
from Grids import Grid
from Input import Input
from Player import Player
from Minions import Minion

class Game:
	def __init__(self):
		pygame.init()
		
	def run(self):
		# Run the game
		gameNotOver = True
		while gameNotOver:
			gameNotOver = self.runGame()

	def runGame(self):
		gridObj = Grid.Grid()
		
		
		screenObj = Display.Screen(gridObj)
		playerHandlerObj = Player.PlayerHandler(gridObj, screenObj)
		minionHandlerObj = Minion.MinionHandler(playerHandlerObj, gridObj, screenObj, 1)
		inputObj = Input.Input(playerHandlerObj, minionHandlerObj, screenObj)
		
		endGame = False
		while not endGame:
			endGame = inputObj.update()
			screenObj.update()
			
			gridObj.update()
			playerHandlerObj.update()
			minionHandlerObj.update()
			pygame.display.update()
			Display.FPSCLOCK.tick(Display.FPS)
	

 
if __name__ == '__main__':
	""" For non-networked gameplay """
	game = Game()
	game.run()
