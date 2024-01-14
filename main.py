import random
import os
from art import logo

cards_values = {
  'A♥' : 11, 'A♦' : 11, 'A♣' : 11, 'A♠' : 11,
  'K♥' : 10, 'K♦' : 10, 'K♣' : 10, 'K♠' : 10,
  'Q♥' : 10, 'Q♦' : 10, 'Q♣' : 10, 'Q♠' : 10,
  'J♥' : 10, 'J♦' : 10, 'J♣' : 10, 'J♠' : 10,
  '10♥' : 10, '10♦' : 10, '10♣' : 10, '10♠' : 10,
  '9♥' : 9, '9♦' : 9, '9♣' : 9, '9♠' : 9,
  '8♥' : 8, '8♦' : 8, '8♣' : 8, '8♠' : 8,
  '7♥' : 7, '7♦' : 7, '7♣' : 7, '7♠' : 7,
  '6♥' : 6, '6♦' : 6, '6♣' : 6, '6♠' : 6,
  '5♥' : 5, '5♦' : 5, '5♣' : 5, '5♠' : 5,
  '4♥' : 4, '4♦' : 4, '4♣' : 4, '4♠' : 4,
  '3♥' : 3, '3♦' : 3, '3♣' : 3, '3♠' : 3,
  '2♥' : 2, '2♦' : 2, '2♣' : 2, '2♠' : 2,
}

cards = ['A♥', 'A♦', 'A♣', 'A♠', 'K♥', 'K♦', 'K♣', 'K♠', 'Q♥', 'Q♦', 'Q♣', 'Q♠', 'J♥', 'J♦', 'J♣', 'J♠', '10♥', '10♦', '10♣', '10♠', '9♥', '9♦', '9♣', '9♠', '8♥', '8♦', '8♣', '8♠', '7♥', '7♦', '7♣', '7♠', '6♥', '6♦', '6♣', '6♠', '5♥', '5♦', '5♣', '5♠', '4♥', '4♦', '4♣', '4♠', '3♥', '3♦', '3♣', '3♠', '2♥', '2♦', '2♣', '2♠']


def hands_setup(player_cards,dealer_cards):
  hand = []
  dealer = []
  for i in range(0,player_cards):
    hand.append(cards.pop(cards.index(cards[random.randrange(0,len(cards))])))  
  for i in range(0,dealer_cards):
    dealer.append(cards.pop(cards.index(cards[random.randrange(0,len(cards))])))
  return hand, dealer

def hit(list, house):
  if sum_cards(list) > 21:
    print(f"You lose! 💥💥💥 Your hand value is {sum_cards(list)}!")
    play_again = input("Do you want to play again? Type 'y' to try again, type 'n' to refuse: ").lower()
    if play_again == "y":
      blackjack()
    else:
      os.system('cls')
  another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
  if another_card == 'y':
    list.append(hands_setup(1,0)[0][0])
    print(f"Your cards: {list}\nComputer's first card: {house}")
    hit(list, house)
  return list

def final_hand(hand,house):
  total_value = 0
  reference_value = sum_cards(hand)
  while total_value < 21 and total_value < reference_value:   
    total_value = 0
    house.append(hands_setup(0,1)[1][0])
    total_value = sum_cards(house)
  return house

def sum_cards(hand):
  values = []
  sum_hand = 0
  ace_present = 0
  for card in hand:
    values.append(cards_values[card])
    if card[0] == 'A':
      ace_present += 1
  for value in values:
    sum_hand += value
  if ace_present > 0 and sum_hand > 21:
    sum_hand -= 10*ace_present
  return sum_hand
  
def blackjack():
  os.system('cls')
  print(logo)
  player = hands_setup(2,0)[0]
  dealer = hands_setup(0,1)[1]
  print(f"Your cards: {player}\nComputer's first card: {dealer}")
  final_player = hit(player, dealer)
  final_dealer = final_hand(player, dealer)
  print(f"Your final hand: {final_player}\nComputer's final hand: {final_dealer}")
  player_points = sum_cards(final_player)
  dealer_points = sum_cards(final_dealer)
  print(f"Your score is {player_points}, and the dealer score is {dealer_points}")
  if player_points == dealer_points:
    print("What are the odds? This is a draw!!")
  elif player_points > dealer_points or dealer_points > 21:
    print("Congratulations! You win!")
  else: 
    print("You lose! Try again!")
  play_again = input("Do you want to play again? Type 'y' to try again, type 'n' to refuse: ").lower()
  if play_again == "y":
    blackjack()
  else:
    os.system('cls')

blackjack()