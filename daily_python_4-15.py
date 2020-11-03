def everyOtherNegative(arr):
	i=0
	arr[0] = arr[0] * (-1)
	if len(arr) > 2:
		while i + 2 < len(arr):
			i += 2
			arr[i] = arr[i] * (-1)

	return arr

def main():
	inp = input("Enter a comma separated list: ")
	inpArr = [int(i) for i in inp.split(",")]
	print(everyOtherNegative(inpArr))

main()