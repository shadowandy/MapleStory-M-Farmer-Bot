from keypress import keyPress
import random
import threading
import time

# Movement related vars
movementDirection = 1
movementDistMin = 0.1
movementDistMax = 0.8
movementDuration = 0.0
movementCountMin = 6
movementCountMax = 12
movementCount = random.choice(range(movementCountMin,movementCountMax,1))

# Numbers of times to triggers and buttons binded for attacks
# 0 if you wish to trigger a double move
skillRand = [0, 1, 2, 2]
skillButton = ['v']
skillSlpMin = 0.3
skillSlpMax = 0.5

# Buttons binded for character buff spells
buffWaitMin = 1500
buffWaitMax = 1645
buffButton = ['c', 'f']
buffSlpMin = 2.5
buffSlpMax = 3.6
# For switching to buff
buffButtonSwitch = 's'
buffSwitch = 0

# Buttons binded for summon spells
summonWaitMin = 120
summonWaitMax = 220
summonButton = ['d', 'd']
summonSlpMin = 2.5
summonSlpMax = 3.3

def castSkill():
	for x in range(random.choice(skillRand)):
		keyPress(random.choice(skillButton), random.uniform(0.1,0.3))
		time.sleep(random.uniform(skillSlpMin,skillSlpMax))

def castBuff():
	if buffSwitch:
		keyPress(buffButtonSwitch, random.uniform(0.1,0.3))
	rand = random.choice(random.sample(range(buffWaitMin,buffWaitMax),5))
	threading.Timer(rand, castBuff).start()
	print ("'" + str(rand) + "'" + " seconds until next castBuff()")
	for keyValue in buffButton:
		keyPress(keyValue, random.uniform(0.1,0.3))
		time.sleep(random.uniform(buffSlpMin,buffSlpMax))
	if buffSwitch:
		keyPress(buffButtonSwitch, random.uniform(0.1,0.3))

def castSummon():
	rand = random.choice(random.sample(range(summonWaitMin,summonWaitMax),5))
	threading.Timer(rand, castSummon).start()
	print ("'" + str(rand) + "'" + " seconds until next castSummon()")
	for keyValue in summonButton:
		keyPress(keyValue, random.uniform(0.1,0.3))
		time.sleep(random.uniform(summonSlpMin,summonSlpMax))

def charMove():
	global movementDirection, movementDuration, movementCount
	duration = random.uniform(movementDistMin,movementDistMax)
	if movementDirection:
		movementDuration += duration
		keyPress('right', duration)
	else:
		movementDuration -= duration
		keyPress('left', duration)

	if movementCount <= 0:
		if movementDuration > 0:
			keyPress('left', movementDuration)
		else:
			keyPress('right', movementDuration * -1)

		print ("Zero-ing character to starting point")
		movementCount = random.choice(range(movementCountMin,movementCountMax,1))
		movementDuration = 0.0

	movementDirection = not movementDirection
	movementCount -= 1
