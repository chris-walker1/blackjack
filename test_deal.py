from blackjack import deal

def test_deal_picture_cards():
    deck = [11, 12, 13, 14]
    hand = deal(deck)
    assert(hand in ["J", "Q", "K", "A"])
