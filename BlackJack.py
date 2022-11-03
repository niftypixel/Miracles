import random

def buildDeck():
    deck = {}
    for suit in ['Spades', 'Hearts', 'Diamonds', 'Clubs']:
        i = 2
        card = {}
        while (i <= 10):
            card = {f'{i} of {suit}':i}
            deck.update(card)
            i += 1
        cards = {f'Ace of {suit}':10, f'King of {suit}':10, f'Queen of {suit}':10, f'Jack of {suit}':10}
        deck.update(cards)
    return deck


def dealCard():
    global deck
    card, value = random.choice(list(deck.items()))
    deck.pop(card)
    return card, value


def startPlay():
    global startCount
    while(True):
        if startCount == 21:
            print('You got BlackJack!')
            break
        elif startCount > 21:
            print(f'You busted with a total of {startCount}!')
            break
        else:
            print(f'Your total is {startCount}')
            print("Do you want to hit or stand?")
            print("1. Hit")
            print("2. Stand")
            choice = input()
            if choice == "2":
                print("You stand")
                break
            else:
                card, value = dealCard()
                print(f"{card} was dealt")
                startCount += value

deck = buildDeck()
while(True):
    startCount = 0
    card, value = dealCard()
    print(f"{card} was dealt")
    startCount += value
    card, value = dealCard()
    print(f"{card} was dealt")
    startCount += value
    startPlay()
    print("------------------------------")
    print(f"There are {len(deck)} cards left in the deck")
    print("------------------------------")