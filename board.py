class Board:
    def __init__(self) -> None:

        self.__board = ''' 
                    1 | 2 | 3 
                    ===+===+===  
                    4 | 5 | 6  
                    ===+===+===
                    7 | 8 | 9 
                    '''

        self.__available_moves = [
            '1', '2', '3',
            '4', '5', '6',
            '7', '8', '9'
        ]

        self.__winning_combinations = [
            # Horizontal
            ['1', '2', '3'], 
            ['4', '5', '6'], 
            ['7', '8', '9'], 
            # Vertical
            ['1', '4', '7'], 
            ['2', '5', '8'], 
            ['3', '6', '9'],
            # Diagonal
            ['1', '5', '9'], 
            ['3', '5', '7']
            ]

    def draw_board(self):
        return self.__board

    def update_Board(self, avatar: str, position: str):

        self.__board = self.__board.replace(position, avatar)
        print('replaced successfully')


    def ask_for_move(self, player):

        position = input(f'{player.get_avatar()} turn: Input the position you wish to play: ')
        
        if position in self.__available_moves:
            self.__available_moves.remove(position)
            player.positions.append(position)

            return position 

        else:
            print(f'Invalid Position. Available positions are: {self.__available_moves}')
            print(self.draw_board())

            return


    def end_game(self, player):
        for winning_combination in self.__winning_combinations:
            winning_combo = 0
            for position in winning_combination:
                for player_position in player.positions:
                    if position == player_position:
                        winning_combo += 1
                if winning_combo == 3:
                    player.score += 1
                    print(player.get_avatar() + " Wins!!")
                    return True

        if len(self.__available_moves) == 0:
            print('Draw') 
            return True