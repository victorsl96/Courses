from random import randint

num = randint(1, 10)

playing = True

while playing == True:

	x = int(input("Guess a number between 1 and 10: "))

	if x == num:
		print("You guessed it! you won")
		c = input("keep playing? (y/n) ")
		if c == "y":
			num = randint(1, 10)

		elif c == "n":
			print("Thank you for playing!")
			playing = False

	elif x > num:
		print("Too high, try again")

	elif x < num:
		print("Too low, try again")

