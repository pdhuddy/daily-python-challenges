def reverse(inputString):
	count = len(inputString) - 1
	reverseString = ""
	while count >=0:
		reverseString += inputString[count]
		count -= 1
	return reverseString

def main():
	inp = input("Input a string: ")
	reverseString = reverse(inp)
	print(reverseString)

main()