def boo(inp):
	lowerCaseInput = inp.lower()
	if "boo" in lowerCaseInput:
		print("AHHHHHHH")
	else:
		print("You can't scare me")

def main():
	inp = input("Tell me something: ")
	boo(inp)

main()