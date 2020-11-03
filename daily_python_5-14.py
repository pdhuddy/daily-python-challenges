def countString(fullString, findString):
	index = 0
	count = 0
	while True:
		if fullString.find(findString, index) == -1:
			break
		else:
			count += 1
			index = fullString.find(findString, index) + 1
		
	return count

def main():
	fullString = input("Enter a string: ")
	findString = input("Enter a substring: ")
	print(findString + " is in " + fullString + " " + str(countString(fullString, findString)) + " times")

main()