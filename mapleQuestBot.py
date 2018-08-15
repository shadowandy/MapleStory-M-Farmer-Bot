from pyautogui import locateCenterOnScreen, locateOnScreen, click, mouseDown, mouseUp
import random
import threading
import time

#screenDimension = [2560, 1440]
#screenScalingFactor = 1
screenDimension = [2880, 1800]
screenScalingFactor = 2

status = ['1/4 Starting Quest', 'Skipping Narratives', '2/4 Accepting Quest', '3/4 Completing Quest', '4/4 Claiming Rewards', '2/4 Accepting Quest', '3/4 Completing Quest']
images = ['questScroll.png', 'questSkip.png', 'questAccept.png', 'questComplete.png', 'questClaim.png', 'questAvailable.png', 'questMultiComplete.png']

regionSizeInit = [screenDimension[0]/2, screenDimension[1]/2]
regionSizeScaled = [240, 50]

regionSearchX = [0, 0, screenDimension[0]/2, screenDimension[0]/2, screenDimension[0]/4, 0, 0]
regionSearchY = [0, 0, screenDimension[1]/2, screenDimension[1]/2, screenDimension[1]/2, screenDimension[1]/2, screenDimension[1]/2]
regionSearchW = [regionSizeInit[0]-1, regionSizeInit[0]-1, regionSizeInit[0]-1, regionSizeInit[0]-1, regionSizeInit[0]-1, regionSizeInit[0]-1, regionSizeInit[0]-1]
regionSearchH = [regionSizeInit[1]-1, regionSizeInit[1]-1, regionSizeInit[1]-1, regionSizeInit[1]-1, regionSizeInit[1]-1, regionSizeInit[1]-1, regionSizeInit[1]-1]

started = 0

def questBot():
	global started, regionSearchX, regionSearchY, regionSearchH, regionSearchW
	if started:
		coord = [0, 0]
		for x in range(1,len(images)):
			if locateCenterOnScreen(images[x], grayscale=True, region=(regionSearchX[x], regionSearchY[x], regionSearchW[x], regionSearchH[x])) is not None:
				time.sleep(2)
				(coord[0], coord[1]) = locateCenterOnScreen(images[x], grayscale=True, region=(regionSearchX[x], regionSearchY[x], regionSearchW[x], regionSearchH[x]))
				mouseClick(coord[0]/screenScalingFactor, coord[1]/screenScalingFactor)
				print("x=" + str(coord[0]) + " y=" + str(coord[1]))
				if regionSearchW[x] != regionSizeScaled[0]:
					regionSearchX[x] = coord[0] - regionSizeScaled[0]/2*screenScalingFactor
					regionSearchY[x] = coord[1] - regionSizeScaled[1]/2*screenScalingFactor
					regionSearchW[x] = regionSizeScaled[0]*screenScalingFactor
					regionSearchH[x] = regionSizeScaled[1]*screenScalingFactor
				print(status[x])

				if x == 4:
					started = not started
				if x == 2 or x == 5:
					time.sleep(random.uniform(25,52))
	else:
		#mouseClick(480, 540)
		mouseClick(240, 380)
		print(status[0])
		started = not started

def mouseClick(xi,yi):
	mouseDown(x=xi, y=yi)
	time.sleep(0.5)
	mouseUp()
