class Player:
    def __init__(self, avatar: str) -> None:
        self.avatar = avatar
        self.score = 0
        self.positions = []


class Board:
    def __init__(self) -> None:

        self.board = ''' 
                    1 | 2 | 3 
                    ===+===+===  
                    4 | 5 | 6  
                    ===+===+===
                    7 | 8 | 9 
                    '''

        self.available_moves = [
            '1', '2', '3',
            '4', '5', '6',
            '7', '8', '9'
        ]

        self.winning_combinations = [
            ['1', '2', '3'], 
            ['4', '5', '6'], 
            ['7', '8', '9'], 
            ['1', '4', '7'], 
            ['2', '5', '8'], 
            ['3', '6', '9'],
            ['1', '5', '9'], 
            ['3', '6', '9']
            ]

    def draw_board(self):
        print(self.board)

    def __update_Board(self, avatar: str, position: str):

        self.board = self.board.replace(position, avatar)


    def ask_for_move(self, player):

        position = input(f'{player.avatar} turn: Input the position you wish to play: ')
        
        if position in self.available_moves:
            self.available_moves.remove(position)
            self.__update_Board(player.avatar, position)
            player.positions.append(position)

        else:
            print(f'Invalid Position. Available positions are: {self.available_moves}')
            self.draw_board()
            self.ask_for_move(player)


    def end_game(self, player):
        for combination in self.winning_combinations:
            winning_combo = 0
            for winning_position in combination:
                for player_position in player.positions:
                    if winning_position == player_position:
                        winning_combo += 1
                if winning_combo == 3:
                    player.score += 1
                    print(player.avatar + " Won!!")
                    return True

        if len(self.available_moves) == 0:
            print('Draw') 
            return True
            

player_1 = Player('X')

player_2 = Player('O')

players = [player_1, player_2]

def tictactoe():

    board = Board()

    game_is_on = True

    while game_is_on:
    
        for player in players:

            import os
            os.system('cls')
            

            print(f'Current scores are: \nPlayer-1: {player_1.score}\nPlayer-2: {player_2.score}')

            #Draw Board
            board.draw_board()  

            #Ask for move
            board.ask_for_move(player)

            #Start checking for a winner when a player has made more than two moves.
            if len(player.positions) > 2:

                #check if the game has ended by returning true for win or draw
                if board.end_game(player):

                    #if a player has won or drawn. Ask to play again.or end game.
                    to_continue = input('Do you wish to continue playing? ').upper()

                    if to_continue == 'Y':

                        tictactoe()
                        
                        for player in players:

                            player.positions = []

                    else:
                        game_is_on = False
                    
            if not game_is_on:
                    break
 
            
tictactoe()