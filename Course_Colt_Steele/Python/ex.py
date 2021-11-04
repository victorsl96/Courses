# EX: 1
# x = int(input("How many times do I have to tell you? "))

# for num in range(x):
# 	print("CLEAN UP YOUR ROOM!")

# EX: 2

# for x in range(1,21):
# 	if x == 4 or x == 13:
# 		print(f"{x} is UNLUCKY")
# 	elif x % 2 == 0:
# 		print(f"{x} is even")
# 	elif x % 2 != 0:
# 		print(f"{x} is odd")

# x = 1
# while x <= 20:
# 	if x == 4 or x == 13:
# 		print(f"{x} is UNLUCKY")
# 	elif x % 2 == 0:
# 		print(f"{x} is even")
# 	elif x % 2 != 0:
# 		print(f"{x} is odd")
# 	x += 1
# EX: 3 smileys: print("\U0001f600")
#x = 1
#while x <=10:
#	print("*" * x)
#	x += 1

# for x in range(1,10):
# 	print("*" * x)

# EX: 4 copycat

x = input("Hey how's it going? ")
while x != "stop copying me":
	x = input(f"{x}\n")
print("fine you win!")