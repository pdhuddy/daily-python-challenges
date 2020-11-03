def extractOddOrEven(nums, even):
	if even is True:
		returnNums = [num for num in nums if int(num) % 2 == 0]
	else:
		returnNums = [num for num in nums if int(num) % 2 == 1]
	return returnNums

def main():
	inp = input("Enter a comma separated list of integers: ")
	evenOdd = input("Choose to extract even or odd numbers: ")
	nums = inp.split(",")
	even = evenOdd == "even"
	oddOrEven = extractOddOrEven(nums, even)
	print(oddOrEven)

main()