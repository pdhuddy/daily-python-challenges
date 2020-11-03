def fizzbuzz(num):
	fb = ""
	if num % 3 == 0:
		fb += "FIZZ"
	if num % 5 == 0:
		fb += "BUZZ"
	print(fb)

def main():
	num = int(input("Enter a number: "))
	fizzbuzz(num)

main()