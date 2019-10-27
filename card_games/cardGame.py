import random

SUITS = {"D": "Diamonds", "C": "Clubs", "H": "Hearts", "S": "Spades"}
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
RANK_TO_VALUE = {"A": ("01", "14"), "1": "01", "2": "02", "3": "03", "4": "04",
                 "5": "05", "6": "06", "7": "07", "8": "08", "9": "09",
                 "10": "10", "J": "11", "Q": "12", "K": "13"}
VALUE_TO_RANK = {"01": "A", "02": "2", "03": "3", "04": "4", "05": "5",
                 "06": "6", "07": "7", "08": "8", "09": "9", "10": "10",
                 "11": "J", "12": "Q", "13": "K", "14": "A"}


def getDeck():
    """ Builds a deck of card
        Returns list """
    deck = []
    for suit in SUITS.keys():
        for rank in RANKS:
            deck.append(suit + rank)
    return deck


def shuffleDeck(deck):
    """ Shuffles Deck
        Returns List """
    random.shuffle(deck)
    return deck


def dealCard(deck, hand):
    """ Removes last card from deck and adds to hand
        Returns a boolean on outcome
    """
    # make sure there are cards to deal
    if len(deck) > 0:
        card = deck.pop()
        hand.append(card)
        return True
    return False


def dealCards(deck, numOfCards, numOfPlayers, hands=[]):
    """ Takes a deck and deals given number of cards in
        a given number of hands
        Returns a list of lists each list is a player's hand """
    # if number of cards not provided, deal all cards evenly
    if numOfCards == 0:
        numOfCards = (len(deck) // numOfPlayers) + 1
    # create empty list for each player
    if len(hands) == 0:
        for _ in range(numOfPlayers):
            hands.append([])
    for _ in range(numOfCards):
        for player in range(numOfPlayers):
            dealCard(deck, hands[player])
    return hands


def printHands(hands):
    """ print a players hand to the screen
        first player is player 1
        Doesn't Return """
    for player, hand in enumerate(hands):
        print(str(player + 1) + " - " + str(hand))


def getHandIndexOfCard(hands, cardToFind):
    """ Return the index of the hand for the card
        Return int or None """
    for handIndex, hand in enumerate(hands):
        for card in hand:
            if card == cardToFind:
                return handIndex
    return None


def convertHandToValues(hand, aceHigh=False):
    """ Converts each card in a hand to it's value format
        e.g SJ -> S11
        Doesn't Return """
    for index, card in enumerate(hand):
        hand[index] = convertCardToValue(card, aceHigh)


def convertCardToValue(card, aceHigh=False):
    """ Converts a card to it's value
        e.g. Jack's value is 11.
        e.g 6's value is 06
        aceHigh determines if an Ace is valued at 1 or 14
        Return String """
    suit = card[0]
    rank = card[1:]
    if rank != "A":
        return suit + RANK_TO_VALUE[rank]
    elif rank == "A":
        return suit + (RANK_TO_VALUE[rank][1] if aceHigh
                       else RANK_TO_VALUE[rank][0])


def convertHandToRanks(hand):
    """ Converts a hand to it's rank
        Doesn't Return """
    for index, card in enumerate(hand):
        hand[index] = convertCardToRank(card)


def convertCardToRank(card):
    """ Converts a card to it's ranked
        e.g. 11 rank is J.
             01 and 14 is A
        Returns String """
    suit = card[0]
    value = card[1:]
    if len(value) < 2:
        value = "0" + value
    return suit + VALUE_TO_RANK[value]


def sortHandByRank(hand, aceHigh=False):
    """ Sort a hand in place, sorted by rank
        Doesn't Return """
    convertHandToValues(hand, aceHigh)
    hand.sort(key=lambda card: card[1:])
    convertHandToRanks(hand)


def sortHandBySuitThenRank(hand, aceHigh=False):
    """ Sort a hand in place, sorted by suit then rank
        Doesn't Return """
    convertHandToValues(hand, aceHigh)
    hand.sort()
    convertHandToRanks(hand)


def doesHandContainCard(hand, cardToFind):
    """ Determines if a card is found in hand
        Returns True or False """
    for card in hand:
        if card == cardToFind:
            return True
    return False


def getCardValue(card, aceHigh):
    """ Gets the value of a card
        Returns int """
    cardAsValue = convertCardToValue(card, aceHigh)
    return int(cardAsValue[1:])


def doesHandContainValue(hand, valueToFind, aceHigh=False):
    """ Determines if a card with a certain value is found in hand
        Returns True or False """
    for card in hand:
        cardValue = getCardValue(card, aceHigh)
        if cardValue == valueToFind:
            return True
    return False


def getCardSuit(card):
    return card[0]
