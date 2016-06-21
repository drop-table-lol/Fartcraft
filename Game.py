""" Main game logic. Where the magic happens. """

import pygame
import Display
import Grid
import Input
import Player

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
		inputObj = Input.Input()
		
		screenObj = Display.Screen(gridObj)
		playerObj = Player.Player(screenObj, gridObj)
		endGame = False
		while not endGame:
			endGame = inputObj.update(playerObj)
			screenObj.update()
			
			gridObj.update()
			playerObj.update()
			
			pygame.display.update()
			Display.FPSCLOCK.tick(Display.FPS)
			
 
if __name__ == '__main__':
	""" For non-networked gameplay """
	game = Game()
	game.run()
