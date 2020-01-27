import numpy

suit = ['C', 'H', 'S', 'D']
value = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


def seed_deck(num_decks):
    deck = []
    for d in range(num_decks):
        for i in suit:
            for j in value:
                deck.append(tuple((i, j)))
    return(deck)


def shuffle_deck(deck):
    numpy.random.shuffle(deck)
    return()
