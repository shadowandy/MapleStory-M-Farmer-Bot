from pyautogui import locateCenterOnScreen, locateOnScreen, click, mouseDown, mouseUp
from keypress import keyPress
import random
import threading
import time
import sys
import datetime

screenDimension = [2560, 1440]
screenScalingFactor = 1
#screenDimension = [2880, 1800]
#screenScalingFactor = 2

questStart = [480, 540]
#questStart = [430, 655]
#questStart = [228, 380]
imagesToggle = 'questClaim.png'

started = 0
images = ['questScroll.png', 'questClaim.png', 'questComplete.png', 'questSkip.png', 'questAccept.png', 'questAvailable.png', 'questMultiComplete.png', 'questConfirm.png']
searchX = dict(shadow='andy')
searchY = dict(shadow='andy')
searchM = [240, 240]

# Buttons binded for character buff spells
buffNow = 1
buffWaitMin = 220
buffWaitMax = 300
buffButton = ['a', 'a', 's', 'd', 'f']
buffSlpMin = 2.5
buffSlpMax = 3.6
# For switching to buff
buffButtonSwitch = 'z'
buffSwitch = 0


# Buttons binded for character summon spells
summonNow = 1
summonWaitMin = 260
summonWaitMax = 290
summonButton = ['y']

def questBot():
	global started, searchX, searchY, buffNow, summonNow
	if started:
		coord = [0,0]
		for x in range(1,len(images)):
			found = 0
			try:
				if images[x] in searchX:
					if locateCenterOnScreen(images[x], grayscale=True, region=(int(searchX[images[x]]),int(searchY[images[x]]),searchM[0]*screenScalingFactor,searchM[1]*screenScalingFactor)) is not None:
						(coord[0], coord[1]) = locateCenterOnScreen(images[x], grayscale=True, region=(int(searchX[images[x]]),int(searchY[images[x]]),searchM[0]*screenScalingFactor,searchM[1]*screenScalingFactor))
						found = not found
				else:
					if locateCenterOnScreen(images[x], grayscale=True) is not None:
						(coord[0], coord[1]) = locateCenterOnScreen(images[x], grayscale=True)
						searchX[images[x]] = str(coord[0] - searchM[0]/2*screenScalingFactor)
						searchY[images[x]] = str(coord[1] - searchM[1]/2*screenScalingFactor)
						found = not found
				if found:
					mouseClick(coord[0]/screenScalingFactor, coord[1]/screenScalingFactor)
					print("[" + datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m %H:%M:%S') + "] - Clicked '" + images[x] + "'")
					if images[x] == imagesToggle:
							started = not started
					found = not found
			except IOError as e:
				print("Catching IO Error from pyautogui")
	else:
		if buffNow:
			castBuff()
			buffNow = not buffNow
		if summonNow:
			castSummon()
			summonNow = not summonNow

		mouseClick(questStart[0], questStart[1])
		print("[" + datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m %H:%M:%S') + "] - Clicked 'Start Quest'")
		started = not started

def mouseClick(xi,yi):
	mouseDown(x=xi, y=yi)
	time.sleep(random.uniform(0.4,0.7))
	mouseUp()

def castBuff():
	if buffSwitch:
		keyPress(buffButtonSwitch, random.uniform(0.1,0.3))
	rand = random.choice(random.sample(range(buffWaitMin,buffWaitMax),5))
	threading.Timer(rand, buffToggle).start()
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
