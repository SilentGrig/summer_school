import random

handCounter = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

numberOfPlayerWins = 0
numberOfComputerWins = 0


def getComputerChoice():
    options = list(handCounter.keys())
    return random.choice(options)


def buildChoicesString():
    output = "Please type "
    options = list(handCounter.keys())
    for index, option in enumerate(options):
        if index == len(options) - 1:
            output += "or " + option + " ('quit' to quit): "
        else:
            output += option + ", "
        return output


def getPlayerChoice():
    playerChoice = input(buildChoicesString())
    return playerChoice


def validatePlayerChoice(choice):
    if choice == "quit":
        return True
    return choice in handCounter


def determineWinner(playerChoice, computerChoice):
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

while True:
    computerChoice = getComputerChoice()
    playerChoice = getPlayerChoice()

    while not validatePlayerChoice(playerChoice):
        print("Invalid input. ", end="")
        playerChoice = getPlayerChoice()

    if playerChoice == "quit":
        break

    winner = determineWinner(playerChoice, computerChoice)
    print("Player choice: " + playerChoice + " - Computer choice: " +
          computerChoice)
    announceWinner(winner)
    numberOfPlayerWins, numberOfComputerWins = updateScores(
        winner, numberOfPlayerWins, numberOfComputerWins)

if numberOfPlayerWins > 0 or numberOfComputerWins > 0:
    print("You won " + str(numberOfPlayerWins) + " " +
          pluraliseWord("time", numberOfPlayerWins) +
          " and the computer won " +
          str(numberOfComputerWins) + " " +
          pluraliseWord("time", numberOfComputerWins) + ".")

print("Goodbye!")
