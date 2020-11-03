import math

def binary(binaryString):
	bits = len(binaryString)-1
	decimalNum = 0
	for character in binaryString:
		decimalNum += math.pow(2, bits) * int(character)
		bits -= 1
	print(str(binaryString) + " in decimal is " + str(decimalNum))

def main():
	binaryString = input("Enter a binary number: ")
	binary(binaryString)

main()