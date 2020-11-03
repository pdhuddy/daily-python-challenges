def displayOrder(order):
	chickenCost = 5
	fryCost = 1
	sodaCost = 2
	numChickenOrdered = 0
	numFriesOrdered = 0
	numSodaOrdered = 0
	cost = 0
	for element in order:
		if element == "done":
			continue
		splitElement = element.split(" ")
		numFood = int(splitElement[0])
		food = splitElement[1]
		if food == "1":
			numChickenOrdered += numFood
			cost += numFood * chickenCost
		elif food == "2":
			numFriesOrdered += numFood
			cost += numFood * fryCost
		elif food == "3":
			numSodaOrdered += numFood
			cost += numFood * sodaCost
	print("You ordered " + str(numChickenOrdered) + " chicken nugget(s), " + str(numFriesOrdered) + " fry(s), " + str(numSodaOrdered) + " soda(s)")
	print("Your total is $" + str(cost))


def displayMenu():
	print("Menu")
	print("1. 10 Chicken Nuggets: $5")
	print("2. Medium french fry: $1")
	print("3. Medium soda: $2")


def main():
	displayMenu()
	order = []
	inp = ""
	while inp != "done":
		inp = input()
		order.append(inp)
	displayOrder(order)

main()