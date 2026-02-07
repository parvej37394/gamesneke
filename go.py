def start_game():
    print("start game....")
    play_again = input(" what to play again? (y/n): ")
    if play_again.lower() == 'y': start_game()
    else : print("Thanks you")

start_game()