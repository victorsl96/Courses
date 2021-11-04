from random import randint

def flip_coin():
	r = randint(0,1)
	if r == 0:
		return 'Heads'
	else:
		return 'Tails'
print(flip_coin())