import pygame
from Displays import Display
"""ClickPlacement.py?

yeah, so lame title aside, this class is responsible for capturing a click of the mouse,
and translating that not into an x,y position, but a position on the grid that is the x,y
position of a tile, and then building a structure on that tile. 
Eventually the click, or shift-click, or right-click or whatever input we decide,
should bring up a radial menu that allows the player some options as to 
what they want to build.
"""

def calculateTile(xScroll, yScroll):
	position = pygame.mouse.get_pos()
	trueX = position[0] / Display.TILE_SIZE# + xScroll
	trueY = position[1] / Display.TILE_SIZE# + yScroll
	scrollX = position[0] / Display.TILE_SIZE + xScroll
	scrollY = position[1] / Display.TILE_SIZE + yScroll

	return (trueX, trueY, scrollX, scrollY)
	