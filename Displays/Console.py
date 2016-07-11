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
		self.rect = pygame.Rect(self.x, self.y, self.xsize, self.ysize)

	def draw(self):
		Display.CANVAS.blit(self.sprite, self.rect)