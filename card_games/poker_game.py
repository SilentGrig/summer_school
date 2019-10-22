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
    print("Player played: " + str(playedHands[PLAYER]))
    for i in range(1, len(playedHands)):
        hand = playedHands[i]
        print("Computer " + str(i) + " played: " + str(hand))


def printSingleWinner(winningHands):
    winner = winningHands[0]
    winningHand = winningHands[1]
    if winner == PLAYER:
        print("Player wins with: " + str(winningHand))
    else:
        print("Computer " + str(winner) + " wins with: " + str(winningHand))


def printTiedWinners(winningHands):
    print("Tied game")
    for hand in winningHands:
        printSingleWinner(hand)


def printWinners(winningHands, playedHands):
    print("-" * 30)
    printPlayedHands(playedHands)
    print("-" * 30)
    if len(winningHands) == 1:
        printSingleWinner(winningHands[0])
    else:
        printTiedWinners(winningHands)


def main():
    print("Welcome to the Game!")
    numberOfComputerPlayers = getNumberOfComputers()
    numOfPlayers = numberOfComputerPlayers + 1
    cardGame.dealCards(deck=deck, numOfCards=2, numOfPlayers=numOfPlayers, hands=hands)
    playerHand = hands[0]
    middle = []

    while True:
        print()
        print("Player Hand: " + str(playerHand))
        print("Middle: " + str(middle))
        command = getPlayerCommand()

        if command == "fold":
            break

        if command == "check":
            cardGame.dealCard(deck, middle)

        if len(middle) >= 3:
            handsToBePlayed = buildHandsToBePlayed(hands, middle)
            winningHands = poker_score.get_winning_hands(handsToBePlayed)
            printWinners(winningHands, handsToBePlayed)
            break


if __name__ == '__main__':
    main()
