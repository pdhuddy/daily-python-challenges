members = []

class Member:
	def __init__(self, name, ttClass, position, hometown, gradYear, major, big, littles):
		self.name = name
		self.ttClass = ttClass
		self.major = major
		self.hometown = hometown
		self.gradYear = gradYear
		self.position = position
		self.big = big
		self.littles = littles
	def __str__(self):
		nameStr = "Name: " + self.name + "\n"
		ttClassStr = "Theta Tau Class: " + self.ttClass + "\n"
		positionStr = "Position: " + self.position + "\n"
		hometownStr = "Hometown: " + self.hometown + "\n"
		gradYearStr = "Graduation Year: " + str(self.gradYear) + "\n"
		majorStr = "Major: " + self.major + "\n"
		bigStr = "Big: " + self.big + "\n"
		littlesStr = "Little(s): " + ", ".join(self.littles) + "\n"
		return nameStr + ttClassStr + positionStr + hometownStr + gradYearStr + majorStr + bigStr + littlesStr
	def getName(self):
		return self.name
	def setName(self, name):
		self.name = name
	def getTtClass(self):
		return selt.ttClass
	def setTtClass(self, ttClass):
		self.ttClass = ttClass
	def getPosition(self):
		return self.position
	def setPosition(self, position):
		self.position = position
	def getHometown(self):
		return self.hometown
	def setHometown(self, hometown):
		self.hometown = hometown
	def getGradYear(self):
		return self.gradYear
	def setGradYear(self, gradYear):
		self.gradYear = gradYear
	def getMajor(self):
		return self.major
	def setMajor(self, major):
		self.major = major
	def getBig(self):
		return self.big
	def setBig(self, big):
		self.big = big
	def getLittles(self):
		return self.littles
	def setLittles(self, littles):
		self.littles = littles

def getMemberByName(name):
	for member in members:
		if member.getName() == name:
			return member

def addMember():
	name = input("Enter the member's name: ")
	ttClass = input("Enter the member's Theta Tau class: ")
	position = input("Enter the member's position, or NONE if they don't have one: ")
	hometown = input("Enter the member's hometown: ")
	gradYear = int(input("Enter the member's graduation year: "))
	major = input("Enter the member's major: ")
	big = input("Enter the member's big: ")
	littles = []
	little = ""
	while True:
		little = input("Enter a little one at a time, and enter none when there are no more: ")
		if little == "none":
			break
		littles.append(little)
	members.append(Member(name, ttClass, position, hometown, gradYear, major, big, littles))

def displayMember():
	print("Display Menu")
	print("a - display all members")
	print("m - display a certain member")
	inp = input()
	if inp is "a":
		for member in members:
			print(member)
	elif inp is "m":
		memberName = input("Enter the member's full name: ")
		member = getMemberByName(memberName)
		print(member)
	else:
		print("Please enter a valid command")
		displayMember()

def main():
	while True:
		print("Menu")
		print("a - add a member")
		print("d - display members")
		print("q - quit")
		inp = input()
		if inp is "a":
			addMember()
		elif inp is "d":
			displayMember()
		elif inp is "q":
			break
		else:
			print("Please enter a valid command")
	print()

main()