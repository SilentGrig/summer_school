import random

games = [{
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}, {
    "Darth Vader": "Emperor",
    "Emperor": "Luke Skywalker",
    "Luke Skywalker": "Darth Vader",
}, ]


def getGameType():
	while True:
		try:
			gameType = int(input("Enter game type - 0 for standard, or 1 for starwars: "))
			return gameType
		except ValueError:
			print("Please enter 0 or 1")


def getComputerChoice(handCounter):
	options = list(handCounter.keys())
	return random.choice(options)


def buildChoicesString(handCounter):
	output = "Please type "
	options = list(handCounter.keys())
	for index, option in enumerate(options):
		if index == len(options) - 1:
			output += "or " + option + " ('quit' to quit): "
		else:
			output += option + ", "
	return output


def getPlayerChoice(handCounter):
	playerChoice = input(buildChoicesString(handCounter))
	return playerChoice


def validatePlayerChoice(choice, handCounter):
	if choice == "quit":
		return True
	return choice in handCounter


def determineWinner(playerChoice, computerChoice,handCounter):
	if handCounter[playerChoice] == computerChoice:
		return "player"
	elif handCounter[computerChoice] == playerChoice:
		return "computer"
	return "draw"


def announceWinner(winner):
	if winner == "draw":
		print("It was a draw!")
	elif winner == "player":
		print("You win!")
	elif winner == "computer":
		print("Computer won!")


def updateScores(winner, numberOfPlayerWins, numberOfComputerWins):
	if winner == "player":
		numberOfPlayerWins += 1
	elif winner == "computer":
		numberOfComputerWins += 1
	return (numberOfPlayerWins, numberOfComputerWins)


def pluraliseWord(word, count):
	if count == 1:
		return word
	return word + "s"


def playGame():
	numberOfPlayerWins = 0
	numberOfComputerWins = 0

	gameType = getGameType()
	handCounter = games[gameType]

	while True:
		print()
		computerChoice = getComputerChoice(handCounter)
		playerChoice = getPlayerChoice(handCounter)

		while not validatePlayerChoice(playerChoice, handCounter):
			print("Invalid input. ", end="")
			playerChoice = getPlayerChoice(handCounter)

		if playerChoice == "quit":
			break;

		winner = determineWinner(playerChoice, computerChoice, handCounter)
		print("Player choice: " + playerChoice + " - Computer choice: " + computerChoice)
		announceWinner(winner)
		numberOfPlayerWins, numberOfComputerWins = updateScores(winner, numberOfPlayerWins, numberOfComputerWins)
	
	if numberOfPlayerWins > 0 or numberOfComputerWins > 0:
		print("You won " + str(numberOfPlayerWins) + " " + pluraliseWord("time", numberOfPlayerWins) + " and the computer won " 
				+ str(numberOfComputerWins) + " " + pluraliseWord("time", numberOfComputerWins) + ".")


def main():
	playing = True
	while playing:
		playGame()
		print()
		playAgain = input("Do you want to play again? ").lower()
		if playAgain in ["no", "n"]:
			playing = False
	
	print("Goodbye!")

if __name__ == "__main__":
	main()
