import cardGame

layouts = {"D": [], "C": [], "H": [], "S": []}
ACE_HIGH = False


def getNumberOfPlayers():
    """ Gets number of player's from user.
        Number of players must be at least 3
        Returns an int """
    numberOfPlayers = int(input("Please enter the number of players: "))
    while not numberOfPlayers >= 3:
        numberOfPlayers = int(input(
            "Minimum number of please is 3, please enter number of players: "))
    return numberOfPlayers


def getStartingPlayer(hands):
    """ Determines which player starts.
        Starting player has Seven of Spades.
        Returns int, -1 if card not found """
    startingPlayer = cardGame.getHandIndexOfCard(hands, "S7")
    if startingPlayer is None:
        return -1
    return startingPlayer


def getNextPlayer(currentPlayer, numberOfPlayers):
    """ Gets next player, loops back to first player
        when after last player has been reached
        Returns int """
    return (currentPlayer + 1) % numberOfPlayers


def isGameOver(hands):
    """ Determines if game is over.
        Game is over when one player's hand is empty """
    for hand in hands:
        if len(hand) == 0:
            return True
    return False


def printLayouts():
    """ Prints layouts (card's played) to the screen
        Doesn't Return """
    for suit in layouts.keys():
        print(suit + " - " + str(layouts[suit]))


def getPlayerCommand():
    """ Get's an input from the user
        Returns String """
    command = input("Enter card to play, 'pass' or 'quit': ")
    return command


def getValidCards():
    """ Gets all the valid cards that could be played
        Returns list Strings """
    validCards = []
    for suit in layouts.keys():
        playedCards = layouts[suit]
        if len(playedCards) == 0:
            validCards.append(suit + "7")
        else:
            validCards += getNextLowerAndUpperCard(suit, playedCards)
    return validCards


def getNextLowerAndUpperCard(suit, cards):
    """ Gets the next lower and highest card.
        Assumes cards are sorted from lowest to highest value
        Return list """
    if len(cards) == 0:
        return None
    cardsToReturn = []
    lowestCard = cards[0]
    highestCard = cards[-1]
    lowestCardValue = cardGame.getCardValue(lowestCard, ACE_HIGH)[1:]
    # don't add a lower card if one doesn't exist
    if lowestCardValue > 1:
        cardsToReturn.append(
            cardGame.convertCardToRank(suit + str(lowestCardValue - 1))
        )
    highestCardValue = cardGame.getCardValue(highestCard, ACE_HIGH)
    # don't add a higher card if one doesn't exist
    if highestCardValue < 13:
        cardsToReturn.append(
            cardGame.convertCardToRank(suit + str(highestCardValue + 1))
        )
    return cardsToReturn


def isValidCommand(command, hand):
    """ Determines if command given is valid
        Checks if player has a valid card that could be played
        Returns Boolean """
    if command == "quit":
        return True

    validCards = getValidCards()
    validMoves = list(filter(lambda card: card in validCards, hand))

    if len(validMoves) == 0 and command == "pass":
        return True

    return command in validMoves


def sortHands(hands):
    """ Sort each hand
        Doesn't Return """
    for hand in hands:
        cardGame.sortHandByRank(hand)


def getWinningPlayer(hands):
    """ Gets the winning player, index of empty hand plus 1
        First player is player 1
        Returns int """
    for index, hand in enumerate(hands):
        if len(hand) == 0:
            return index + 1
    return -1


def updateHandAndLayouts(pickedCard, hand):
    """ Removes card from hand and adds to the layouts in sorted order
        Assumes picked card is a valid card
        Doesn't Return """
    hand.remove(pickedCard)
    valueCard = cardGame.convertCardToValue(pickedCard, ACE_HIGH)
    suit = valueCard[0]
    value = int(valueCard[1:])
    if value < 7:
        layouts[suit].insert(0, pickedCard)
    else:
        layouts[suit].append(pickedCard)


def initialSetUp():
    """ Perform initial setup for game
        Returns a tuple of starting variables
        deck, hands, numberOfPlayers, startingPlayer """
    deck = cardGame.getDeck()
    cardGame.shuffleDeck(deck)
    numberOfPlayers = getNumberOfPlayers()
    hands = cardGame.dealCards(deck, 0, numberOfPlayers)
    sortHands(hands)
    startingPlayer = getStartingPlayer(hands)
    return deck, hands, numberOfPlayers, startingPlayer


def main():
    """ Main Game Function """
    deck, hands, numberOfPlayers, currentPlayer = initialSetUp()

    while True:
        print()
        print("Player " + str(currentPlayer + 1) + "'s turn:")
        currentPlayerHand = hands[currentPlayer]
        print("Your hand is - " + str(currentPlayerHand))
        printLayouts()
        command = getPlayerCommand()

        while not isValidCommand(command, currentPlayerHand):
            print("Invalid Command!")
            print()
            print("Player " + str(currentPlayer + 1) + "'s turn:")
            print("Your hand is - " + str(currentPlayerHand))
            printLayouts()
            command = getPlayerCommand()

        if command not in ["pass", "quit"]:
            updateHandAndLayouts(command, currentPlayerHand)

        if isGameOver(hands) or command == "quit":
            break

        currentPlayer = getNextPlayer(currentPlayer, numberOfPlayers)

    if isGameOver(hands):
        print("Player " + str(getWinningPlayer(hands)) + " wins!")
    print("Goodbye")

if __name__ == "__main__":
    main()
