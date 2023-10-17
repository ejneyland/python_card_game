import sys
import random

game_started = False
# list of cards the player has picked out of the deck
player_cards = []
# list of cards the robot picks from the deck each round
robot_cards = []

def game_header():
  print("""
------------------------
  🐍 PYTHON CARD GAME 🐍
------------------------
Welcome! Enter 1-6 to select one of the following options:
  """, end=' ')
  
def display_suit_options():
  print("""\
  1.  ♡ ♢ ♧ ♤
  2.  😃 😈 😵 🤢 😨
  3.  🤡 👹 👺 👻 👽 👾 🤖
    """, end=' ')
        
def main_menu():
  # start menu welcomes the user and displays 6 options to select from
  global game_started
  print("""
------------------------
1. START GAME (enter 1, followed by a space, then your chosen suit)  e.g. '1 2', '103', '1-1'")
    """)
  
  if not game_started:
    display_suit_options()

  print("""
2. Pick a Card
3. Shuffle Deck
4. Show my Cards
5. Check: Win or Lose
6. EXIT
------------------------
  """, end=' ')

  if game_started:
    print("Game Begun. Options 2-5 are now available.")
  else:
    print("!! You must 'Start Game' first (Option 1), before options 2-5 are executable !!")
  
def selection_input():
  menu_options = ['1', '2', '3', '4', '5', '6']
  suit_options = ['1', '2', '3']

  while True:
    # prompts a selection from the user and accepts a string input
    # [:3] limits the input to 3 characters in length
    # .strip() clears any empty spaces in input; e.g. "  5 " >> "5"
    selection = input("Please enter your selection: ")[:3].strip()

    # if the first char of input contains options 2-5
    if selection:
      if len(selection) <= 3 and selection[0] in menu_options[1:]:
        selection = selection[0] 
      elif selection[0] == '1' and len(selection) == 3 and selection[2] in suit_options:
        selection = selection[:]
      else:
        print("Invalid selection. Please enter one of the available options.")
        continue
      return selection
    else:
      print("Invalid input. Please enter a selection.")

# 1. Start Game method
def start_game():
  print("starting game...")

# create deck function is performed when a user starts the game
# user must select a class of suits (classic, emojisOne, emojisTwo)
def create_deck(suits_selection):

  deck = []

  # defines the different suit types, applicable to different games 
  suits1 = ['♡', '♢', '♧', '♤']
  suits2 = ['😃', '😈', '😵', '🤢', '😨']
  suits3 = ['🤡', '👹', '👺', '👻', '👽', '👾', '🤖']

  # creates numbers 2 .. 10, where str(number)'s value ≈ int(number)  # e.g. '5': 5
  numbers = [str(i) for i in range(2, 11)]
  letters = ['J', 'Q', 'K', 'A']
  values = numbers + letters

  if suits_selection == '1':
    suits = suits1
  elif suits_selection == '2':
    suits = suits2
  elif suits_selection == '3':
    suits = suits3
  else:
    print("Create Deck: unsuccessful")
    return

  print("suits: ", end=" ")
  for suit in suits: 
    print(f"{suit}", end = " ")

  # creating a deck of cards for standard suits game, suits1
  for value in values: # for each individual value in the values[] set
    for suit in suits:  # for each individual suit in the (e.g.) set ♡, ♢, ♧, ♤
      card = (value, suit) # each card is named value + suit, e.g. '5♡'
      deck.append(card) # unique value-suit card is added to the deck
  
  return deck, suits

# displays every card in the parsed deck []
# printing a card-like string representation, e.g. |5♡| |7♧| |Q♢|
def display_deck(deck):
  print('\n')
  for i, card in enumerate(deck, 1):
    value = card[0]
    suit = card[1]
    print(f"|{value}{suit}|", end=' ')
    if i % 12 == 0:  # Start a new line after every 12 cards
      print('\n')
  print('\n')

# 2. Pick Card method
def pick_card(deck):
  global player_cards, robot_cards
  print("picking a card...")

  for loop in range(2):
    # generates random index between 0 and -1
    random_index = random.randint(0, len(deck) - 1)
    # takes a card from the deck, removing it from that set
    picked_card = deck.pop(random_index)

    # defining values inside tuple element (value, suit)
    value = picked_card[0]
    suit = picked_card[1]

    if loop == 0:
      # appends the removed deck card to the players cards
      player_cards.append(picked_card)
      print(f"\nPlayer picked up .. |{value}{suit}|" )
    else:
      robot_cards.append(picked_card)
      print(f"\nRobot picked up .. |{value}{suit}|" )

