"""
This is an module used for simulate flipping coins.
"""

import random

def flip_coin():
	side = random.randint(0,1)
	if side == 0:
		return "head"
	else:
		return "tail"
	