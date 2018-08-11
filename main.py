#############################################################
# A simple (random) MapleStory M farmer by sending			#
# keystrokes to an Android emulator (i.e. BlueStacks)		#
#															#
# Warning: You can get banned from MapleStory M for using	#
#          this as it is a form of simple botting.			#
#															#
# There are four (4) files:									#
# 		- main.py (for launching the bot)					#
#		- mapleFarmer.py (actual farming functions)			#
#		- keypress.py (for handling keypresses)				#
#		- requirements.txt (for installing pre-req)			#
#															#
# Author: shadowandy[dot]sg[at]gmail[dot]com				#
# Web: www.shadowandy.net									#
#############################################################

from mapleFarmer import castSkill, castBuff, castSummon, charMove
import time

# Allowing time to toggle to BlueStacks
time.sleep(2.5)

# Casting Buffs and Summons
castBuff()
castSummon()

# Looping through farming
while True:
	castSkill()
	charMove()