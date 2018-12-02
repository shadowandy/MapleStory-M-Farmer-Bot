from mapleQuestBot import questBot
import time
import random

# Allowing time to toggle to BlueStacks
time.sleep(2.5)

# Looping through farming
while True:
	questBot()
	time.sleep(random.uniform(0.5,1))