# 3. Shuffle Deck method
def shuffle_deck(deck, suits): # 3
  print("shuffling deck...")

  start_index = 0 # ace of first suit
  middle_index = len(deck)//2
  last_index = -1 # K of last suit

  # excludes indexes from the shuffle, leaving fixed positions for the 3 cards
  excluded_indices = [start_index, middle_index, last_index]

  for card in deck:
    value = card[0] 
    suit = card[1]
    if value == 'A' and suit == suits[0]:
      first_card = card
      deck[start_index] = first_card
    elif value == 'Q' and suit == suits[1]:
      middle_card = card
      deck[middle_index] = middle_card
    elif value == 'K' and suit == suits[-1]:
      end_card = card
      deck[last_index] = end_card

  # defines two ranges, between first and middle, middle and end
  shuffable_cards = [deck[i] for i in range(len(deck)) if i not in excluded_indices]

  # shuffles the shuffable cards (excl. first, middle, end)
  random.shuffle(shuffable_cards)

  # re-assembles the shuffled deck, with the fixed cards in their intended positions
  shuffled_deck = [first_card] + shuffable_cards[:len(deck)//2] + [middle_card] + shuffable_cards[len(deck)//2-1:] + [end_card]

  return shuffled_deck

# 4. Show Cards method
def show_cards(): 
  global player_cards, robot_cards
  print("showing cards...")

  print("\nPlayer's Cards: ", end=" ")
  for card in player_cards:
    print(f"|{card[0]}{card[1]}|", end=" ")
  print("")

# 5. Check Win or Lose method
# contains private methods to check game conditions
def check_win_lose(suits):
  global player_cards, robot_cards

  print("checking: win or lose...")

  def count_value_cards(cards):
    highest_count = 0
    counted_value = None

    unique_values = set(card[0] for card in cards)

    for value in unique_values:
      num_of_matching = cards.count(value)

      if num_of_matching > highest_count:
        highest_count = num_of_matching
        counted_value = value

    return highest_count, counted_value
  
  def count_suit_cards(cards):
    count = 0
    for card in cards:
     if card[1] == suits[1]:
       count += 1
    return
  
  def calculate_average(cards):
    total_value = 0
    for card in cards:
      value = card[0]
      # letters_value = {'A': 1, 'J': 11, 'Q': 12, 'K':13}
      if value == 'A':
        total_value += 1
      elif value == 'J':
        total_value += 11
      elif value == 'Q':
        total_value += 12
      elif value == 'K':
        total_value += 13
      else:
        total_value += int(card[0])
  
    average_value = total_value / len(cards)
    return average_value

  player_matching_count, player_matching_value = count_value_cards(player_cards)
  robot_matching_count, robot_matching_value = count_value_cards(robot_cards)

  player_second_suit = count_suit_cards(player_cards)
  robot_second_suit = count_suit_cards(robot_cards)

  player_average_value = calculate_average(player_cards)
  robot_average_value = calculate_average(robot_cards)
  
  # game conditions evaluation logic
  # 1. player holds same value card for all suits
  if player_matching_count == 4 and robot_matching_count == 4:
    print("It's a draw! You and Robot have a complete set of the same value.")
  elif player_matching_count == 4:
    print(f"Player WINS! They have a complete set of the value: {player_matching_value}")
  elif robot_matching_count == 4:
    print(f"You Lose. Robot wins! They have a complete set of the value: {robot_matching_value}")
  # 2. player holds 3 cards of the same value (differing suit)
  elif player_matching_count == 3 and robot_matching_count == 3:
    print("It's a draw! You and Robot both have 3 cards of the same value.")
  elif player_matching_count == 3:
    print(f"Player WINS! They have 3 cards of the value: {player_matching_value}")
  elif robot_matching_count == 3:
    print(f"You Lose. Robot wins! They have 3 cards of the same value: {robot_matching_value}")
  # 3. player holds more cards of the second suit
  elif player_second_suit == robot_second_suit:
    print(f"It's a draw! You and Robot both have the same number of {suits[1]} cards")
  elif player_second_suit > robot_second_suit:
    print(f"Player WINS! You have {player_second_suit} cards of the {suits[1]} suit")
  elif player_second_suit < robot_second_suit:
    print(f"You Lose. Robot wins! They have {player_second_suit} cards of the {suits[1]} suit")
  # 4. player holds a higher avg. of card value
  elif player_average_value > robot_average_value:
    print("Player WINS! They have a higher average value.")
    print(f"Average value: {player_average_value}")
  elif player_average_value < robot_average_value:
    print("You Lose. Robot wins! They have a higher average value.")
    print(f"Average value: {robot_average_value}")
  else:
    print("It's a draw! You and Robot have the same average value.")

# 6. Exit method, executed when user selects 'exit', application is exited
def exit():
  print("exiting application...")
  sys.exit()

# GAME LOGIC, contains all the application logic and is the only method ran at runtime
def main():
  global game_started
  game_header()

  # main game loop
  while True:

    main_menu()

    selection = selection_input()
    primary_choice = selection[0]

    # checks user's input against available options
    # executes prescribed functions of the matched condition
    if primary_choice == '1' and len(selection) == 3:
      if game_started:
        print("Game ended. Starting new game ..")
      start_game()
      suits_selection = selection[2]
      deck, suits = create_deck(suits_selection)
      game_started = True
      display_deck(deck)
    elif selection[0] == '2' and game_started:
      # if a player has 5 cards and picks a card (now 6 cards), the result is checked
      if len(player_cards) == 5:
        pick_card(deck)
        print("You now have a full hand.")
        check_win_lose(suits)
        main() # the game is restarted after displaying the result
      else:
        pick_card(deck)
    elif selection[0] == '3' and game_started:
      deck = shuffle_deck(deck, suits)
      display_deck(deck)
    elif selection[0] == '4' and game_started:
      show_cards()
    elif selection[0] == '5' and game_started:
      check_win_lose(suits)
    elif selection[0] == '6' and game_started:
      exit()
    else:
      print("Invalid selection. Please enter one of the available options.")
      selection_input()

main()