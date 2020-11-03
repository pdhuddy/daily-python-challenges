def printChoice():
	print("Pick a choice number")
	print("1) Rock")
	print("2) Paper")
	print("3) Scissor")

def getChoice(playerNum):
	print("Player " + str(playerNum) + "'s turn")
	playerChoice = 0
	while playerChoice != 1 and playerChoice != 2 and playerChoice != 3:
		printChoice()
		playerChoice = int(input())
	return playerChoice

def getWinner(p1Choice, p2Choice):
	if p1Choice == "rock":
		if p2Choice == "scissor":
			return 1
		else:
			return 2
	elif p1Choice == "paper":
		if p2Choice == "rock":
			return 1
		else:
			return 2
	else:
		if p2Choice == "paper":
			return 1
		else:
			return 2


def main():
	choices = ["rock", "paper", "scissor"]
	winCount = int(input("How many wins to win the game: "))
	p1WinCount = 0
	p2WinCount = 0
	roundNum = 1
	while p1WinCount < winCount and p2WinCount < winCount:
		print("ROUND" + str(roundNum))
		p1Choice = 0
		p2Choice = 0
		while p1Choice == p2Choice:
			p1Choice = choices[getChoice(1)-1]
			p2Choice = choices[getChoice(2)-1]
			if p1Choice == p2Choice:
				print("TIE... TRY AGAIN")
		winnerNum = getWinner(p1Choice, p2Choice)
		if winnerNum == 1: 
			p1WinCount += 1
		else:
			p2WinCount += 1
		print("Player " + str(winnerNum) + " wins round " + str(roundNum))
		roundNum += 1

	if p1WinCount == winCount:
		print("PLAYER 1 WINS!!!!")
	else:
		print("PLAYER 2 WINS!!!!")

main()




