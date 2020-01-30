from blackjack import seed_deck, shuffle_deck

deck = seed_deck(6)
print(deck)

shuffled_deck = shuffle_deck(deck)
print(shuffled_deck)

small_deck = [('C', '3')]
shuffle_small_deck = shuffle_deck(small_deck)
print(shuffle_small_deck)
