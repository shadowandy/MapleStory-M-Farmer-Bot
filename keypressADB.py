from adb.client import Client as AdbClient

import time
import random

client = AdbClient(host="127.0.0.1", port=5037)
device = client.device("emulator-5554")


def keyPress(keyValue, duration):
	dur = int(duration * 1000)
	dx = 0
	dy = 0

	if keyValue == "left":
		dx = 200
		dy = 800
	elif keyValue == "right":
		dx = 400
		dy = 800
	elif keyValue == "up":
		dx = 250
		dy = 700
	elif keyValue == "down":
		dx = 250
		dy = 900
	elif keyValue == "c":
		dx = 1600
		dy = 800
	elif keyValue == "a":
		dx = 1500
		dy = 900
	elif keyValue == "s":
		dx = 1500
		dy = 800
	elif keyValue == "d":
		dx = 1600
		dy = 700
	elif keyValue == "f":
		dx = 1700
		dy = 700
	else: #p
		dx = 500
		dy = 900
	device.shell("input swipe " + str(dx) + " " + str(dy) + " " + str(dx) + " " + str(dy) + " " + str(dur))
	print ("'" + keyValue + "'" + " key pressed!")
	time.sleep(random.uniform(0.1,0.2))

def mouseClick(xi,yi):
	dx = 800
	dy = 800
	device.shell("input swipe " + str(dx) + " " + str(dy) + " " + str(dx) + " " + str(dy) + " 500")


#keyPress('c', 0.3)