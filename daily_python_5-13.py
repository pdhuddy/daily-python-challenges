import re

def checkInput(inp):
	regex = re.compile('\d*[+*/-]\d*')
	return regex.match(inp)

def compute(inp):
	ans = ""
	if "+" in inp:
		[x,y] = inp.split('+')
		ans = str(int(x)+int(y))
	elif "*" in inp:
		[x,y] = inp.split('*')
		ans = str(int(x)*int(y))
	elif "/" in inp:
		[x,y] = inp.split('/')
		ans = str(int(x)/int(y))
	else:
		[x,y] = inp.split('-')
		ans = str(int(x)-int(y))
	print("The answer is: " + ans)

def main():
	while True:
		inp = input("Enter an operation: ")
		if checkInput(inp):
			compute(inp)
			break
		else:
			print("Bad formatting!")

main()