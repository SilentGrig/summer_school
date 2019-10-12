import random

SUITS = ["D", "C", "H", "S"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K"]
RANK_TO_VALUE = {"A": ("01", "13"), "1": "01", "2": "02", "3": "03", "4": "04",
                 "5": "05", "6": "06", "7": "07", "8": "08", "9": "09", "J": "10",
                 "Q": "11", "K": "12"}
VALUE_TO_RANK = {"01": "A", "02": "2", "03": "3", "04": "4", "05": "5", "06": "6", "07": "7",
                 "08": "8", "09": "9", "10": "J", "11": "Q", "12": "K", "13": "A"}


def getDeck():
    deck = []
    for suit in SUITS:
        for rank in RANKS:
            deck.append(rank + suit)
    return deck


def shuffleDeck(deck):
    random.shuffle(deck)
    return deck


def dealCard(deck, hand):
    if len(deck) > 0:
        card = deck.pop()
        hand.append(card)
        return True
    return False


def dealCards(deck, numOfCards, numOfPlayers, hands=[]):
    if numOfCards == 0:
        numOfCards = (len(deck) // numOfPlayers) + 1
    if len(hands) == 0:
        for _ in range(numOfPlayers):
            hands.append([])
    for _ in range(numOfCards):
        for player in range(numOfPlayers):
            dealCard(deck, hands[player])
    return hands


def printHands(hands):
    for player, hand in enumerate(hands):
        print(str(player + 1) + " - " + str(hand))


def getHandIndexOfCard(hands, cardToFind):
    for handIndex, hand in enumerate(hands):
        for card in hand:
            if card == cardToFind:
                return handIndex
    return None


def convertHandToValues(hand, AceHigh=False):
    for index, card in enumerate(hand):
        hand[index] = convertCardToValue(card, AceHigh)
    return hand


def convertCardToValue(card, AceHigh=False):
    suit = card[1]
    rank = card[0]
    if rank != "A":
        return RANK_TO_VALUE[rank] + suit
    elif rank == "A":
        return (RANK_TO_VALUE[rank][1] if AceHigh else RANK_TO_VALUE[rank][0]) + suit


def convertHandToRanks(hand):
    for index, card in enumerate(hand):
        hand[index] = convertCardToRank(card)
    return hand


def convertCardToRank(card):
    suit = card[2]
    value = card[:2]
    return VALUE_TO_RANK[value] + suit


def sortHandByRankThenSuit(hand):
    convertHandToValues(hand)
    hand.sort()
    convertHandToRanks(hand)


def doesHandContainCard(hand, cardToFind):
    for card in hand:
        if card == cardToFind:
            return True
    return False


def getCardValue(card):
    return None
