import cardGame

layouts = {"D": [], "C": [], "H": [], "S": []}
AceHigh = False


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


def getPlayerCommand():
    command = input("Enter card to play or type 'pass' to pass: ")
    while not command == "pass":
        command = input("Enter card to play or type 'pass' to pass: ")
    return command


def getValidCards():
    validCards = []
    for suit in layouts.keys():
        playedCards = layouts[suit]
        if len(playedCards) == 0:
            validCards.append("7" + suit)
        else:


def getNextLowerAndUpperCard(suit, cards):
    cardsToReturn = []
    lowestCard = cards[0]
    highestCard = card[-1]
    lowestCardValue = int(cardGame.convertCardToValue(lowestCard, AceHigh)[:2])
    if lowestCardValue > 1:
        cardsToReturn.append(cardGame.convertCardToRank(str(lowestCardValue + 1) + suit))
    highestCardValue = int(cardGame.convertCardToValue(highestCard, AceHigh)[:2])
    if highestCardValue < 12:

    return cardsToReturn





def isValidCommand(command, hand):



def initialSetUp():
    deck = cardGame.getDeck()
    cardGame.shuffleDeck(deck)
    numberOfPlayers = getNumberOfPlayers()
    hands = cardGame.dealCards(deck, 0, numberOfPlayers)
    startingPlayer = getStartingPlayer(hands)
    return deck, hands, numberOfPlayers, startingPlayer


def main():
    deck, hands, numberOfPlayers, currentPlayer = initialSetUp()

    while True:
        print("It is " + str(currentPlayer + 1) + "'s turn:")
        currentPlayerHand = hands[currentPlayer]
        print("Your hand is - " + str(currentPlayerHand))
        printLayouts()
        command = getPlayerCommand()

        if not command == "pass":
            pass

        if isGameOver(hands):
            break

main()
