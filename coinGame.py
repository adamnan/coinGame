#! /usr/bin/env python

import flipCoin

f = open("highscore.txt", "r+")

side = raw_input ("Guess the side of the coin: (type 'head' or 'tail')\t")

score = 0

while side == flipCoin.flip_coin():
	
	score += 1
	
	print("You are right, your score now is {}.".format(score))
	
	side = raw_input ("Guess the side of the coin: (type 'head' or 'tail')\t")
	
print("Sorry, you are wrong, your final score is {}.".format(score))

highscore = f.read()

if score >= int(highscore):
	print("Congratulation, you are the new highscore!")
	f.seek(0)
	f.write(str(score))


