import random

class Player:
    def __init__(self, letter):
        # letter = O or X
        self.letter = letter
        
        # get next move for each player
    def get_move(self, game):
        pass

class ComputerPlayer(Player):
    
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square
    
class HumanPlayer(Player):
    
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn, input move (0-8): ')
            # check that this is a correct value by trying to cast it to an interger, and if it's not then, we say it's invalid
            # if that spot is not available on the board, we also say its in valid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            
            except ValueError:
                print('Invalid square, try again!')
            
        return val