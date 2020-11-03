vowels = ["a", "e", "i", "o", "u"]

def convertToPigLatin(sentence):
	words = sentence.split(' ')
	pigLatin = []
	for word in words:
		if word[0].casefold() in vowels:
			pigLatinWord = word + "yay"
			pigLatin.append(pigLatinWord)
		else:
			print(word)
			index = 0
			for i in range(len(word)):
				if word[i] in vowels:
					index = i
					break
			pigLatinWord = word[i:len(word)] + word[0:i] + "ay"
			pigLatin.append(pigLatinWord)
	return " ".join(pigLatin)

def main():
	inp = input("Enter a sentence: ")
	pigLatin = convertToPigLatin(inp)
	print(pigLatin)

main()