import random

deck_cards = 10
deck_cards_pint = ["🍀","❤️","♠️","💎"]

def create_deck ():
    whole_deck = []
    for card_pint in range(len(deck_cards_pint)):
            for card in range(deck_cards):
                  card_info = {
                        "pint" : deck_cards_pint[card_pint],
                        "number" : card + 1
                  }
                  whole_deck.append(card_info)
    return whole_deck

def shufle_cards (cards):
    for card in range(len(cards)):      
        random.shuffle(cards)
    return cards
      
def remove_card (cards):
    card_removed = cards.pop()
    return card_removed

     
def game ():
    player_total = 0
    casino_total = 17
    print("Welcome to 21 black jack")
    player_money = 50
    print("Let's start")
    total = remove_card(shufle_cards(create_deck()))["number"] + remove_card(shufle_cards(create_deck()))["number"]
    one_first_card = input(f"You already have {total}, Do you want another card: ")
    if one_first_card == "yes":
        total += remove_card(shufle_cards(create_deck()))["number"]
        one_second_card = input(f"You already have {total}, Do you want another card: ")
        if one_second_card == "yes":
            total += remove_card(shufle_cards(create_deck()))["number"]
            one_third_card = input(f"You already have {total}, Do you want another card: ")
            if one_third_card == "yes":
                total += remove_card(shufle_cards(create_deck()))["number"]
                print(f"Your total score is {total}")
            else:
             print(f"your Score is {total}, Now is the dealer's turn, Good luck") 
        else:
            print(f"your Score is {total}, Now is the dealer's turn, Good luck") 
    else:
         print(f"your Score is {total}, Now is the dealer's turn, Good luck") 

    return total
         
game()
