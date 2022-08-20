"""
BLACKJACK v9
by RANDALL TR
MAY 21, 2022

"""


import random


def card_total():
    print("\n")
    print(f"Player's hand is {player} with a total of {player_total}.")
    print(f"Dealer's hand is {dealer} with a total of {dealer_total}.")


def heads_up():
    print("\n")
    print(f"Player's hand is {player} totaling {player_total}.")
    print(f"Dealer is showing {dealer[0]}.")


def calculate_hand(hand, total):
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            card = 10
        elif card == "A":
            card = 11
        else:
            card = int(card)
        total += card
    return total


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


""" CREATE AND SHUFFLE DECK """
deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
        "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
        "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
        "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
random.shuffle(deck)

""" DEAL CARDS """

player = []
dealer = []
player.append(deck.pop())
player.append(deck.pop())
dealer.append(deck.pop())
dealer.append(deck.pop())

""" CALCULATE HAND TOTALS """

player_total = 0
dealer_total = 0
player_total = calculate_hand(player, player_total)
dealer_total = calculate_hand(dealer, dealer_total)

""" ASK PLAYER TO HIT """

print("\n")
print("* * * * * * * * * * * * * * * * * * * * * * * * *")
print("* Welcome to Basic Blackjack!                   *")
print("* In this game, Aces are ALWAYS worth 11.       *")
print("* Also you can't yet split or double down.      *")
print("* Press 'X' or type 'exit' at any time to quit. *")
print("* Shuffle up and deal!                          *")
print("* * * * * * * * * * * * * * * * * * * * * * * * *")

while True:
    if player_total > 21:
        card_total()
        print("Player busts! Dealer wins!")
        print("\n")
        exit()
    else:
        heads_up()
        choice = input(
            "Would you like to hit (H) or stand (S)? ").lower()
        if choice == "exit" or choice == "x":
            exit()
        elif choice == "hit" or choice == "h":
            player_total = 0
            player.append(deck.pop())
            player_total = calculate_hand(player, player_total)
        elif choice == "stand" or choice == "s":
            """ DEALER HITS """
            while dealer_total < 17:
                dealer_total = 0
                dealer.append(deck.pop())
                dealer_total = calculate_hand(dealer, dealer_total)
                if dealer_total > 21:
                    card_total()
                    print("Dealer busts! Player wins!")
                    print("\n")
                    exit()
            card_total()
            declare_winner()
        else:
            print("Invalid input. Hit (H) or stand (S)? ")

# TO DO:
# Declare blackjack at 21
# Ace 11 to 1 when over 21
# Continue playing until choose to quit
