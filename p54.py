# Problem 54
# How many hands does Player 1 win?

from itertools import groupby

def special_cards(ch):
    if ch.isdigit():
        return int(ch)
    if ch == "T":
        return 10
    if ch == "J":
        return 11
    if ch == "Q":
        return 12
    if ch == "K":
        return 13
    if ch == "A":
        return 14


def format_card(hand):
    my_list = [[special_cards(card[0]), card[1]] for card in hand]
    my_list.sort(key=lambda x: x[0])
    return my_list


def score(hand):
    # number of same card suit

    num_suits = [len(list(group)) for key, group in groupby([card[1] for card in hand])]
    flush = 5 in num_suits

    straight = (hand[1][0] == hand[0][0] + 1 and hand[2][0] == hand[0][0] + 2 and hand[3][0] == hand[0][0] + 3
                and hand[4][0] == hand[0][0] + 4)
    if straight:
        if flush:
            if hand[0][0] == 10:
                return [10, []]  # Royal Flush
            return [9, [hand[0][0]]] # Straight Flush
        return [5, [hand[0][0]]]  # Straight
    if flush:
        return [6, [hand[4][0], hand[3][0], hand[2][0], hand[1][0], hand[0][0]]]  # Flush

    # number of same card value
    num_values = [len(list(group)) for key, group in groupby([card[0] for card in hand])]

    if 4 in num_values:
        return [8, []]   # Four of a kind
    if 3 in num_values:
        if 2 in num_values:
            return [7, []]  # Full House
        return [4, []]  # Three of a Kind
    if 2 in num_values:
        num_values.remove(2)
        if 2 in num_values:
            return [3, []]  # Two Pairs
        return [2, []]  # Pair
    return 1

player_one_wins = 0
file = open("./Data/p054_poker.txt", "r")
for line in file:
    arr = line.strip("\n").split(" ")
    hand1 = arr[0:5]
    hand2 = arr[5:10]
    format_hand1 = format_card(hand1)
    format_hand2 = format_card(hand2)
    s1 = score(format_hand1)
    s2 = score(format_hand2)

    if s1[0] > s2[0]:
        player_one_wins += 1
    if s1[0] == s2[0]:
        while s1[1][    ]

    print(format_hand1)
    print(format_hand2)
    print(player_one_wins)
