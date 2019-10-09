import cardGame

layouts = {"D": [], "C": [], "H": [], "S": []}


def getNumberOfPlayers():
    numberOfPlayers = int(input("Please enter the number of players: "))
    while not numberOfPlayers >= 3:
        numberOfPlayers = int(input("Minimum number of please is 3, please enter number of players: "))
    return numberOfPlayers


def getStartingPlayer(hands):
    startingPlayer = cardGame.getHandIndexOfCard(hands, "7S")
    if startingPlayer is None:
        return -1
    return startingPlayer


def getNextPlayer(currentPlayer, numberOfPlayers):
    return (currentPlayer + 1) % numberOfPlayers


def isGameOver(hands):
    return False


def printLayouts():
    for suit in layouts.keys():
        print(suit + " - " + str(layouts[suit]))


def getPlayerCommand(hand):
    command = input("Enter card to play or type 'pass' to pass: ")
    while not (command == "pass" or cardGame.doesHandContainCard(hand, command)):
        command = input("Enter card to play or type 'pass' to pass: ")
    return command

deck = cardGame.getDeck()
cardGame.shuffleDeck(deck)

numberOfPlayers = getNumberOfPlayers()
hands = cardGame.dealCards(deck, 0, numberOfPlayers)
startingPlayer = getStartingPlayer(hands)

currentPlayer = startingPlayer

while True:
    print("It is " + str(currentPlayer + 1) + "'s turn:")
    print("Your hand is - " + str(hands[currentPlayer]))
    printLayouts()
    command = getPlayerCommand()

    if isGameOver(hands):
        break

