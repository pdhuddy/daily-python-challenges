def displayAreas(x,y):
	print("Area of triangle: " + str(x*y*0.5))
	print("Area of rectangle: " + str(x*y))

def main():
	length = int(input("Input the length: "))
	height = int(input("Input the height: "))
	displayAreas(length, height)

main()