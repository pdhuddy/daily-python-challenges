def zipper(list1, list2):
	maxLength = len(list1) if len(list1) > len(list2) else len(list2)
	count = 0
	zipList = []
	while count < maxLength:
		if count < len(list1):
			zipList.append(list1[count])
		if count < len(list2):
			zipList.append(list2[count])
		count +=1
	return zipList

def main():
	inp = input("Enter a comma separated list: ")
	list1 = inp.split(",")
	inp = input("Enter another comma separated list: ")
	list2 = inp.split(",")
	zipList = zipper(list1, list2)
	print(zipList)

main()
