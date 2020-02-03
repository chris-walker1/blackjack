import os
import random

decks = input("Enter number of decks: ")

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4 * int(decks)

wins = 0
losses = 0


def clear():
    if os.name == "nt":
        os.system("CLS")
    if os.name == "posix":
        os.system("clear")


def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11: card = "J"
        if card == 12: card = "Q"
        if card == 13: card = "K"
        if card == 14: card = "A"
        hand.append(card)
    return(hand)


def play_again():
    again = input("Would you like to play again? (Y/N) : ").lower()
    if again == "y":
        dealer_hand = []
        player_hand = []
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4
        game()
    else:
        print("Bye!")
        exit()


def total(hand):
    total = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            total += 10
        elif card == "A":
            if total >= 11:
                total += 1
            else:
                total += 11
        else:
            total += card
    return(total)


def hit(hand):
    card = deck.pop()
    if card == 11: card = "J"
    if card == 12: card = "Q"
    if card == 13: card = "K"
    if card == 14: card = "A"
    hand.append(card)
    return(hand)


def print_results(dealer_hand, player_hand):
    clear()
    print("Welcome to the table!\n")
    print("Wins: " + str(wins))
    print("Losses: " + str(losses))
    print("The dealer has " + str(dealer_hand) + " for " + str(total(dealer_hand)))
    print("You have " + str(player_hand) + " for " + str(total(player_hand)))


def blackjack(dealer_hand, player_hand):
    global wins
    global losses
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("You got Blackjack\n")
        wins += 1
        play_again()
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Dealer got Blackjack\n")
        losses += 1
        play_again()


def score(dealer_hand, player_hand):
    global wins
    global losses
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("You got Blackjack\n")
        wins += 1
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Dealer got Blackjack\n")
        losses += 1
    elif total(player_hand) > 21:
        print_results(dealer_hand, player_hand)
        print("You bust")
        losses += 1
    elif total(dealer_hand) > 21:
        print_results(dealer_hand, player_hand)
        print("Dealer bust")
        wins += 1
    elif total(player_hand) < total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print("You lose")
        losses += 1
    elif total(player_hand) > total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print("You win")


def game():
    global wins
    global losses
    choice = 0
    clear()
    print("Welcome to the table!\n")
    print("Wins: " + str(wins))
    print("Losses: " + str(losses))
    dealer_hand = deal(deck)
    player_hand = deal(deck)
    print("The dealer is showing a " + str(dealer_hand[0]))
    print("You have " + str(player_hand) + " for " + str(total(player_hand)))
    blackjack(dealer_hand, player_hand)
    quit = False
    while not quit:
        choice = input("[H]it or [S]tand? Type Q to quit: ").lower()
        if choice == "h":
            hit(player_hand)
            print(player_hand)
            print("Hand total: " + str(total(player_hand)))
            if total(player_hand) > 21:
                print("You bust")
                losses += 1
                play_again()
        elif choice == "s":
            while total(dealer_hand) < 17:
                hit(dealer_hand)
                print(dealer_hand)
                if total(dealer_hand) > 21:
                    print("Dealer bust")
                    wins += 1
                    play_again()
            score(dealer_hand, player_hand)
            play_again()
        elif choice == "q":
            print("Bye!")
            quit = True
            exit()


if __name__ == "__main__":
    game()
    
