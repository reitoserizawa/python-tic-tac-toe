import time
from player import HumanPlayer, ComputerPlayer

class TicTacToe:
    def __init__(self):
        # we will use a single list to rep 3 x 3 board
        self.board = [' ' for _ in range(9)]
        # keep track of winner 
        self.current_winner = None
        
    def print_board(self):
        for row in [self.board[i * 3: (i + 1) * 3] for i in range(3)]:
            print(' | ' + ' | '.join(row) + ' | ')
            
    @staticmethod
    def print_board_nums():
        # return as | 0 | 1 | 2 | etc...
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print(' | ' + ' | '.join(row) + ' | ')
            
    def available_moves(self):
        # return []
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return len(self.available_moves())
    
    def make_move(self, square, letter):
        # if valid move, make the move
        # then return true if in valid return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner (self, square, letter):
        # winner if 3 in a row anywherem we have to check all of these!
        # first let's check the row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        # check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # check diagnoals
        # but only if the square is an even number(0, 2, 4, 6, 8)
        # these are the only moves possible to win a diagnoal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            print(diagonal2)
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

def play(game, x_player, o_player, print_game=True):
    # retirn the winner of the game or none for a tie
    if print_game:
        game.print_board_nums()
    
    # starting letter
    letter = 'X'
    # iterate while the game still has empty squares
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')
            
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
                
            # after we made our move, we need to alternate the letters
            letter = 'O' if letter == 'X' else 'X'
            
        # tiny time break to pause
        time.sleep(0.8)
    
    if print_game:
        print("It's a tie!")

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = ComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player,print_game=True)