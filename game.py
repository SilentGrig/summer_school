import cardGame

hands = []
deck = cardGame.getDeck()
cardGame.shuffleDeck(deck)

numOfComputerPlayers = int(input("How many computer players? "))

while True:
    command = input("Please enter a command - deal, quit/exit: ")
    if command == "deal":
        hands = cardGame.dealCards(deck, 1, numOfComputerPlayers + 1, hands)
    elif command == "quit" or command == "exit":
        break
    else:
        print("Invalid command.")
    cardGame.printHands(hands)
