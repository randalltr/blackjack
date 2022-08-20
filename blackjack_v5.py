import random

""" CALCULATE HAND TOTAL """


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


def card_total():
    print(f"Player's hand is {player} with a total of {player_total}.")
    print(f"Dealer's hand is {dealer} with a total of {dealer_total}.")


# def ace_check(hand, total):
#     if "A" in hand:
#         for card in hand:
#             if card == "J" or card == "Q" or card == "K":
#                 card = 10
#             elif card == "A":
#                 card = 1
#             else:
#                 card = int(card)
#             total += card
#         return total


def heads_up():
    print(f"Player's hand is {player}.")
    print(f"Dealer is showing {dealer[0]}.")


def declare_winner():
    if player_total > dealer_total:
        print("Player wins!")
        exit()
    elif dealer_total > player_total:
        print("Dealer wins!")
        exit()
    else:
        print("It was a tie!")
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
# print(player)
# print(dealer)

""" CALCULATE HAND TOTALS """

player_total = 0
dealer_total = 0

player_total = calculate_hand(player, player_total)

dealer_total = calculate_hand(dealer, dealer_total)

""" ASK PLAYER TO HIT """

while True:
    if player_total > 21:
        # player_total = ace_check(player, player_total)
        card_total()
        print("Player busts!")
        exit()
    else:
        heads_up()
        choice = input("Would you like to hit (H) or stand (S)? ").lower()
        if choice == "hit" or choice == "h":
            player_total = 0
            player.append(deck.pop())
            player_total = calculate_hand(player, player_total)
        elif choice == "stand" or choice == "s":
            """ DEALER HITS """
            if dealer_total < 17:
                dealer_total = 0
                dealer.append(deck.pop())
                dealer_total = calculate_hand(dealer, dealer_total)
                if dealer_total > 21:
                    # dealer_total = ace_check(dealer, dealer_total)
                    card_total()
                    print("Dealer busts!")
                    exit()
            card_total()
            declare_winner()
        else:
            print("Invalid input. Hit (H) or stand (S)? ")

""" DEALER HITS """
# while True:
#     if dealer_total < 17:
#         dealer_total = 0
#         dealer.append(deck.pop())
#         dealer_total = calculate_hand(dealer, dealer_total)
#         if dealer_total > 21:
#             card_total()
#             print("Dealer busts!")
#             exit()
#     break

""" DECLARE WINNER """

# card_total()

# declare_winner()


# Compare Player and Dealers Cards
