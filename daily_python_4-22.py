import math

def getChange(change):
	quarters = math.floor(change/25)
	change -= quarters * 25
	dimes = math.floor(change/10)
	change -= dimes * 10
	nickels = math.floor(change/5)
	change -= nickels * 5

	changeStr = ""
	if quarters > 0: changeStr += str(quarters) + " quarter(s) "
	if dimes > 0: changeStr += str(dimes) + " dime(s) "
	if nickels > 0: changeStr += str(nickels) + " nickel(s) "
	if change > 0: changeStr += str(change) + " penny(s)"
	print(changeStr)

def main():
	inp = input("Enter an amount: ")
	change = int(inp)
	getChange(change)

main()