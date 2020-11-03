def switchCase(inp, num):
	count = 0
	inpArray = list(inp)
	while count < len(inpArray):
		if (count+1) % num == 0:
			char = inpArray[count]
			if char.isupper():
				char = char.lower()
			else:
				char = char.upper()
			inpArray[count] = char
		count += 1
	inp = "".join(inpArray)
	print(inp)

def main():
	inp = input("Enter a string: ")
	num = int(input("Enter a num: "))
	switchCase(inp, num)

main()