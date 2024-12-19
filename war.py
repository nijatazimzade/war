import pydealer


deck = pydealer.Deck()
deck.shuffle()

hand_player = deck.deal(26)
hand_computer = deck.deal(26)

while True:
    input("Press enter to draw: ")

    player_move = hand_player.deal(1).cards[0]
    print(player_move)

    computer_move = hand_computer.deal(1).cards[0]
    print(computer_move)

    if player_move.value == computer_move.value:
        print("War!")
        break
    else:
        continue

# next step should be adding to war functionality
# this will involve creating a new deck and dealing 3 cards to each player
# the player with the highest card wins the war, and gets to keep the cards that were played
# the game will continue until one player has all the cards
# also when stack ends, it should shuffle and restart
# also add a way to end the game early if a player wants to quit
# also add a way to display the current score of the game
# also both pc and player should have their own stack lists
