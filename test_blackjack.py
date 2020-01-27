from blackjack import seed_deck, shuffle_deck


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


def shuffle_deck_empty_deck():
    in_deck = []
    out_deck = shuffle_deck(in_deck)
    assert(out_deck == [])


def shuffle_deck_one_card():
    in_deck = [('C', '3')]
    out_deck = shuffle_deck(in_deck)
    assert(out_deck == [('C', '3')])


def shuffle_deck_four_cards():
    in_deck = [('C', '3'), ('H', '3'), ('S', '3'), ('D', '3')]
    out_deck = shuffle_deck(in_deck)
    for i in in_deck:
        assert(i in out_deck)


def shuffle_deck_all_cards():
    in_deck = seed_deck(1)
    out_deck = shuffle_deck(in_deck)
    assert(len(out_deck == 51))
