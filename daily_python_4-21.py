def isInt(str):
	try:
		int(str)
		return True
	except ValueError:
		return False

def checkString(inp):
	qCount = 0
	firstInt = 0
	for item in inp:
		if isInt(item) is True:
			if firstInt + int(item) == 10 and qCount is not 3:
				return False
			firstInt = int(item)
			qCount = 0
		elif item is "?":
			qCount += 1

	return True

def main():
	inp = input("Enter a test string: ")
	if checkString(inp) is True:
		print("VALID")
	else:
		print("INVALID")

main()