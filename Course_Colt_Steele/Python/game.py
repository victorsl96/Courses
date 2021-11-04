from random import randint

p_score = 0
pc_score = 0

while p_score < 2 and pc_score < 2:
	
	print(f"Player score: {p_score} and Pc score: {pc_score}")
	print("...rock...")
	print("...paper...")
	print("...scissors...")

	player1 = input("Your move: ").lower()
	rand_num = randint(0,2)

	if rand_num == 0:
		pc = "rock"
	elif rand_num == 1:
		pc = "paper"
	else:
		pc = "scissors"

	print(f"pc plays: {pc}")

	if player1 == pc:
		print("Tie")

	elif player1 == "rock":
		if pc == "scissors":
			print("player wins")
			p_score += 1
		else:
			print("pc wins")
			pc_score += 1

	elif player1 == "paper":
		if pc == "rock":
			print("player wins")
			p_score += 1
		else:
			print("pc wins")
			pc_score += 1

	elif player1 == "scissors":
		if pc == "paper":
			print("player wins")
			p_score += 1
		else:
			print("pc wins")
			pc_score += 1

	else:
		print("Something went wrong!")