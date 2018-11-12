from mapleFarmer import charMove, castSummon, castBuff, castSkill
import time
import random

# Allowing time to toggle to BlueStacks
time.sleep(2.5)
castBuff()
castSummon()

# Looping through farming
while True:
	castSkill()
	time.sleep(random.uniform(0.2,0.4))
	charMove()
	time.sleep(random.uniform(0.3,0.5))
