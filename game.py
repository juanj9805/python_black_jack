import random

CARDS = 10
DECK_CARDS_SUITS = ["🍀","❤️","♠️","💎"]

def create_deck ():
    deck = []
    for suit in range(len(DECK_CARDS_SUITS)):
        for card in range(CARDS):
            card_info = {
                "pint" : DECK_CARDS_SUITS[suit],
                "number" : card + 1
            }
            deck.append(card_info)
    return deck

def shufle_deck (deck):
    random.shuffle(deck)
    return deck
 
def remove_card (deck):
    card_removed = deck.pop()
    return card_removed

def game ():
    deck_shufled = shufle_deck(create_deck())
    player_points = 0
    casino_points = 0
    winner = ""
    player_points += remove_card(deck_shufled)["number"] + remove_card(deck_shufled)["number"]
    while player_points <= 21:
        choice = input(f"You already have {player_points}\nDo you want another card: ")
        if choice == "yes":
            player_points += remove_card(deck_shufled)["number"]
        elif choice != "yes":
            print(f"Your final score is {player_points}")
            break
    while casino_points <= 21 and casino_points < player_points :
        casino_points += remove_card(deck_shufled)["number"]
    print(f"Casino already has {casino_points}")
    if player_points > casino_points and player_points <=21  :
        winner += "Player"
    elif player_points <= 21 and casino_points >21:
        winner += "Player"
    elif casino_points > player_points and casino_points <=21:
        winner += "Casino"
    elif casino_points > player_points and casino_points <=21:
        winner += "Casino"
    elif casino_points <= 21 and player_points >21:
        winner += "Player"
    else:
        winner += "Draw"
    return print(f"The winner in this turn is\n{winner}")

game()