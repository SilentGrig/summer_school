import sevens


def testCorrectStartingPlayerReturned():
    hands = []
    playerOneHand = ["H3", "S7", "CK"]
    playerTwoHand = ["SA", "C7", "DQ"]
    hands.append(playerOneHand)
    hands.append(playerTwoHand)
    startingPlayer = sevens.getStartingPlayer(hands)
    assert(startingPlayer == 0)


def testNoPlayerReturnedWhenNoSevenOfSpades():
    hands = []
    playerOneHand = ["H3", "D7", "CK"]
    playerTwoHand = ["SA", "C7", "DQ"]
    hands.append(playerOneHand)
    hands.append(playerTwoHand)
    startingPlayer = sevens.getStartingPlayer(hands)
    assert(startingPlayer == -1)


def testGetNextPlayerReturnsNextPlayer():
    currentPlayer = 0
    numberOfPlayers = 4
    assert(sevens.getNextPlayer(currentPlayer, numberOfPlayers) == 1)


def testGetNextPlayerReturnsIndexZeroAfterLastPlayer():
    currentPlayer = 2
    numberOfPlayers = 3
    assert(sevens.getNextPlayer(currentPlayer, numberOfPlayers) == 0)


def testGetNextLowerAndUpperCardsEmptyList():
    suit = "D"
    cards = []
    nextCards = sevens.getNextLowerAndUpperCard(suit, cards)
    assert(nextCards is None)


def testGetNextLowerAndUpperCardsSingleCard():
    suit = "S"
    cards = ["S7"]
    nextCards = sevens.getNextLowerAndUpperCard(suit, cards)
    assert(nextCards == ["S6", "S8"])


def testGetNextLowerAndUpperCardsLowerBoundary():
    suit = "H"
    cards = ["HA", "H2", "H3", "H4", "H5", "H6", "H7"]
    nextCards = sevens.getNextLowerAndUpperCard(suit, cards)
    assert(nextCards == ["H8"])


def testGetNextLowerAndUpperCardsHigherBoundary():
    suit = "H"
    cards = ["H7", "H8", "H9", "H10", "HJ", "HQ", "HK"]
    nextCards = sevens.getNextLowerAndUpperCard(suit, cards)
    assert(nextCards == ["H6"])


def testGetValidCards():
    validCards = sevens.getValidCards()
    filterValidCards = filter(
        lambda card: card in ["H7", "S7", "D7", "C7"], validCards
        )
    assert(len(list(filterValidCards)) == len(validCards))


testCorrectStartingPlayerReturned()
testNoPlayerReturnedWhenNoSevenOfSpades()
testGetNextPlayerReturnsNextPlayer()
testGetNextPlayerReturnsIndexZeroAfterLastPlayer()
testGetNextLowerAndUpperCardsEmptyList()
testGetNextLowerAndUpperCardsSingleCard()
testGetNextLowerAndUpperCardsLowerBoundary()
testGetNextLowerAndUpperCardsHigherBoundary()
testGetValidCards()
