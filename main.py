from player import *
from board import *

player_1 = Player('X')

player_2 = Player('O')

players = [player_1, player_2]


def tictactoe():
    from random import choice
    randomized_players = []
    randomized_players.append(choice(players))
    while len(randomized_players) < 2:
        player = choice(players)
        if randomized_players[0] != player:
            randomized_players.append(player)

    board = Board()

    game_is_on = True

    while game_is_on:
    
        for player in randomized_players:

            import os
            os.system("cls")

            print(f'Current scores are: \nPlayer {player_1.get_avatar()}: {player_1.score}\nPlayer {player_2.get_avatar()}: {player_2.score}')

            #Draw Board
            print(board.draw_board())

            #Ask for move
            pos = None
            while pos == None:
                pos = board.ask_for_move(player)
    
            board.update_Board(player.get_avatar(), pos)
            
            #Start checking for a winner when a player has made more than two moves.
            if len(player.positions) > 2:

                #check if the game has ended by returning true for win or draw
                if board.end_game(player):

                    print(board.draw_board())

                    #if a player has won or drawn. Ask to play again.or end game.
                    to_continue = input('Do you wish to continue playing? ').lower()

                    if to_continue == 'y' or to_continue == 'yes':

                        for player in players:

                            player.positions = []

                        tictactoe()

                    else:
                        game_is_on = False
                    
            if not game_is_on:
                    break
 
            
tictactoe()