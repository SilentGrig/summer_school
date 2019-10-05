import random

alphabet = "abcdefghijklmnopqrstuvwxyz"

def anagram(word):
	word = list(word)
	for index in range(len(word)):
		letter = getLowerCaseLetter(word, index)

		# if character to swap isn't in alphabet then leave it where it is
		if letter not in alphabet:
			continue

		swapIndex = getRandomIndexFromCurrentPosition(word, index)
		letterToSwap = getLowerCaseLetter(word, swapIndex)

		# only swap with other characters in alphabet
		while letterToSwap not in alphabet:
			swapIndex = getRandomIndexFromCurrentPosition(word, index)
			letterToSwap = getLowerCaseLetter(word, swapIndex)

		swapElements(word, index, swapIndex)
	
	return "".join(word)

def getLowerCaseLetter(array, index):
	return array[index].lower()

def getRandomIndexFromCurrentPosition(array, fromIndex):
	return random.randint(fromIndex, len(array) - 1)

def swapElements(array, firstIndex, secondIndex):
	temp = array[firstIndex]
	array[firstIndex] = array[secondIndex]
	array[secondIndex] = temp

word = input("Give me a word: ")
print("Anagram is: " + anagram(word))
