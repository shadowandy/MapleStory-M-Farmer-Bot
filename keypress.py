from pyautogui import keyDown, keyUp
import time
import random

def keyPress(keyValue, duration):
	keyDown(keyValue)
	time.sleep(duration)
	keyUp(keyValue)
	print ("'" + keyValue + "'" + " key pressed!")
	time.sleep(random.uniform(0.1,0.2))