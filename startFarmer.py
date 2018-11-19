from mapleFarmer import charMove, castSkill, castSummon, castBuff, toggleAuto
import time
import random

# Allowing time to toggle to BlueStacks
time.sleep(2.5)
toggleAuto()
#castSummon()
#castBuff()

# Looping through farming
while True:
	charMove()
	castSkill()
	# time.sleep(random.uniform(0.2,0.5))
	# time.sleep(random.uniform(1,2))