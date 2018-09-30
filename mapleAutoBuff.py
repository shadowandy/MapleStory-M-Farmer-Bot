from keypress import keyPress
import random
import threading
import time
import sys
import datetime

# Buttons binded for character buff spells
buffNow = 1
buffWaitMin = 720
buffWaitMax = 750
buffButton = ['a','s','d','f']
buffSlpMin = 0.3
buffSlpMax = 0.6
# For switching to buff
buffButtonSwitch = 'z'
buffSwitch = 0


# Buttons binded for character summon spells
summonNow = 1
summonWaitMin = 220
summonWaitMax = 250
summonButton = ['c']

# Buttons binded for fever buff
feverNow = 1
feverWaitMin = 240
feverWaitMax = 300
feverButton = ['c']

def questBot():
	global buffNow, summonNow, feverNow
	
	if buffNow:
		castBuff()
		buffNow = not buffNow
	if summonNow:
		castSummon()
		summonNow = not summonNow
	if feverNow:
		castFever()
		feverNow = not feverNow

def castBuff():
	if buffSwitch:
		keyPress(buffButtonSwitch, random.uniform(0.1,0.3))
	rand = random.choice(random.sample(range(buffWaitMin,buffWaitMax),5))
	threading.Timer(rand, buffToggle).start()
	print ("'" + str(rand) + "'" + " seconds until next castBuff()")
	for keyValue in buffButton:
		keyPress(keyValue, random.uniform(0.1,0.3))
		time.sleep(random.uniform(buffSlpMin,buffSlpMax))
	if buffSwitch:
		keyPress(buffButtonSwitch, random.uniform(0.1,0.3))

def buffToggle():
	global buffNow
	buffNow = 1

def castSummon():
	rand = random.choice(random.sample(range(summonWaitMin,summonWaitMax),5))
	threading.Timer(rand, summonToggle).start()
	print ("'" + str(rand) + "'" + " seconds until next castSummon()")
	for keyValue in summonButton:
		keyPress(keyValue, random.uniform(0.1,0.3))
		time.sleep(random.uniform(buffSlpMin,buffSlpMax))

def summonToggle():
	global summonNow
	summonNow = 1

def castFever():
	rand = random.choice(random.sample(range(feverWaitMin,feverWaitMax),5))
	threading.Timer(rand, feverToggle).start()
	print ("'" + str(rand) + "'" + " seconds until next castFever()")
	for keyValue in feverButton:
		keyPress(keyValue, random.uniform(0.1,0.3))
		time.sleep(random.uniform(buffSlpMin,buffSlpMax))

def feverToggle():
	global feverNow
	feverNow = 1