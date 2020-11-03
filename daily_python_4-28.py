def messWithSentence(sentence, word):
	words = sentence.split(" ")
	words.reverse()
	joinStr = " " + word + " "
	newSentence = joinStr.join(words)
	print(newSentence)

def alternateMessWithSentence(sentence, word):
	words = sentence.split(" ")
	words = [word for word in reversed(words)]
	joinStr = " " + word + " "
	newSentence = joinStr.join(words)
	print(newSentence)

def main():
	sentence = input("Enter a sentence: ")
	word = input("Enter a word: ")
	alternateMessWithSentence(sentence, word)

main()