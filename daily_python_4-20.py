import random
randomInt = str(random.randint(1000,9999))

def analyzeGuess(inp):
	if inp == randomInt:
		return True

	rightCount = 0
	wrongCount = 0
	for i in range(len(randomInt)):
		if randomInt[i] == inp[i]:
			rightCount += 1
		elif inp[i] in randomInt:
			wrongCount += 1

	print(str(rightCount) + " right, " + str(wrongCount) + " wrong")
	return False


def main():
	guess = False
	while guess is False:
		inp = input("Enter a guess: ")
		guess = analyzeGuess(inp)
	print("Correct!")

main()