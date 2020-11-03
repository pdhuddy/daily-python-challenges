import random

def diceGame():
	roll = input("Would you like to roll the dice (y/n) ")
	rollCounts = [0,0,0,0,0,0,0,0,0,0,0,0]
	doubles = 0
	while roll == "y":
		dice1 = random.randint(1,6)
		dice2 = random.randint(1,6)
		if dice1 == dice2:
			doubles += 1
		value = dice1 + dice2
		rollCounts[value-1] += 1
		print("You rolled a " + str(value))
		roll = input("Would you like to roll the dice (y/n) ")

	maxVal = 0
	maxRolls = []
	print("Roll Counts")
	for i in range(0, len(rollCounts)):
		print(str(i+1) + ": " + str(rollCounts[i]))
		if rollCounts[i] > maxVal:
			maxRolls = [i+1]
			maxVal = rollCounts[i]
		elif maxVal == rollCounts[i]:
			maxRolls.append(i+1)

	print("Most common rolls: " + str(maxRolls))
	print("Doubles: " + str(doubles))

diceGame()