def fac(num):
	if num <= 0: return 0
	if num == 1: return 1
	return num * fac(num - 1)

def main():
	num = int(input("Enter a number: "))
	print("The factorial of " + str(num) + " is " + str(fac(num)))

main()