"""Pathing.py

Because the grid and tile classes are getting bloated with code concerning units
ability to walk in directions, check directions, etc, we need a helper file that
deals with pathing, such as finding an object (hero, tower, base), 
takes sight of a unit into account, and then codes more complicated movement
than basic left, right, up and down. Perhaps even allowing different behaviors, 
such as defensive, (search for terrain or walls/towers then hold position) and
agressive, (move toward the nearest sighted enemy. If no enemy is in sight, move 
toward the opposite base.)
The idea being that this extra file (perhaps entire module) allows for more complicated 
coding than bloating the tile/grid file"""


"""ideas for functions"""
#Calculate sight: 
	#Tell which tiles are adjacent, in x+sight, x-sight, etc and update those tiles.
	#When do we do this? How do we tell tiles they no longer are in sight?
	
#Aggressive pathing:
	#Check for enemies
	#If yes
		#calculate shortest path to them 
	#elif
		#move forward
	#else
		#calculate shortest path forward
	
#Defensive pathing:
	#Check for defences (walls, towers, barricades, etc (wall vs barricade?))
	#If yes
		#Calculate path towards that
	#elif
		#snake? Find other troops to reinforce?
	#elif
		#move forward
	#else
		#Calculate how to move forward to empty spot in sight
		
