import random

def flipAndRoll(guess):
	headOrTails = 1 if guess[1] == "H" else 2
	roll = int(guess[0])
	randFlip = 0
	randRoll = 0
	count = 0
	while randFlip != headOrTails or randRoll != roll:
		randFlip = random.randint(1,2)
		randRoll = random.randint(1,6)
		flipStr = "H" if randFlip == 1 else "T"
		print(str(randRoll) + flipStr)
		count += 1
	print("It took " + str(count) + " rolls to get " + guess)

def main():
	inp = input("Enter a guess: ")
	flipAndRoll(inp.upper())

main()