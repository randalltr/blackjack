"""
BLACKJACK v9
by RANDALL TR
MAY 21, 2022

"""

import random

""" CARD TOTALS FOR END OF GAME """


def card_total():
    print("\n")
    print(f"Player's hand is {player} with a total of {player_total}.")
    print(f"Dealer's hand is {dealer} with a total of {dealer_total}.")


""" CARD TOTALS FOR HIT OR STAND """


def heads_up():
    print("\n")
    print(f"Player's hand is {player} totaling {player_total}.")
    print(f"Dealer is showing {dealer[0]}.")


""" CALCULATE CARD TOTALS """


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


""" DECLARE WINNERS AT END OF GAME """


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

""" WELCOME MESSAGE """

print("\n")
print("* * * * * * * * * * * * * * * * * * * * * * * * *")
print("* Welcome to Basic Blackjack!                   *")
print("* In this game, Aces are ALWAYS worth 11.       *")
print("* Also you can't yet split or double down.      *")
print("* Press 'X' or type 'exit' at any time to quit. *")
print("* Shuffle up and deal!                          *")
print("* * * * * * * * * * * * * * * * * * * * * * * * *")

""" BLACKJACK GAME LOGIC """

while True:

    # If player busts, quit game
    if player_total > 21:
        card_total()
        print("Player busts! Dealer wins!")
        print("\n")
        exit()

    # Ask player to hit or stand (always have option to exit)
    else:
        heads_up()
        choice = input(
            "Would you like to hit (H) or stand (S)? ").lower()
        if choice == "exit" or choice == "x":
            print("Thanks for playing! Goodbye!")
            print("\n")
            exit()
        elif choice == "hit" or choice == "h":
            player_total = 0
            player.append(deck.pop())
            player_total = calculate_hand(player, player_total)
        elif choice == "stand" or choice == "s":

            # Once player stands, dealer hits on less than 17
            while dealer_total < 17:
                dealer_total = 0
                dealer.append(deck.pop())
                dealer_total = calculate_hand(dealer, dealer_total)

                # If dealer busts quit game
                if dealer_total > 21:
                    card_total()
                    print("Dealer busts! Player wins!")
                    print("\n")
                    exit()

            # Show totals and declare winner
            card_total()
            declare_winner()

        # Correction for invalid input
        else:
            print("Invalid input. Hit (H) or stand (S)? ")


""" TO DO: """
# Declare blackjack at 21
# Change Ace value from 11 to 1 when over 21
# Welcome message only plays on first iteration of game
# Continue playing until choose to quit
# Betting and chip count
# Basic strategy trainer
# OOP
