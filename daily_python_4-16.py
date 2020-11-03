def oddOneOut(arr):
	if arr[0]%2 != arr[1]%2:
		if arr[1]%2 == arr[2]%2:
			return arr[0]
		else:
			return arr[1]

	oddOrEven = arr[0]%2
	i = 1
	while arr[i]%2 == oddOrEven:
		i += 1

	return arr[i]

def main():
	inp = input("Enter a comma separated list: ")
	inpArr = [int(i) for i in inp.split(",")]
	print(oddOneOut(inpArr))


main()