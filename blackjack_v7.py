"""
BLACKJACK GAME v7 (19 MAY 2020)
by RANDALL TRZASKA
"""

import random

"""
PRINTS CARD TOTALS FOR END OF GAME
"""


def card_total():
    print("\n")
    print(f"Player's hand is {player} with a total of {player_total}.")
    print(f"Dealer's hand is {dealer} with a total of {dealer_total}.")


"""
PRINTS EXPOSED CARD TOTALS FOR HIT OR STAND
"""


def heads_up():
    print("\n")
    print(f"Player's hand is {player} totaling {player_total}.")
    print(f"Dealer is showing {dealer[0]}.")


"""
CALCULATES HAND TOTAL WHEN TOTAL LESS THAN 21
"""


def calculate_hand(hand):
    total = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            card = 10
        elif card == "A":
            card = 11
        else:
            card = int(card)
        total += card
    return total


"""
CALCULATES HAND TOTAL WHEN GREATER THAN 21 AND HOLDING ACES
"""


def calculate_aces(hand):
    total = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            card = 10
        elif card == "A":
            card = 1
        else:
            card = int(card)
        total += card
    return total


"""
COMPARES TOTALS AND DECLARES WINNER
"""


def declare_winner():
    if player_total > dealer_total:
        print("Player wins!")
        print("\n")
        exit()
    elif dealer_total > player_total:
        print("Dealer wins!")
        print("\n")
        exit()
    else:
        print("It was a tie!")
        print("\n")
        exit()


"""
CREATE AND SHUFFLE DECK
"""
deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
        "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
        "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
        "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
random.shuffle(deck)

"""
DEAL CARDS
"""
player = []
dealer = []
player.append(deck.pop())
player.append(deck.pop())
dealer.append(deck.pop())
dealer.append(deck.pop())

"""
CALCULATE HAND TOTALS
"""
player_total = calculate_hand(player)
dealer_total = calculate_hand(dealer)

"""
BLACKJACK GAME LOGIC
"""
while True:
    # Exit game when player busts
    # if player_total > 21 and "A" not in player:
    #     card_total()
    #     print("Player busts! Dealer wins!")
    #     exit()
    # Compare cards and ask to hit or stand
    # else:
    heads_up()
    choice = input("Would you like to hit (H) or stand (S)? ").lower()
    # Add card to players hand when hit
    if choice == "hit" or choice == "h":
        player.append(deck.pop())
        # I
        if player_total > 21 and "A" in player:
            player_total = calculate_aces(player)
        elif player_total > 21 and "A" not in player:
            card_total()
            print("Player busts! Dealer wins!")
            exit()
        else:
            player_total = calculate_hand(player)
    elif choice == "stand" or choice == "s":
        """ DEALER HITS """
        while dealer_total < 17:
            # dealer_total = 0
            dealer.append(deck.pop())
            if dealer_total > 21 and "A" in dealer:
                dealer_total = calculate_aces(dealer)
            elif dealer_total > 21 and "A" not in dealer:
                card_total()
                print("Dealer busts! Player wins!")
                exit()
            else:
                dealer_total = calculate_hand(dealer)

        card_total()
        declare_winner()
    else:
        print("Invalid input. Hit (H) or stand (S)? ")

# TO DO:
# Declare blackjack at 21
# Ace 11 to 1 when over 21
