""" Main game logic. Where the magic happens. """

import pygame
from Displays import Display
from Grids import Grid
from Input import Input
from Player import Player
from Minions import Minion
from Structures import Spawner

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
		playerHandlerObj = Player.PlayerHandler(gridObj, screenObj)
		minionHandlerObj = Minion.MinionHandler(gridObj, screenObj, 1)
		playerSpawner = Spawner.Spawner(0, 0, (gridObj.lengthTiles/2), 0, (gridObj.lengthTiles/2), gridObj, screenObj)
		inputObj = Input.Input(playerHandlerObj, minionHandlerObj, screenObj)
		
		#Game Loop follows
		endGame = False
		while not endGame:
			endGame = inputObj.update()
			screenObj.update()
			
			gridObj.update()
			playerHandlerObj.update()
			minionHandlerObj.update()
			playerSpawner.update()
			pygame.display.update()
			Display.FPSCLOCK.tick(Display.FPS)
	

 
if __name__ == '__main__':
	""" For non-networked gameplay """
	game = Game()
	game.run()
