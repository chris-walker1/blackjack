from blackjack import seed_deck, shuffle_deck, hello_world


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
    assert(len(out_deck == 52))


def test_hello_world():
    message = hello_world()
    assert(message == 'Hello World')
