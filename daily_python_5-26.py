def main():
	run = True
	while(run):
		inp = input("Enter d for dog, h for human, or q for quit: ")
		if inp is "d":
			dogAge = int(input("Enter your dog's age: "))
			print("Your dog is " + str(dogAge*7) + " in human years")
		elif inp is "h":
			humanAge = float(input("Enter your human's age: "))
			print("Your human is " + str(humanAge/7) + " in dog years")
		elif inp is "q":
			print("Goodbye")
			run = False
		else:
			print("Invalid input")

main()