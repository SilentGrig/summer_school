import sevens


def testCorrectStartingPlayerReturned():
    hands = []
    playerOneHand = ["3H", "7S", "KC"]
    playerTwoHand = ["AS", "7C", "QD"]
    hands.append(playerOneHand)
    hands.append(playerTwoHand)
    startingPlayer = sevens.getStartingPlayer(hands)
    assert(startingPlayer == 0)


def testNoPlayerReturnedWhenNoSevenOfSpades():
    hands = []
    playerOneHand = ["3H", "7D", "KC"]
    playerTwoHand = ["AS", "7C", "QD"]
    hands.append(playerOneHand)
    hands.append(playerTwoHand)
    startingPlayer = sevens.getStartingPlayer(hands)
    assert(startingPlayer == -1)


def getNextPlayerReturnsNextPlayer():
    currentPlayer = 0
    numberOfPlayers = 4
    assert(sevens.getNextPlayer(currentPlayer, numberOfPlayers) == 1)


def getNextPlayerReturnsIndexZeroAfterLastPlayer():
    currentPlayer = 2
    numberOfPlayers = 3
    assert(sevens.getNextPlayer(currentPlayer, numberOfPlayers) == 0)


testCorrectStartingPlayerReturned()
testNoPlayerReturnedWhenNoSevenOfSpades()
getNextPlayerReturnsNextPlayer()
getNextPlayerReturnsIndexZeroAfterLastPlayer()

