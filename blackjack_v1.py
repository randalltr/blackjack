import random

# Initialize card numbers

cards = ["AD", "2D"]




"""
cards = {"AD": 11, "2D": 2, "3D": 3, "4D": 4, "5D": 5, "6D": 6,
         "7D": 7, "8D": 8, "9D": 9, "10D": 10, "JD": 10, "QD": 10, "KD": 10,
         "AH": 11, "2H": 2, "3H": 3, "4H": 4, "5H": 5, "6H": 6,
         "7H": 7, "8H": 8, "9H": 9, "10H": 10, "JH": 10, "QH": 10, "KH": 10,
         "AC": 11, "2C": 2, "3C": 3, "4C": 4, "5C": 5, "6C": 6,
         "7C": 7, "8C": 8, "9C": 9, "10C": 10, "JC": 10, "QC": 10, "KC": 10,
         "AS": 11, "2S": 2, "3S": 3, "4S": 4, "5S": 5, "6S": 6,
         "7S": 7, "8S": 8, "9S": 9, "10S": 10, "JS": 10, "QS": 10, "KS": 10}

"""





"""

# Create deck
deck = []
for i in range(4):
    for num in number.keys:
        deck.append(num)

# Shuffle deck
random.shuffle(deck)

# Deal cards to player (p) and dealer (d)
p_card1 = deck.pop()
d_card1 = deck.pop()
p_card2 = deck.pop()
d_card2 = deck.pop()

# Print cards dealt
print(f"You were dealt: {p_card1} {p_card2}\nDealer card showing: {d_card1}")

# Calculate totals
p_total = p_card1 + p_card2
d_total = d_card1 + d_card2

print(p_total, d_total)


# Hit or stay
while True:
    play = input("Hit or Stay? ").lower
    # Pop another card and add to player total
    if play == "hit":

    # If dealer total less than 17 pop card, otherwise compare totals
    if play == "stay":

    else:
        print("Invalid selection")
"""


"""
if number == "J" or number == "Q" or number == "K":
    value = 10
elif number == "A":
    value = 11
else:
    number == int(number)
"""

"""
suite = ["♠", "♥", "♣", "♦"]
number = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

deck = []
for s in suite:
    for n in number:
        deck.append(n + s)
print(deck)
"""
