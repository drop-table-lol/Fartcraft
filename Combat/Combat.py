"""Combat.py - What it sounds like, eh?
	Should have methods that take any two units/objects, (what about powers and whatnot?)
	do some math, calculate a winner, based on attack, health, etc. and 
	have some sort of outcome (WOW, such specification... so, they may not die in one round of combat?"""
	
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

BUFF_TURNS = 2
DEBUFF_TURNS = 2
	
	
"""Melee combat for units right next to each other. Need to develop a way to have combat between mixed types,
as well as two ranged units, though, two ranged units could use the same initiative.
ALSO, do buildings have initative? Do they autocast? Do they cost AP?"""
def meleeCombat(attacker, defender, owner):
	print "CHHARRRGE!!!!"
	if attacker.initiative+1 > defender.initiative: #Attacker gets an initiative bonus for forcing combat
		defender.health -= attacker.damage
		if not isDead(defender):
			attacker.health -= defender.damage
			if isDead(attacker):
				owner.attacker.death()
		else:
			defender.death()
			attacker.debuff("initative", INITATIVE_DEBUFF, DEBUFF_TURNS)

	elif defender.initiative >= attacker.initiative: #BUT, the defender wins ties...
		attacker.health -= defender.damage
		if not isDead(attacker):
			defender.health -= attacker.damage
			if isDead(defender):
				defender.death()
		else:
			attacker.death()
			defender.debuff("initative", INITATIVE_DEBUFF, DEBUFF_TURNS)
		
		
def isDead(unit):
	if unit.health <= 0:
		return True
	else:
		return False
		

	