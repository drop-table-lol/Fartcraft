"""Combat.py - What it sounds like, eh?
	Should have methods that take any two units/objects, (what about powers and whatnot?)
	do some math, calculate a winner, based on attack, health, etc. and 
	have some sort of outcome (WOW, such specification... so, they may not die in one round of combat?"""

import pygame
import random
import Sprites
from Displays import Display
from Animations import Animation
	
	#Singleton class vs just methods?
	
#DEFAULT values for buffs/debuffs applied in combat.


INITATIVE_BUFF = 1
INITATIVE_DEBUFF = -1

ATTACK_BUFF = 1
ATTACK_DEBUFF = -1

DEFENSE_BUFF = 1
DEFENSE_DEBUFF = -1
#Maybe add a check to flee (3/4th's chance) that happens if a hero unit comes across a basic minion?
#BUT, if they pass, they get a bonus stat?
SPEED_BUFF = 1
SPEED_DEBUFF = -1

BUFF_TURNS = 3
DEBUFF_TURNS = 3
	
	
"""Melee combat for units right next to each other. Need to develop a way to have combat between mixed types,
as well as two ranged units, though, two ranged units could use the same initiative.
ALSO, do buildings have initative? Do they autocast? Do they cost AP?"""
def meleeCombat(attacker, defender, owner):
	if not attacker.isDead:
		print "MORTAL KOMBAT!!!!"
		if attacker.initiative > 0: #Must not be recovering from debuff
			if attacker.initiative+1 > defender.initiative: #Attacker gets an initiative bonus for forcing combat
				first = attacker
				second = defender
		elif defender.initiative >= attacker.initiative+1:
			first = defender
			second = attacker
			
		animType = getAnim(first)		
		damage = nDm(first.attacks, first.damage) - nDm(second.defense, second.armor)
		if damage < 1:
			damage = 1
		print "%s of clan %s did %s damage to %s of clan %s!" % (first.handle, first.team, damage, second.handle, second.team)
		second.health -= damage
		Animation.Animation(second.x,second.y, animType, owner)
		if isDead(second): #sad day, he died
			second.death()
			first.debuff("initiative", INITATIVE_DEBUFF, DEBUFF_TURNS)
			animType = getCorpse(second)
			Animation.Animation(second.x, second.y, animType, owner)
			
			
		elif not isDead(second): #Do combat for number dos
			animType = getAnim(second)		
		damage = nDm(second.attacks, second.damage) - nDm(first.defense, first.armor)
		if damage < 1 and second.handle is not "wall":
			damage = 1
		elif damage < 1 and second.handle is "wall":
			damage = 0
		print "%s of clan %s did %s damage to %s of clan %s!" % (second.handle, second.team, damage, first.handle, first.team)
		first.health -= damage
		if animType is not "empty":
			Animation.Animation(first.x,first.y, animType, owner)
		if isDead(first): #sad day, he died
			first.death()
			second.debuff("initiative", INITATIVE_DEBUFF, DEBUFF_TURNS)
			animType = getCorpse(first)
			Animation.Animation(first.x, first.y, animType, owner)
			
			
				
				
def isDead(unit):
	if unit.health <= 0:
		return True
	else:
		return False
		

"""Allows us to roll n m sided dice. For things like attack, defense, etc. This way, different minions or heros 
	can have different stats, and we can hand this function those stats and not worry about it."""
def nDm(n, m = 6): 
	sum = 0
	for x in range (0, n):
		sum += random.randint(0, m)
	return sum
	
	
"""Allows us to take in an attacker, we read their handle, then determine the correct type of animation to display"""
def getAnim(attacker): 
	if attacker.handle is "minion":
		return "slash"
	elif attacker.handle is "tower":
		return "arrows"
	elif attacker.handle is "spawner":
		return "arrows"
	elif attacker.handle is "wall":
		return "empty"
	else:
		return "slash"
		
"""Just like getAnim, but for whoever died."""
def getCorpse(deadGuy): 
	if deadGuy.handle is "minion":
		return "corpse"
	if deadGuy.handle is "tower" or "wall":
		return "rubble"