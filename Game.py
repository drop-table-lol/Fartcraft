""" Main game logic. Where the magic happens. """

import pygame
from Displays import Display
from Grids import Grid
from Input import Input
from Player import Player
from Minions import Minion
from Structures import Spawner
from Structures import Wall
from Structures import Tower
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
		Minny0 = Minion.Minion(8, 0, 1)
		Minny1 = Minion.Minion(11, 0, 1)
		Minny2 = Minion.Minion(14, 0, 1)
		Minny3 = Minion.Minion(17, 0, 1)
		Minny4 = Minion.Minion(20, 0, 1)
		DopeAssTower = Tower.Tower(1, 0, 0)
		#print "team %s" % (NotMinny.team)
		
		gridObj.grid[8][0].recieveObject(Minny0)
		gridObj.grid[11][0].recieveObject(Minny1)
		gridObj.grid[14][0].recieveObject(Minny2)
		gridObj.grid[17][0].recieveObject(Minny3)
		gridObj.grid[20][0].recieveObject(Minny4)
		gridObj.grid[1][0].recieveObject(DopeAssTower)
	#	SPW = Spawner.Spawner(19, 1, 0)
		#NotSPW = Spawner.Spawner(6, 0, 1)
	#	gridObj.grid[19][1].recieveObject(SPW)
		#gridObj.grid[6][0].recieveObject(NotSPW)
		#DopeAssWall = Wall.Wall(3, 0, 0)
		#gridObj.grid[3][0].recieveObject(DopeAssWall)"""
		
		#Game Loop follows
		screenObj.update()
		pygame.display.update()
		done = False
		turns = 1
		sac = Sprites.spr_cursor
		while not done:
		
			#input = raw_input(">>>")
			#print "Turn %s" % (turns)
			gridObj.updateObjects()
			done = inputObj.update()
			screenObj.update()
			gridObj.resetObjects()
			turns += 1
			gridObj.corpseCleanup()
			
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
