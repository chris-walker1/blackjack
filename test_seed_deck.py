from blackjack import seed_deck


def test_seed_deck_has_ace_clubs():
    deck = seed_deck(1)
    assert(tuple(('C', 'A')) in deck)


def test_seed_deck_has_ace_hearts():
    deck = seed_deck(1)
    assert(tuple(('H', 'A')) in deck)


def test_seed_deck_has_ace_spades():
    deck = seed_deck(1)
    assert(tuple(('S', 'A')) in deck)


def test_seed_deck_has_ace_diamonds():
    deck = seed_deck(1)
    assert(tuple(('D', 'A')) in deck)


def test_seed_deck_with_4_decks_has_208_cards():
    deck = seed_deck(4)
    assert(len(deck) == 208)


def test_seed_deck_with_6_decks_has_312_cards():
    deck = seed_deck(6)
    assert(len(deck) == 312)
