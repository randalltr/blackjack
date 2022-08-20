import random

""" CALCULATE HAND TOTAL """

# def calculate_hand(player, player_total):


""" CREATE AND SHUFFLE DECK """

deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
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

for card in player:
    if card == "J" or card == "Q" or card == "K":
        card = 10
    elif card == "A":
        card = 11
    else:
        card = int(card)
    player_total += card

for card in dealer:
    if card == "J" or card == "Q" or card == "K":
        card = 10
    elif card == "A":
        card = 11
    else:
        card = int(card)
    dealer_total += card


""" DEALER HITS """
while True:
    if dealer_total < 17:
        dealer.append(deck.pop())
        if card == "J" or card == "Q" or card == "K":
            card = 10
        elif card == "A":
            card = 11
        else:
            card = int(card)
        dealer_total += card
    break

""" DECLARE WINNER """

print(f"Player's hand was {player} with a total of {player_total}.")
print(f"Dealer's hand was {dealer} with a total of {dealer_total}.")

if player_total > dealer_total:
    print("Player wins!")
elif dealer_total > player_total:
    print("Dealer wins!")
else:
    print("It was a tie!")


# Compare Player and Dealers Cards
