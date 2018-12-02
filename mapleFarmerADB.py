from pyautogui import locateCenterOnScreen, locateOnScreen, click, mouseDown, mouseUp, keyUp
from keypressADB import keyPress, mouseClick
import random
import threading
import time

#
autoX = 1200
autoY = 1000
#autoDuration = 15
#autoMacroDur = 120
autoDuration = 15
autoMacroDur = 60
manualOn = 1
manualFirst = 1

# Movement related vars
movementDirection = 1
movementDistMin = 0.2
movementDistMax = 0.6
movementDuration = 0.0
movementCountMin = 6
movementCountMax = 9
movementCount = random.choice(range(movementCountMin,movementCountMax,1))

# Numbers of times to triggers and buttons binded for attacks
# 0 if you wish to trigger a double move

skillRand = [0, 2, 2, 2, 2, 3]
#skillRand = [0, 3, 3, 2, 3]

skillButton = ['c']
skillSlpMin = 0.3
skillSlpMax = 0.5

# Buttons binded for character buff spells

buffEnabled = 1
buffNow = 1
buffWaitMin = 20
buffWaitMax = 35
buffButton = ['d']
buffSlpMin = 0.4
buffSlpMax = 0.9
# For switching to buff
buffButtonSwitch = ''
buffSwitch = 0

# Buttons binded for summon spells
summonEnabled = 1
summonNow = 1
summonWaitMin = 120
summonWaitMax = 220
summonButton = ['s','f']
summonSlpMin = 0.4
summonSlpMax = 0.9

def toggleAuto():
	global manualOn, manualFirst
	manualOn = not manualOn
	if manualFirst:
		manualOn = not manualOn
	if manualOn:
		if not manualFirst:
			manualOn = 0
			time.sleep(random.uniform(1,1.3))
			#keyPress('p', random.uniform(0.3,0.7))
			keyPress('p', random.uniform(0.7,1.2))
			time.sleep(random.uniform(0.3,0.7))
			#keyPress('esc', random.uniform(0.3,0.7))
			manualOn = 1
			# time.sleep(random.uniform(0.1,0.3))
		else:
			manualFirst = 0
		threading.Timer(autoMacroDur, toggleAuto).start()
	else:
		manualOn = 0
		time.sleep(random.uniform(1.1,1.3))
		keyPress('p', random.uniform(0.1,0.3))
		time.sleep(random.uniform(0.9,1.3))
		mouseClick(autoX, autoY)
		manualOn = 0
		threading.Timer(autoDuration, toggleAuto).start()

def castSkill():
	if manualOn:
		if buffEnabled:
			if buffNow:
				castBuffNow()
				castBuff()
				rand = random.choice(random.sample(range(buffWaitMin,buffWaitMax),1))
				print ("'" + str(rand) + "'" + " seconds until next castBuff()")
				threading.Timer(rand, castBuffNow).start()

		if summonEnabled:
			if summonNow:
				castSummonNow()
				castSummon()
				rand = random.choice(random.sample(range(summonWaitMin,summonWaitMax),7))
				print ("'" + str(rand) + "'" + " seconds until next castSummon()")
				threading.Timer(rand, castSummonNow).start()

		for x in range(random.choice(skillRand)):
			keyPress(random.choice(skillButton), random.uniform(0.1,0.3))
			time.sleep(random.uniform(skillSlpMin,skillSlpMax))

def castBuff():
	if buffSwitch:
		keyPress(buffButtonSwitch, random.uniform(0.1,0.3))
	#rand = random.choice(random.sample(range(buffWaitMin,buffWaitMax),5))
	#threading.Timer(rand, castBuff).start()
	#print ("'" + str(rand) + "'" + " seconds until next castBuff()")
	for keyValue in buffButton:
		keyPress(keyValue, random.uniform(0.1,0.3))
		time.sleep(random.uniform(buffSlpMin,buffSlpMax))
	if buffSwitch:
		keyPress(buffButtonSwitch, random.uniform(0.1,0.3))

def castBuffNow():
	global buffNow
	buffNow = not buffNow

def castSummon():
	#rand = random.choice(random.sample(range(summonWaitMin,summonWaitMax),5))
	#threading.Timer(rand, castSummon).start()
	#print ("'" + str(rand) + "'" + " seconds until next castSummon()")
	for keyValue in summonButton:
		keyPress(keyValue, random.uniform(0.1,0.3))
		time.sleep(random.uniform(summonSlpMin,summonSlpMax))

def castSummonNow():
	global summonNow
	summonNow = not summonNow

def charMove():
	if manualOn:
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
