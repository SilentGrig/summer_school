import poker_score
import cardGame

PLAYER = 0

deck = cardGame.getDeck()
cardGame.shuffleDeck(deck)
hands = []


def getPlayerCommand():
    command = input("Enter a command - 'check' or 'fold' to quit: ")
    while command not in ["check", "fold"]:
        command = input("Please enter a valid command - 'check' or 'fold' to quit: ")
    return command


def getNumberOfComputers():
    while True:
        try:
            numberOfComputerPlayers = int(input("Please enter number of computer players: "))
            if numberOfComputerPlayers >= 1 and numberOfComputerPlayers <= 4:
                return numberOfComputerPlayers
            else:
                print("number must be between 1 and 4")
        except ValueError:
            print("Please give a number between 1 and 4")


def buildHandsToBePlayed(hands, middle):
    handsToBePlayed = []
    for hand in hands:
        handsToBePlayed.append(hand + middle)
    return handsToBePlayed


def printPlayedHands(playedHands):
    print("Player hand: " + formatHandString(playedHands[PLAYER]))
    for i in range(1, len(playedHands)):
        hand = playedHands[i]
        print("Computer " + str(i) + " hand: " + formatHandString(hand))


def printSingleWinner(player, hand, winType):
    if player == PLAYER:
        print("Player wins with " + winType + " : " + formatHandString(hand))
    else:
        print("Computer " + str(player) + " wins with " + winType + " : " + formatHandString(hand))


def printWinners(winningHands, playedHands, winType):
    print("-" * 30)
    printPlayedHands(playedHands)
    print("-" * 30)
    if len(winningHands) != 1:
        print("Tied Game!")
    for player, hand in winningHands.items():
        printSingleWinner(player, hand, winType)


def formatHandString(hand):
    return ", ".join(hand)


def main():
    print("Welcome to the Game!")
    numberOfComputerPlayers = getNumberOfComputers()
    numOfPlayers = numberOfComputerPlayers + 1
    cardGame.dealCards(deck=deck, numOfCards=2, numOfPlayers=numOfPlayers, hands=hands)
    playerHand = hands[0]
    middle = []

    while True:
        print()
        print("Player Hand: " + formatHandString(playerHand))
        print("Middle: " + formatHandString(middle))
        command = getPlayerCommand()

        if command == "fold":
            break

        if command == "check":
            cardGame.dealCard(deck, middle)

        if len(middle) >= 3:
            handsToBePlayed = buildHandsToBePlayed(hands, middle)
            winningHands, winType = poker_score.get_winning_hands(handsToBePlayed)
            printWinners(winningHands, handsToBePlayed, winType)
            break


if __name__ == '__main__':
    main()
