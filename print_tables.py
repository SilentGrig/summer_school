FILENAME = "games.txt"

with open(FILENAME, "r") as file:
	data = file.readlines()


def getLongestStringPerColumn(headings, data):
	longestStrings = [0] * len(headings)

	for i in range(len(data)):
		row = data[i].split(",")
		for j in range(len(row)):
			if len(row[j]) > longestStrings[j]:
				longestStrings[j] = len(row[j])
	
	# add two extra charactesr for spacing
	for index, longestString in enumerate(longestStrings):
		longestStrings[index] = longestString + 2;

	return longestStrings


def printLineBreak(longestStrings):
	for stringLength in longestStrings:
		print("+" + "-" * (stringLength), end="")
	print("+")


def printLine(row, longestStrings):
	for index, word in enumerate(row):
		print("|" + padWord(word, longestStrings[index]), end="")
	print("|")


def padWord(word, totalLength):
	# filter out newline
	word = word.split("\n")[0]
	# pad start of word
	word = " " + word
	# pad end of word
	while len(word) < totalLength:
		word += " "
	return word


headings = data[0].split(",")
longestStrings = getLongestStringPerColumn(headings, data)

printLineBreak(longestStrings)
printLine(headings, longestStrings)
printLineBreak(longestStrings)

for i in range(1, len(data)):
	row = data[i].split(",")
	# only print out rows with same number of columns as the headings
	# this filters out empy lines
	if len(row) == len(headings):
		printLine(row, longestStrings)

printLineBreak(longestStrings)
