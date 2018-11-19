from mapleFarmer import charMove, castSkill, castSummon, castBuff
import time
import random

# Allowing time to toggle to BlueStacks
time.sleep(2.5)
castSummon()
castBuff()

# Looping through farming
while True:
	charMove()
	time.sleep(random.uniform(0.1,0.3))
	castSkill()
	time.sleep(random.uniform(2,4))