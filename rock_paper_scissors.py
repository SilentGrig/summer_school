import random

handCounter = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}


def getComputerChoice(options):
    options = list(options.keys())
    return random.choice(options)

computerChoice = getComputerChoice(handCounter)

print(computerChoice)
