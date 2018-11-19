<<<<<<< HEAD
from mapleFarmer import charMove, castSkill, castSummon, castBuff, toggleAuto
=======
from mapleFarmer import charMove, castSummon, castBuff, castSkill
>>>>>>> cee314b2f2f9e3bef22e0a182598a6dcb650805d
import time
import random

# Allowing time to toggle to BlueStacks
time.sleep(2.5)
<<<<<<< HEAD
toggleAuto()
#castSummon()
#castBuff()

# Looping through farming
while True:
	charMove()
	castSkill()
	# time.sleep(random.uniform(0.2,0.5))
	# time.sleep(random.uniform(1,2))
=======
castBuff()
castSummon()

# Looping through farming
while True:
	castSkill()
	time.sleep(random.uniform(0.2,0.4))
	charMove()
	time.sleep(random.uniform(0.3,0.5))
>>>>>>> cee314b2f2f9e3bef22e0a182598a6dcb650805d
