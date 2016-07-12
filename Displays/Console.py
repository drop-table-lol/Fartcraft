"""Console.py
A redirect for game output. It'll allow the player to make decisions, based on text output
and descriptions, Simple, if nothing is selected, we can leave it blank, but if we select something, or 
when combat happens, it can tell us the state of the game/combat/etc."""
import pygame
import Display
import Sprites

class Console:
	def __init__(self):
		self.sprite = Sprites.spr_console
		self.x = 0
		self.y = 768
		self.xsize = 200
		self.ysize = 768
		self.commandSizeX = 100
		self.commandSizeY = 192
		self.rect = pygame.Rect(self.x, self.y, self.xsize, self.commandSizeY)
		self.buildRect = pygame.Rect(0, 768, self.commandSizeX, self.commandSizeY)			#Hardcoded
		self.attackRect = pygame.Rect(192, 768, self.commandSizeX, self.commandSizeY) 		#Because
		self.spawnRect = pygame.Rect(384, 768, self.commandSizeX, self.commandSizeY)		#Don't 
		self.passRect = pygame.Rect(572, 768, self.commandSizeX, self.commandSizeY)			#Change
		self.commands = ["build", "attack", "spawn minion", "pass"]
		self.commandSprites = Sprites.sprCommands
		self.commandRects = []
		self.commandRects.append(self.buildRect)
		self.commandRects.append(self.attackRect)
		self.commandRects.append(self.spawnRect)
		self.commandRects.append(self.passRect)

	def draw(self):
		Display.CANVAS.blit(self.sprite, self.rect)
		for x in xrange (len(self.commandSprites)):
			Display.CANVAS.blit(self.commandSprites[x], self.commandRects[x])